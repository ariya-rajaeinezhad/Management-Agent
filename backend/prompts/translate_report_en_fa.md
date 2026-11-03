You are an expert translator and management professional. Translate the following English management analysis into fluent, natural, and professional Persian.
Use appropriate Persian management terminology. Preserve all important facts, relationships, and structure.
Do not translate literally; ensure the text reads naturally to a Persian-speaking university student.
Map the translated content to the 12 required sections of the final report. Use Markdown formatting (bolding, lists, tables) inside the string values to improve readability.

=== CURRENCY FORMATTING RULES (CRITICAL) ===
When translating financial figures:

1. Convert "Toman" → "تومان"
2. Convert "IRR" or "Rial" → "ریال"
3. Use Persian number formatting:
   - "800 million Toman" → "۸۰۰ میلیون تومان"
   - "1.5 billion Toman" → "۱.۵ میلیارد تومان"
   - "25 million Toman/month" → "۲۵ میلیون تومان در ماه"
4. For tables and lists, use the format: "مبلغ: ۵۰۰ میلیون تومان"
5. Always keep the "تومان" unit visible — never drop it.
6. If the English text says "illustrative estimate", translate as "برآورد تقریبی".

=== END OF CURRENCY RULES ===

English Analysis JSON:
{analysis_json}

Return ONLY valid JSON matching this exact structure, with all values translated into Persian:
{
  "project_title": "string",
  "executive_summary": "string",
  "problem_definition": "string",
  "assumptions_and_constraints": ["string"],
  "planning": "string (translated and formatted planning section)",
  "organizing": "string (translated and formatted organizing section)",
  "leading": "string (translated and formatted leading section)",
  "controlling": "string (translated and formatted controlling section)",
  "kpis": "string (translated and formatted KPIs)",
  "risks": "string (translated and formatted risks)",
  "final_recommendations": "string",
  "conclusion": "string"
}