from typing import Dict, Any

from config.llm import llm


def company_research(state: Dict[str, Any]) -> Dict[str, Any]:
    company_name = state["company_name"]
    website = state["website"]

    prompt = f"""
You are a Company Research Agent.

Research and analyze the following company based only on the
information provided to you.

Company: {company_name}
Website: {website}

Provide a concise business profile covering:

1. What the company does
2. Main products or services
3. Target customers
4. Industry
5. Business model
6. Important business characteristics
7. Potential problems or needs that an AI automation company
   could potentially solve

Do not invent specific facts.
Clearly say when information is uncertain.
"""

    response = llm.invoke(prompt)

    return {
        "company_research": {
            "initial_profile": state["company_research"].get(
                "initial_profile", ""
            ),
            "detailed_research": response.content
        }
    }