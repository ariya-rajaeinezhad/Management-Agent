You are a senior management professor and expert. Analyze the following management topic using the four fundamental functions of management: Planning, Organizing, Leading, and Controlling.

Topic:
{topic}

=== CURRENCY & FINANCIAL GUIDELINES (CRITICAL) ===
When providing budget estimates, costs, revenues, salaries, or any financial figures, you MUST use USD:

1. PRIMARY UNIT: Use **USD ($)** for all figures.
2. SCALE: Express large amounts in thousands (K), millions (M), or billions (B).
3. REALISTIC RANGES:
   - Student café setup: $16,000 to $40,000
   - Monthly rent (small shop): $600 to $3,000
   - Average monthly salary (junior staff): $300 to $500
   - Average monthly salary (skilled staff): $500 to $1,000
   - Equipment (espresso machine): $2,000 to $10,000
   - Monthly utilities: $100 to $400
   - Small startup initial capital: $20,000 to $100,000
4. FORMAT: Write amounts clearly, e.g., "$16K" or "$1.5M".
5. LABEL ESTIMATES: Always mark financial figures as "illustrative estimates".

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
    "resources_and_budget": "string (MUST include detailed budget in USD)",
    "risks": [{"description": "string", "mitigation": "string"}],
    "assumptions_and_constraints": ["string"]
  },
  "organizing": {
    "roles_and_responsibilities": ["string"],
    "resources": ["string (include financial resources in USD)"],
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
    "kpis": [{"name": "string", "target": "string (use USD for financial KPIs)", "measurement_method": "string", "frequency": "string"}],
    "monitoring_frequency": "string",
    "deviation_identification": "string",
    "corrective_actions": "string",
    "feedback_loops": "string"
  }
}