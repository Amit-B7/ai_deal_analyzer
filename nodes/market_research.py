from typing import Dict, Any

from config.llm import llm


def market_research(state: Dict[str, Any]) -> Dict[str, Any]:
    company_name = state["company_name"]
    website = state["website"]

    prompt = f"""
You are a Market Research Agent in an AI business intelligence system.

Analyze the market and industry surrounding this company:

Company: {company_name}
Website: {website}

Focus on:

1. Industry and market characteristics
2. Current market trends
3. Market demand
4. Major opportunities
5. Major challenges
6. Customer behavior or expectations
7. Competitive pressure
8. How AI and automation could affect this industry
9. Whether this market appears suitable for AI automation solutions

Do not invent specific market statistics or numbers.

If information is uncertain or unavailable, clearly state that.

The goal is to provide useful market-level information
for a later Decision Agent.
"""

    response = llm.invoke(prompt)

    return {
        "market_research": {
            "analysis": response.content
        }
    }