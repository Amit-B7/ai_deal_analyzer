from typing import Dict, Any

from config.llm import llm


def initial_analysis(state: Dict[str, Any]) -> Dict[str, Any]:
    company_name = state["company_name"]
    website = state["website"]

    prompt = f"""
You are the initial analysis agent in an AI business intelligence system.

Analyze the following company information and prepare a short starting profile
for other research agents.

Company name: {company_name}
Website: {website}

Return:
1. Company name
2. Website
3. What the company appears to do
4. What type of business it is

Do not make a final business decision.
Do not invent information that is not reasonably known.
"""

    response = llm.invoke(prompt)

    return {
        "company_research": {
            "initial_profile": response.content
        },
        "status": "researching"
    }