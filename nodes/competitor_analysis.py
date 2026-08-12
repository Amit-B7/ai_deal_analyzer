from typing import Dict, Any

from config.llm import llm


def competitor_analysis(state: Dict[str, Any]) -> Dict[str, Any]:
    company_name = state["company_name"]
    website = state["website"]

    prompt = f"""
You are a Competitor Analysis Agent in an AI business intelligence system.

Analyze the competitive position of this company:

Company: {company_name}
Website: {website}

Focus on:

1. Likely major competitors
2. How competitors may differ from this company
3. Competitive strengths of the company
4. Possible competitive weaknesses
5. Areas where competitors may have a technology advantage
6. Potential opportunities to use AI or automation for competitive advantage
7. Competitive risks
8. Important information that is unknown

Do NOT invent specific competitor statistics, revenue,
market share, rankings, or other unsupported numbers.

If you are uncertain about a competitor or fact, clearly
mark it as uncertain.

The goal is to provide useful information for a later
Decision Agent that will determine whether this company
is a strong AI automation prospect.
"""

    response = llm.invoke(prompt)

    return {
        "competitor_analysis": {
            "analysis": response.content
        }
    }