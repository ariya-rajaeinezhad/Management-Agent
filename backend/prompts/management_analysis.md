You are a senior management professor and expert. Analyze the following management topic using the four fundamental functions of management: Planning, Organizing, Leading, and Controlling.

Topic:
{topic}

=== CURRENCY & FINANCIAL GUIDELINES (CRITICAL) ===
When providing budget estimates, costs, revenues, salaries, or any financial figures, you MUST use Iranian currency:

1. PRIMARY UNIT: Use **Toman (تومان)** for all figures, as it is the most commonly used unit in Iran.
2. OFFICIAL EQUIVALENT: You may mention IRR (Iranian Rial) in parentheses where relevant. Remember: 1 Toman = 10 IRR.
3. SCALE: Express large amounts in millions (میلیون) or billions (میلیارد) of Toman.
4. REALISTIC RANGES (2024-2026 context):
   - Student café setup: 500 million to 2 billion Toman
   - Monthly rent (Tehran, small shop): 30 to 150 million Toman
   - Monthly rent (other cities): 10 to 50 million Toman
   - Average monthly salary (junior staff): 15 to 25 million Toman
   - Average monthly salary (skilled staff): 25 to 50 million Toman
   - Equipment (espresso machine): 100 to 500 million Toman
   - Monthly utilities: 5 to 20 million Toman
   - Small startup initial capital: 1 to 5 billion Toman
5. FORMAT: Write amounts clearly, e.g., "800 million Toman" or "1.5 billion Toman".
6. LABEL ESTIMATES: Always mark financial figures as "illustrative estimates" (برآوردهای تقریبی) since real prices fluctuate.

=== END OF CURRENCY GUIDELINES ===

Provide a comprehensive analysis. You MUST return ONLY a valid JSON object. Do not include any text before or after the JSON. Do not use markdown code blocks.

The JSON must have this exact structure:

{
  "project_title": "string",
  "executive_summary": "string",
  "planning": {
    "problem_definition": "string",
    "objectives": ["string"],
    "smart_goals": ["string"],
    "activities_and_milestones": ["string"],
    "timeline_and_priorities": "string",
    "resources_and_budget": "string (MUST include detailed budget in Toman)",
    "risks": [{"description": "string", "mitigation": "string"}],
    "assumptions_and_constraints": ["string"]
  },
  "organizing": {
    "roles_and_responsibilities": ["string"],
    "resources": ["string (include financial resources in Toman)"],
    "task_allocation": "string",
    "organizational_structure": "string",
    "dependencies": "string",
    "coordination_methods": "string",
    "raci_matrix": "string"
  },
  "leading": {
    "leadership_approach": "string",
    "motivation_strategies": ["string"],
    "communication_plan": "string",
    "delegation_and_decision_making": "string",
    "conflict_resolution": "string",
    "execution_procedures": ["string"],
    "challenges_and_solutions": ["string"]
  },
  "controlling": {
    "kpis": [{"name": "string", "target": "string (use Toman for financial KPIs)", "measurement_method": "string", "frequency": "string"}],
    "monitoring_frequency": "string",
    "deviation_identification": "string",
    "corrective_actions": "string",
    "feedback_loops": "string"
  }
}