from unittest.mock import MagicMock
from services.report_service import ReportService


def test_pipeline_execution_order():
    mock_llm = MagicMock()

    # Mock translation Fa->En (generate_text)
    mock_llm.generate_text.return_value = "Planning for a student cafe"

    # Mock management analysis and final translation (generate_json)
    mock_llm.generate_json.side_effect = [
        {  # Management Analysis
            "project_title": "Student Cafe",
            "executive_summary": "Sum",
            "planning": {
                "problem_definition": "Def",
                "objectives": [],
                "smart_goals": [],
                "activities_and_milestones": [],
                "timeline_and_priorities": "",
                "resources_and_budget": "",
                "risks": [],
                "assumptions_and_constraints": [],
            },
            "organizing": {
                "roles_and_responsibilities": [],
                "resources": [],
                "task_allocation": "",
                "organizational_structure": "",
                "dependencies": "",
                "coordination_methods": "",
                "raci_matrix": "",
            },
            "leading": {
                "leadership_approach": "",
                "motivation_strategies": [],
                "communication_plan": "",
                "delegation_and_decision_making": "",
                "conflict_resolution": "",
                "execution_procedures": [],
                "challenges_and_solutions": [],
            },
            "controlling": {
                "kpis": [],
                "monitoring_frequency": "",
                "deviation_identification": "",
                "corrective_actions": "",
                "feedback_loops": "",
            },
        },
        {  # Final Report Fa
            "project_title": "کافه دانشجویی",
            "executive_summary": "خلاصه",
            "problem_definition": "تعریف",
            "assumptions_and_constraints": [],
            "planning": "برنامه",
            "organizing": "سازمان",
            "leading": "هدایت",
            "controlling": "کنترل",
            "kpis": "شاخص",
            "risks": "ریسک",
            "final_recommendations": "پیشنهاد",
            "conclusion": "نتیجه",
        },
    ]

    service = ReportService(mock_llm)
    final_report, topic_en, analysis_en = service.generate_report("کافه دانشجویی")

    assert final_report.project_title == "کافه دانشجویی"
    assert topic_en == "Planning for a student cafe"

    # Verify call order
    calls = mock_llm.method_calls
    assert calls[0].args[0] == "generate_text"  # Fa->En
    assert calls[1].args[0] == "generate_json"  # Analysis
    assert calls[2].args[0] == "generate_json"  # En->Fa Report