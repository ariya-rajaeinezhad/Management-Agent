from abc import ABC, abstractmethod
import json
import re
from openai import OpenAI
from openai import APIError, APITimeoutError, RateLimitError
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from config import settings

class BaseLLMService(ABC):
    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        pass
    @abstractmethod
    def generate_json(self, prompt: str) -> dict:
        pass

class OpenRouterService(BaseLLMService):
    def __init__(self):
        if not settings.openrouter_api_key:
            raise ValueError("OPENROUTER_API_KEY is not set in environment variables.")
        
        # OpenRouter is fully compatible with the OpenAI SDK
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=settings.openrouter_api_key,
            timeout=settings.llm_timeout
        )
        self.model = settings.llm_model

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception_type(
            (APIError, APITimeoutError, RateLimitError, ValueError, json.JSONDecodeError)
        ),
    )
    def generate_text(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )
        return response.choices[0].message.content

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception_type(
            (APIError, APITimeoutError, RateLimitError, ValueError, json.JSONDecodeError)
        ),
    )
    def generate_json(self, prompt: str) -> dict:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert system. You must respond with ONLY a valid JSON object. Do not include any markdown formatting, explanations, or text outside the JSON."
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
        )
        content = response.choices[0].message.content
        return self._extract_json(content)
    
    def _extract_json(self, text: str) -> dict:
        json_match = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', text)
        if json_match:
            json_str = json_match.group(1)
        else:
            json_str = text.strip()
        
        try:
            parsed = json.loads(json_str)
            if not isinstance(parsed, dict):
                print(f"\n[DEBUG] ERROR: Parsed JSON is not a dictionary! Retrying...")
                raise ValueError(f"Expected a JSON object, but got {type(parsed).__name__}")
            return parsed
        except json.JSONDecodeError as e:
            print(f"\n[DEBUG] Failed to parse JSON: {e}")
            print(f"[DEBUG] Raw response snippet: {text[:300]}...")
            raise ValueError(f"Failed to extract valid JSON: {e}")
        except Exception as e:
            print(f"\n[DEBUG] API Error: {e}")
            raise

def get_llm_service() -> BaseLLMService:
    return OpenRouterService()