from typing import Dict, Any

from config.llm import llm
from models.decision import DecisionResult


def limit_text(text: str, max_chars: int = 2500) -> str:
    return text[:max_chars]


def decision_agent(state: Dict[str, Any]) -> Dict[str, Any]:

    company = limit_text(
        state["company_research"].get("analysis", "")
    )

    tech = limit_text(
        state["tech_analysis"].get("analysis", "")
    )

    financial = limit_text(
        state["financial_analysis"].get("analysis", "")
    )

    market = limit_text(
        state["market_research"].get("analysis", "")
    )

    competitors = limit_text(
        state["competitor_analysis"].get("analysis", "")
    )

    automation = limit_text(
        state["automation_analysis"].get("analysis", "")
    )

    prompt = f"""
You are the final Decision Agent in an AI business intelligence system.

Determine whether this company is a good prospect for an AI automation company.

COMPANY RESEARCH:
{company}

TECH ANALYSIS:
{tech}

FINANCIAL ANALYSIS:
{financial}

MARKET RESEARCH:
{market}

COMPETITOR ANALYSIS:
{competitors}

AUTOMATION ANALYSIS:
{automation}

Evaluate:

1. Overall business potential
2. Technology/automation opportunity
3. Financial/business potential
4. Market potential
5. Competitive situation
6. Best automation opportunity
7. Risks
8. Missing information

IMPORTANT:
- Do NOT invent statistics.
- Do NOT invent revenue.
- Do NOT invent ROI percentages.
- Clearly distinguish facts from assumptions.
- Base the decision only on the provided research.
- Put factual supporting information in evidence.
- Put uncertain conclusions in assumptions.

For the confidence score, calculate an integer from 0 to 100 based on:
- Amount of concrete evidence available (more verified facts = higher confidence)
- Consistency of signals across all 6 research areas
- Number of unknowns or missing data points (more gaps = lower confidence)
- Strength and clarity of the automation opportunity identified
Do NOT default to 80. The score must reflect the actual quality and completeness of the research for THIS specific company.

Return ONLY valid JSON.

Do NOT use markdown.
Do NOT use ```json.
Do NOT add explanations outside the JSON.

The JSON MUST contain exactly these fields:

{{
    "decision": "HIGH_POTENTIAL | MEDIUM_POTENTIAL | LOW_POTENTIAL",
    "confidence": <integer 0-100 calculated from the research above>,
    "best_opportunity": "<specific opportunity identified>",
    "reasons": ["<reason 1>", "<reason 2>"],
    "risks": ["<risk 1>", "<risk 2>"],
    "evidence": ["<fact 1>", "<fact 2>"],
    "assumptions": ["<assumption 1>"],
    "missing_information": ["<gap 1>"]
}}

The decision must be one of:
"HIGH_POTENTIAL"
"MEDIUM_POTENTIAL"
"LOW_POTENTIAL"

Confidence must be an integer from 0 to 100.
All list fields must contain strings.
"""

    # Normal Groq request — keeps our rate limiter
    response = llm.invoke(prompt)

    # Validate Groq's JSON using Pydantic
    decision = DecisionResult.model_validate_json(response.content)

    return {
        "decision": decision.model_dump(),
        "status": "decision_complete"
    }