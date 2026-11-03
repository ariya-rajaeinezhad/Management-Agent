from models import ManagementAnalysis, FinalReport, Risk, KPI


def test_management_analysis_validation():
    data = {
        "project_title": "Test Project",
        "executive_summary": "Summary",
        "planning": {
            "problem_definition": "Def",
            "objectives": ["obj1"],
            "smart_goals": ["goal1"],
            "activities_and_milestones": ["act1"],
            "timeline_and_priorities": "time",
            "resources_and_budget": "res",
            "risks": [{"description": "risk", "mitigation": "mit"}],
            "assumptions_and_constraints": ["ass1"],
        },
        "organizing": {
            "roles_and_responsibilities": ["role1"],
            "resources": ["res1"],
            "task_allocation": "task",
            "organizational_structure": "struct",
            "dependencies": "dep",
            "coordination_methods": "coord",
            "raci_matrix": "raci",
        },
        "leading": {
            "leadership_approach": "lead",
            "motivation_strategies": ["mot1"],
            "communication_plan": "comm",
            "delegation_and_decision_making": "del",
            "conflict_resolution": "conf",
            "execution_procedures": ["proc1"],
            "challenges_and_solutions": ["chal1"],
        },
        "controlling": {
            "kpis": [{"name": "kpi1", "target": "t", "measurement_method": "m", "frequency": "f"}],
            "monitoring_frequency": "freq",
            "deviation_identification": "dev",
            "corrective_actions": "corr",
            "feedback_loops": "feed",
        },
    }
    analysis = ManagementAnalysis.model_validate(data)
    assert analysis.project_title == "Test Project"
    assert isinstance(analysis.planning.risks[0], Risk)
    assert isinstance(analysis.controlling.kpis[0], KPI)


def test_final_report_validation():
    data = {
        "project_title": "Test",
        "executive_summary": "Summary",
        "problem_definition": "Def",
        "assumptions_and_constraints": ["ass1"],
        "planning": "plan",
        "organizing": "org",
        "leading": "lead",
        "controlling": "cont",
        "kpis": "kpi",
        "risks": "risk",
        "final_recommendations": "rec",
        "conclusion": "conc",
    }
    report = FinalReport.model_validate(data)
    assert report.project_title == "Test"
    assert len(report.assumptions_and_constraints) == 1