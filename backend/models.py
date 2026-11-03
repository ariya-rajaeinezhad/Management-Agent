from pydantic import BaseModel, Field
from typing import List


# --- Internal English Analysis Models ---

class Risk(BaseModel):
    description: str = Field(description="Description of the risk")
    mitigation: str = Field(description="Mitigation strategy")


class KPI(BaseModel):
    name: str = Field(description="Name of the Key Performance Indicator")
    target: str = Field(description="Target value or goal")
    measurement_method: str = Field(description="How to measure this KPI")
    frequency: str = Field(description="How often to measure")


class PlanningSection(BaseModel):
    problem_definition: str
    objectives: List[str]
    smart_goals: List[str]
    activities_and_milestones: List[str]
    timeline_and_priorities: str
    resources_and_budget: str
    risks: List[Risk]
    assumptions_and_constraints: List[str]


class OrganizingSection(BaseModel):
    roles_and_responsibilities: List[str]
    resources: List[str]
    task_allocation: str
    organizational_structure: str
    dependencies: str
    coordination_methods: str
    raci_matrix: str


class LeadingSection(BaseModel):
    leadership_approach: str
    motivation_strategies: List[str]
    communication_plan: str
    delegation_and_decision_making: str
    conflict_resolution: str
    execution_procedures: List[str]
    challenges_and_solutions: List[str]


class ControllingSection(BaseModel):
    kpis: List[KPI]
    monitoring_frequency: str
    deviation_identification: str
    corrective_actions: str
    feedback_loops: str


class ManagementAnalysis(BaseModel):
    project_title: str
    executive_summary: str
    planning: PlanningSection
    organizing: OrganizingSection
    leading: LeadingSection
    controlling: ControllingSection


# --- Final Persian Report Model ---

class FinalReport(BaseModel):
    project_title: str
    executive_summary: str
    problem_definition: str
    assumptions_and_constraints: List[str]
    planning: str
    organizing: str
    leading: str
    controlling: str
    kpis: str
    risks: str
    final_recommendations: str = Field(default="با توجه به تحلیل فوق، توصیه می‌شود نظارت مستمر بر شاخص‌ها و انعطاف‌پذیری در اجرا حفظ شود.")
    conclusion: str = Field(default="این طرح چارچوب جامعی برای مدیریت موفق پروژه ارائه می‌دهد و با اجرای دقیق آن، احتمال موفقیت به طور قابل توجهی افزایش می‌یابد.")