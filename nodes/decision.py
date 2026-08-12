from typing import Dict, Any

from config.llm import llm


def decision_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    findings = state["aggregated_findings"]

    prompt = f"""
You are the final Decision Agent in an AI business intelligence system.

Your job is to decide whether this company is a good prospect
for an AI automation company.

Here is the complete research:

{findings}

Evaluate:

1. Overall business potential
2. Technology/automation opportunity
3. Financial/business potential
4. Market potential
5. Competitive situation
6. Most valuable automation opportunity
7. Potential ROI
8. Main risks
9. Missing information

Return your answer in EXACTLY this format:

DECISION: HIGH_POTENTIAL / MEDIUM_POTENTIAL / LOW_POTENTIAL
CONFIDENCE: number from 0 to 100
BEST_OPPORTUNITY: one sentence
REASONS:
- reason 1
- reason 2
- reason 3
RISKS:
- risk 1
- risk 2
MISSING_INFORMATION:
- information 1
- information 2

Do not invent facts.
Base the decision only on the provided research.
"""

    response = llm.invoke(prompt)

    return {
        "decision": response.content,
        "status": "decision_complete"
    }