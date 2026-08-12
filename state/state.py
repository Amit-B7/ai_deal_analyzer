from typing import TypedDict, List, Dict, Any


class DealState(TypedDict):
    # Basic company information
    company_name: str
    website: str

    # Research results
    company_research: Dict[str, Any]
    tech_analysis: Dict[str, Any]
    financial_analysis: Dict[str, Any]
    market_research: Dict[str, Any]
    competitor_analysis: Dict[str, Any]
    automation_analysis: Dict[str, Any]

    # Combined research
    aggregated_findings: Dict[str, Any]

    # Decision information
    decision: str
    confidence: float
    missing_information: List[str]

    # Proposal
    proposal: str

    # System information
    errors: List[str]
    status: str