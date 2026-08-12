from typing import Dict, Any


def aggregate_findings(state: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "aggregated_findings": {
            "company_research": state.get("company_research", {}),
            "tech_analysis": state.get("tech_analysis", {}),
            "financial_analysis": state.get("financial_analysis", {}),
            "market_research": state.get("market_research", {}),
            "competitor_analysis": state.get("competitor_analysis", {}),
            "automation_analysis": state.get("automation_analysis", {}),
        },
        "status": "research_complete",
    }