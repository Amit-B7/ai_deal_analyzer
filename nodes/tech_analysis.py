from typing import Dict, Any

from config.llm import llm


def tech_analysis(state: Dict[str, Any]) -> Dict[str, Any]:
    company_name = state["company_name"]
    website = state["website"]

    prompt = f"""
You are a Technology Analysis Agent in an AI business intelligence system.

Analyze the technology and digital presence of this company:

Company: {company_name}
Website: {website}

Focus specifically on:

1. Website and digital presence
2. Customer-facing digital systems
3. Possible software/technology infrastructure
4. Digital processes that may be automated
5. Possible use of AI or automation
6. Potential technical weaknesses or inefficiencies
7. AI automation opportunities for an AI automation company

Do not invent specific technologies or systems.
If something cannot be determined from the available information,
clearly mark it as unknown or uncertain.

Keep the analysis concise and useful for a later Decision Agent.
"""

    response = llm.invoke(prompt)

    return {
        "tech_analysis": {
            "analysis": response.content
        }
    }