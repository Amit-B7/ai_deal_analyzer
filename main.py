from graph.workflow import build_graph


initial_state = {
    "company_name": "Apollo Hospitals",
    "website": "https://www.apollohospitals.com",

    "company_research": {},
    "tech_analysis": {},
    "financial_analysis": {},
    "market_research": {},
    "competitor_analysis": {},
    "automation_analysis": {},

    "aggregated_findings": {},

    "decision": "",
    "confidence": 0.0,
    "missing_information": [],

    "proposal": "",

    "errors": [],
    "status": "starting"
}

graph = build_graph()

result = graph.invoke(initial_state)

print("\n===== GRAPH COMPLETED =====")

print("\n===== COMPANY RESEARCH =====")
print(result["company_research"])

print("\n===== TECH ANALYSIS =====")
print(result["tech_analysis"])

print("\n===== FINANCIAL ANALYSIS =====")
print(result["financial_analysis"])

print("\n===== MARKET RESEARCH =====")
print(result["market_research"])

print("\n===== COMPETITOR ANALYSIS =====")
print(result["competitor_analysis"])

print("\n===== AUTOMATION ANALYSIS =====")
print(result["automation_analysis"])

print("\n===== FINAL DECISION =====")
print(result["decision"])