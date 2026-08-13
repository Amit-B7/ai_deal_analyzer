from typing import Dict, Any


def final_report(state: Dict[str, Any]) -> Dict[str, Any]:

    decision = state.get("decision", {})

    report = {
        "company": state.get("company_name", ""),
        "website": state.get("website", ""),
        "decision": decision.get("decision", ""),
        "confidence": decision.get("confidence", 0),
        "best_opportunity": decision.get("best_opportunity", ""),
        "reasons": decision.get("reasons", []),
        "risks": decision.get("risks", []),
        "evidence": decision.get("evidence", []),
        "assumptions": decision.get("assumptions", []),
        "missing_information": decision.get(
            "missing_information", []
        ),
    }

    return {
        "proposal": report,
        "status": "report_complete"
    }