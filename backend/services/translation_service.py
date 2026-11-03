from services.llm_service import BaseLLMService
from prompt_loader import load_prompt
from models import ManagementAnalysis, FinalReport
from exceptions import TranslationError
import json


class TranslationService:
    def __init__(self, llm_service: BaseLLMService):
        self.llm = llm_service

    def translate_fa_to_en(self, text: str) -> str:
        try:
            template = load_prompt("translate_fa_en.md")
            prompt = template.replace("{topic}", text)
            return self.llm.generate_text(prompt).strip()
        except Exception as e:
            raise TranslationError(f"Failed to translate to English: {e}")

    def translate_analysis_to_fa(self, analysis: ManagementAnalysis) -> FinalReport:
        try:
            template = load_prompt("translate_report_en_fa.md")
            analysis_dict = analysis.model_dump()
            analysis_json = json.dumps(analysis_dict, ensure_ascii=False, indent=2)
            
            prompt = template.replace("{analysis_json}", analysis_json)
            raw_json = self.llm.generate_json(prompt)
            
            # --- ROBUSTNESS FIXES: Fix LLM laziness before Pydantic validation ---
            
            # 1. If LLM returned a list for kpis, convert it to a formatted string
            if isinstance(raw_json.get("kpis"), list):
                raw_json["kpis"] = "\n".join([
                    f"- **{k.get('name', 'شاخص')}**: {k.get('target', '')} (اندازه‌گیری: {k.get('measurement_method', '')})" 
                    for k in raw_json["kpis"]
                ])
            
            # 2. If LLM returned a list for risks, convert it to a formatted string
            if isinstance(raw_json.get("risks"), list):
                raw_json["risks"] = "\n".join([
                    f"- **{r.get('description', 'ریسک')}**: {r.get('mitigation', '')}" 
                    for r in raw_json["risks"]
                ])
            
            # 3. Ensure required fields exist (fallback to defaults if LLM omitted them)
            raw_json.setdefault("final_recommendations", "با توجه به تحلیل فوق، توصیه می‌شود نظارت مستمر بر شاخص‌ها و انعطاف‌پذیری در اجرا حفظ شود.")
            raw_json.setdefault("conclusion", "این طرح چارچوب جامعی برای مدیریت موفق پروژه ارائه می‌دهد و با اجرای دقیق آن، احتمال موفقیت به طور قابل توجهی افزایش می‌یابد.")
            
            # Now validate with Pydantic
            return FinalReport.model_validate(raw_json)
            
        except Exception as e:
            error_str = str(e).lower()
            if "context" in error_str or "length" in error_str:
                raise TranslationError("تحلیل بسیار طولانی است. لطفاً موضوع ساده‌تری را امتحان کنید.")
            else:
                raise TranslationError(f"خطا در ترجمه گزارش به فارسی: {e}")