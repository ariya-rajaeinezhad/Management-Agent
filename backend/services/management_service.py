from services.llm_service import BaseLLMService
from models import ManagementAnalysis
from prompt_loader import load_prompt
from exceptions import AnalysisError


class ManagementService:
    def __init__(self, llm_service: BaseLLMService):
        self.llm = llm_service

    def analyze(self, topic_en: str, language: str = "fa") -> ManagementAnalysis:
        """
        Analyze the topic using the appropriate prompt based on language.
        
        Args:
            topic_en: Topic in English
            language: Output language ('fa' or 'en')
        """
        try:
            # Load language-specific prompt
            if language == "en":
                template = load_prompt("management_analysis_en.md")
            else:
                template = load_prompt("management_analysis.md")
            
            prompt = template.replace("{topic}", topic_en)
            raw_json = self.llm.generate_json(prompt)
            return ManagementAnalysis.model_validate(raw_json)
            
        except Exception as e:
            error_str = str(e).lower()
            print(f"[DEBUG] Error in analysis: {e}")
            
            if "context" in error_str or "length" in error_str:
                raise AnalysisError("موضوع وارد شده بسیار طولانی یا پیچیده است. لطفاً آن را خلاصه‌تر کنید." if language == "fa"
                                   else "The topic is too long or complex. Please simplify it.")
            elif "json" in error_str or "format" in error_str or "dictionary" in error_str:
                raise AnalysisError("مدل هوش مصنوعی نتوانست خروجی JSON معتبر تولید کند. لطفاً دوباره تلاش کنید." if language == "fa"
                                   else "The AI model failed to generate valid JSON. Please try again.")
            elif "rate limit" in error_str or "quota" in error_str:
                raise AnalysisError("محدودیت تعداد درخواست‌های API پر شده است. لطفاً ۱ دقیقه صبر کنید و دوباره تلاش کنید." if language == "fa"
                                   else "API rate limit reached. Please wait 1 minute and try again.")
            else:
                raise AnalysisError(f"خطا در تحلیل موضوع مدیریتی: {e}" if language == "fa"
                                   else f"Error analyzing management topic: {e}")