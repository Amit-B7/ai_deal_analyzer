from typing import Dict, Any

from config.llm import llm


def financial_analysis(state: Dict[str, Any]) -> Dict[str, Any]:
    company_name = state["company_name"]
    website = state["website"]

    prompt = f"""
You are a Financial and Business Analysis Agent in an AI
business intelligence system.

Analyze the business strength and financial potential of:

Company: {company_name}
Website: {website}

Focus on:

1. Business scale
2. Revenue model
3. Potential ability to invest in technology
4. Growth indicators
5. Operational scale
6. Areas where automation could produce financial value
7. Potential ROI from AI automation
8. Financial/business risks
9. Important financial information that is unknown

Do NOT invent revenue, profit, valuation, employee numbers,
or other specific financial figures.

If reliable financial information is unavailable, explicitly
mark it as unknown.

The goal is to help a later Decision Agent determine whether
this company could be a valuable AI automation prospect.
"""

    response = llm.invoke(prompt)

    return {
        "financial_analysis": {
            "analysis": response.content
        }
    }