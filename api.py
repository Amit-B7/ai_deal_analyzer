from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from graph.workflow import build_graph


app = FastAPI(
    title="AI Deal Analyzer API",
    description="API for analyzing companies using a LangGraph multi-agent system",
    version="1.0.0"
)


# Allow requests from any origin (works for both localhost and Render)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CompanyRequest(BaseModel):
    company_name: str
    website: str


@app.get("/")
def root():
    return {
        "message": "AI Deal Analyzer API is running"
    }


@app.post("/analyze")
def analyze_company(request: CompanyRequest):

    try:
        print("\n===== ANALYSIS STARTED =====")
        print(f"Company: {request.company_name}")
        print(f"Website: {request.website}")

        initial_state = {
            "company_name": request.company_name,
            "website": request.website,

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

        print("Building graph...")

        graph = build_graph()

        print("Running LangGraph...")

        result = graph.invoke(initial_state)

        print("LangGraph completed.")

        print("===== ANALYSIS COMPLETED =====\n")

        return result

    except Exception as e:

        print("\n===== ANALYZE ERROR =====")
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {str(e)}")
        print("============================\n")

        raise HTTPException(
            status_code=500,
            detail=f"{type(e).__name__}: {str(e)}"
        )