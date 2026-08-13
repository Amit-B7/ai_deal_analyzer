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

    "decision": {},

    "proposal": "",

    "errors": [],
    "status": "starting"
}


graph = build_graph()

result = graph.invoke(initial_state)


print("\n===== GRAPH COMPLETED =====")

print("\n===== FINAL REPORT =====")

report = result["proposal"]

print(f"\nCOMPANY: {report['company']}")
print(f"WEBSITE: {report['website']}")

print(f"\nDECISION: {report['decision']}")
print(f"CONFIDENCE: {report['confidence']}%")

print(f"\nBEST OPPORTUNITY:")
print(report["best_opportunity"])

print("\nREASONS:")
for reason in report["reasons"]:
    print(f"- {reason}")

print("\nRISKS:")
for risk in report["risks"]:
    print(f"- {risk}")

print("\nEVIDENCE:")
for evidence in report["evidence"]:
    print(f"- {evidence}")

print("\nASSUMPTIONS:")
for assumption in report["assumptions"]:
    print(f"- {assumption}")

print("\nMISSING INFORMATION:")
for info in report["missing_information"]:
    print(f"- {info}")

print("\n===== END OF REPORT =====")