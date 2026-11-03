"""
Report Service - Orchestrates the full report generation pipeline
با پشتیبانی از تولید گزارش به فارسی و انگلیسی
"""
import uuid
from models import ManagementAnalysis, FinalReport
from services.translation_service import TranslationService
from services.management_service import ManagementService
from services.llm_service import BaseLLMService
import database


class ReportService:
    """
    Main service that coordinates the entire report generation process.
    Handles both Persian and English output based on user preference.
    """
    
    def __init__(self, llm_service: BaseLLMService):
        self.translation_service = TranslationService(llm_service)
        self.management_service = ManagementService(llm_service)

    def generate_report(self, topic: str, language: str = "fa") -> tuple[FinalReport, str, str, str]:
        """
        Executes the full pipeline with language support.
        """
        # Step 1: Translate to English if input is Persian
        if language == "fa":
            topic_en = self.translation_service.translate_fa_to_en(topic)
            topic_fa = topic
        else:
            topic_en = topic
            topic_fa = topic
        
        # Step 2: Analyze with language-specific prompt
        analysis = self.management_service.analyze(topic_en, language=language)
        analysis_json_str = analysis.model_dump_json(indent=2)
        
        # Step 3: Generate final report in requested language
        if language == "fa":
            final_report = self.translation_service.translate_analysis_to_fa(analysis)
        else:
            final_report = self._generate_english_report(analysis)

        # Step 4: Save to database
        report_id = str(uuid.uuid4())
        database.save_report(
            report_id=report_id,
            topic_fa=topic_fa,
            topic_en=topic_en,
            analysis_en=analysis.model_dump(),
            final_report=final_report.model_dump(),
        )

        return final_report, topic_en, analysis_json_str, report_id
    def _generate_english_report(self, analysis: ManagementAnalysis) -> FinalReport:
        """
        Convert English analysis to FinalReport format without translation.
        Converts Iranian Toman to USD for English reports.
        """
        return FinalReport(
            project_title=analysis.project_title,
            executive_summary=analysis.executive_summary,
            problem_definition=analysis.planning.problem_definition,
            assumptions_and_constraints=analysis.planning.assumptions_and_constraints,
            planning=self._format_planning_en(analysis.planning),
            organizing=self._format_organizing_en(analysis.organizing),
            leading=self._format_leading_en(analysis.leading),
            controlling=self._format_controlling_en(analysis.controlling),
            kpis=self._format_kpis_en(analysis.controlling.kpis),
            risks=self._format_risks_en(analysis.planning.risks),
            final_recommendations="Based on the analysis above, continuous monitoring of KPIs and flexibility in execution is recommended.",
            conclusion="This plan provides a comprehensive framework for successful project management. Regular review and adaptation to changing conditions will ensure long-term success."
        )
    
    def _convert_toman_to_usd(self, text: str) -> str:
        """
        Convert Iranian Toman amounts to USD in text.
        Assumes 1 USD ≈ 50,000 Toman (approximate rate).
        """
        import re
        
        # Pattern to match amounts like "800 million Toman" or "1.5 billion Toman"
        def replace_amount(match):
            amount_str = match.group(1)
            unit = match.group(2).lower()
            
            # Parse the amount
            try:
                if 'billion' in unit:
                    toman = float(amount_str.replace(',', '')) * 1_000_000_000
                elif 'million' in unit:
                    toman = float(amount_str.replace(',', '')) * 1_000_000
                else:
                    toman = float(amount_str.replace(',', ''))
                
                # Convert to USD (approximate rate: 50,000 Toman = 1 USD)
                usd = toman / 50_000
                
                # Format nicely
                if usd >= 1_000_000:
                    return f"${usd/1_000_000:.1f}M"
                elif usd >= 1_000:
                    return f"${usd/1_000:.0f}K"
                else:
                    return f"${usd:.0f}"
            except:
                return match.group(0)  # Return original if parsing fails
        
        # Replace patterns like "800 million Toman" or "1.5 billion Toman"
        text = re.sub(r'(\d+(?:\.\d+)?)\s*(billion|million)?\s*toman', replace_amount, text, flags=re.IGNORECASE)
        
        return text
    
    def _format_planning_en(self, planning) -> str:
        """Format planning section into readable Markdown with USD conversion."""
        parts = [
            f"**Objectives:**\n" + "\n".join(f"- {obj}" for obj in planning.objectives),
            f"\n**SMART Goals:**\n" + "\n".join(f"- {g}" for g in planning.smart_goals),
            f"\n**Activities & Milestones:**\n" + "\n".join(f"- {a}" for a in planning.activities_and_milestones),
            f"\n**Timeline & Priorities:** {planning.timeline_and_priorities}",
            f"\n**Resources & Budget:** {self._convert_toman_to_usd(planning.resources_and_budget)}",
        ]
        return "\n".join(parts)
    
    def _format_organizing_en(self, organizing) -> str:
        """Format organizing section into readable Markdown with USD conversion."""
        parts = [
            f"**Roles & Responsibilities:**\n" + "\n".join(f"- {r}" for r in organizing.roles_and_responsibilities),
            f"\n**Resources:**\n" + "\n".join(f"- {self._convert_toman_to_usd(r)}" for r in organizing.resources),
            f"\n**Task Allocation:** {organizing.task_allocation}",
            f"\n**Organizational Structure:** {organizing.organizational_structure}",
            f"\n**Dependencies:** {organizing.dependencies}",
            f"\n**Coordination Methods:** {organizing.coordination_methods}",
            f"\n**RACI Matrix:** {organizing.raci_matrix}",
        ]
        return "\n".join(parts)
    
    def _format_leading_en(self, leading) -> str:
        """Format leading section into readable Markdown."""
        parts = [
            f"**Leadership Approach:** {leading.leadership_approach}",
            f"\n\n**Motivation Strategies:**\n" + "\n".join(f"- {s}" for s in leading.motivation_strategies),
            f"\n\n**Communication Plan:** {leading.communication_plan}",
            f"\n\n**Delegation & Decision Making:** {leading.delegation_and_decision_making}",
            f"\n\n**Conflict Resolution:** {leading.conflict_resolution}",
            f"\n\n**Execution Procedures:**\n" + "\n".join(f"- {p}" for p in leading.execution_procedures),
            f"\n\n**Challenges & Solutions:**\n" + "\n".join(f"- {c}" for c in leading.challenges_and_solutions),
        ]
        return "\n".join(parts)
    
    def _format_controlling_en(self, controlling) -> str:
        """Format controlling section into readable Markdown."""
        return (
            f"**Monitoring Frequency:** {controlling.monitoring_frequency}\n\n"
            f"**Deviation Identification:** {controlling.deviation_identification}\n\n"
            f"**Corrective Actions:** {controlling.corrective_actions}\n\n"
            f"**Feedback Loops:** {controlling.feedback_loops}"
        )
    
    def _format_kpis_en(self, kpis) -> str:
        """Format KPIs into readable Markdown list with USD conversion."""
        if not kpis:
            return "No KPIs defined."
        return "\n".join(
            f"- **{k.name}**: Target {self._convert_toman_to_usd(k.target)} (Measurement: {k.measurement_method}, Frequency: {k.frequency})"
            for k in kpis
        )
    
    def _format_risks_en(self, risks) -> str:
        """Format risks into readable Markdown list."""
        if not risks:
            return "No risks identified."
        return "\n".join(
            f"- **{r.description}**\n  - Mitigation: {r.mitigation}"
            for r in risks
        )