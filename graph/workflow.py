from langgraph.graph import StateGraph, START, END

from state.state import DealState

from nodes.initial_analysis import initial_analysis
from nodes.company_research import company_research
from nodes.tech_analysis import tech_analysis
from nodes.financial_analysis import financial_analysis
from nodes.market_research import market_research
from nodes.competitor_analysis import competitor_analysis
from nodes.automation_analysis import automation_analysis
from nodes.aggregate import aggregate_findings
from nodes.decision import decision_agent
from nodes.final_report import final_report

def decision_router(state: DealState):

    decision = state["decision"]["decision"]

    if decision == "HIGH_POTENTIAL":
        return "high"

    elif decision == "MEDIUM_POTENTIAL":
        return "medium"

    else:
        return "low"


def build_graph():

    graph = StateGraph(DealState)

    # Add nodes
    graph.add_node("initial_analysis", initial_analysis)
    graph.add_node("company_research", company_research)
    graph.add_node("tech_analysis", tech_analysis)
    graph.add_node("financial_analysis", financial_analysis)
    graph.add_node("market_research", market_research)
    graph.add_node("competitor_analysis", competitor_analysis)
    graph.add_node("automation_analysis", automation_analysis)
    graph.add_node("aggregate", aggregate_findings)
    graph.add_node("decision", decision_agent)
    graph.add_node("final_report", final_report)
    
    # Initial node
    graph.add_edge(START, "initial_analysis")

    # Parallel research
    graph.add_edge("initial_analysis", "company_research")
    graph.add_edge("initial_analysis", "tech_analysis")
    graph.add_edge("initial_analysis", "financial_analysis")
    graph.add_edge("initial_analysis", "market_research")
    graph.add_edge("initial_analysis", "competitor_analysis")

    # Automation analysis waits for all research
    graph.add_edge("company_research", "automation_analysis")
    graph.add_edge("tech_analysis", "automation_analysis")
    graph.add_edge("financial_analysis", "automation_analysis")
    graph.add_edge("market_research", "automation_analysis")
    graph.add_edge("competitor_analysis", "automation_analysis")

    # Aggregate
    graph.add_edge("automation_analysis", "aggregate")

    # Decision
    graph.add_edge("aggregate", "decision")

    # Conditional routing
    graph.add_conditional_edges(
    "decision",
    decision_router,
    {
        "high": "final_report",
        "medium": "final_report",
        "low": "final_report"
        }
    )

    graph.add_edge("final_report", END)

    return graph.compile()