from typing import Dict, Any

from config.llm import llm


def automation_analysis(state: Dict[str, Any]) -> Dict[str, Any]:
    company_name = state["company_name"]

    company_research = state["company_research"].get(
        "detailed_research", ""
    )

    tech_analysis = state["tech_analysis"].get(
        "analysis", ""
    )

    financial_analysis = state["financial_analysis"].get(
        "analysis", ""
    )

    market_research = state["market_research"].get(
        "analysis", ""
    )

    competitor_analysis = state["competitor_analysis"].get(
        "analysis", ""
    )

    prompt = f"""
You are an AI Automation Opportunity Agent.

Your job is to determine where AI automation could create
real business value for this company.

Company: {company_name}

COMPANY RESEARCH:
{company_research}

TECH ANALYSIS:
{tech_analysis}

FINANCIAL ANALYSIS:
{financial_analysis}

MARKET RESEARCH:
{market_research}

COMPETITOR ANALYSIS:
{competitor_analysis}

Analyze all the information and identify potential
AI automation opportunities.

For each important opportunity consider:

1. Problem
2. Proposed AI automation
3. Who would use it
4. Expected business benefit
5. Technical feasibility
6. Potential ROI
7. Implementation difficulty
8. Priority

Pay special attention to opportunities involving:

- AI agents
- AI calling/voice agents
- Customer support
- Lead qualification
- Sales automation
- Data processing
- Workflow automation
- Internal business operations

Do not invent specific company processes that are not supported
by the available information.

Clearly distinguish between confirmed information and assumptions.

At the end, identify the SINGLE highest-potential
AI automation opportunity.
"""

    response = llm.invoke(prompt)

    return {
        "automation_analysis": {
            "analysis": response.content
        }
    }