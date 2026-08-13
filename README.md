# 🤖 AI Business Intelligence Agent

An autonomous, multi-agent AI system that researches any company and determines whether it is a strong prospect for AI automation solutions — producing a structured, confidence-scored decision report.

---

## 📌 What It Does

Given just a **company name** and **website URL**, this system spins up a coordinated pipeline of specialized AI agents that each independently research a different dimension of the target company. Once all research is complete, a final **Decision Agent** synthesizes everything and returns a clear `HIGH_POTENTIAL / MEDIUM_POTENTIAL / LOW_POTENTIAL` verdict with supporting reasoning.

**Example input:**
```python
"company_name": "Apollo Hospitals"
"website":      "https://www.apollohospitals.com"
```

**Example output sections:**
- Company profile & business model
- Technology stack & digital maturity
- Financial strength & investment capacity
- Market trends & industry dynamics
- Competitive landscape
- AI automation opportunities (ranked by ROI & feasibility)
- Final decision with confidence score, risks, and missing info

---

## 🧠 How It Works — Agent Pipeline

The system is built with **LangGraph**, which orchestrates agents as nodes in a directed state graph.

```
START
  └─► initial_analysis
        ├─► company_research ──┐
        ├─► tech_analysis ─────┤
        ├─► financial_analysis ┼─► automation_analysis ─► aggregate ─► decision ─► END
        ├─► market_research ───┤
        └─► competitor_analysis┘
```

| Stage | Agent | What it does |
|-------|-------|--------------|
| 1 | **Initial Analysis** | Creates a short starter profile of the company to seed all other agents |
| 2 (parallel) | **Company Research** | Full business profile — products, customers, model, pain points |
| 2 (parallel) | **Tech Analysis** | Digital presence, tech stack, automation readiness |
| 2 (parallel) | **Financial Analysis** | Business scale, investment capacity, potential ROI |
| 2 (parallel) | **Market Research** | Industry trends, market demand, AI adoption landscape |
| 2 (parallel) | **Competitor Analysis** | Competitor landscape, weaknesses, differentiation opportunities |
| 3 | **Automation Analysis** | Synthesizes all parallel research → identifies the top AI automation opportunity |
| 4 | **Aggregate** | Merges all findings into a single structured object |
| 5 | **Decision Agent** | Issues a final `HIGH / MEDIUM / LOW` verdict with confidence score, reasons, risks |

> All 5 parallel research agents run **concurrently** after the initial analysis, making the pipeline fast and efficient.

---

## 🗂️ Project Structure

```
new proj/
│
├── main.py                    # Entry point — configure your company here and run
│
├── graph/
│   └── workflow.py            # LangGraph graph definition (nodes + edges)
│
├── nodes/
│   ├── initial_analysis.py    # Agent 1 — starter profile
│   ├── company_research.py    # Agent 2a — business profile
│   ├── tech_analysis.py       # Agent 2b — technology analysis
│   ├── financial_analysis.py  # Agent 2c — financial analysis
│   ├── market_research.py     # Agent 2d — market research
│   ├── competitor_analysis.py # Agent 2e — competitor analysis
│   ├── automation_analysis.py # Agent 3 — AI opportunity synthesis
│   ├── aggregate.py           # Agent 4 — findings aggregator
│   ├── decision.py            # Agent 5 — final decision maker
│   ├── human_approval.py      # (Planned) Human-in-the-loop approval node
│   └── proposal.py            # (Planned) Proposal generation node
│
├── state/
│   └── state.py               # Shared LangGraph state schema (DealState)
│
├── config/
│   └── llm.py                 # LLM config (Groq + rate limiter wrapper)
│
├── utils/
│   ├── rate_limiter.py        # Thread-safe rate limiter (3s between LLM calls)
│   └── retry.py               # (Planned) Retry logic for LLM failures
│
├── tools/
│   ├── web_search.py          # (Planned) Live web search tool
│   ├── website_scraper.py     # (Planned) Website scraper tool
│   └── company_data.py        # (Planned) Structured company data fetcher
│
├── requirements.txt           # Python dependencies
├── .env                       # API keys (not committed)
└── .gitignore                 # Ignored files
```

---

## ⚙️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.10+ |
| Agent Orchestration | LangGraph |
| LLM Framework | LangChain |
| LLM Provider | Groq (`llama-3.1-8b-instant`) |
| State Management | Python `TypedDict` via LangGraph `StateGraph` |
| Rate Limiting | Custom thread-safe `RateLimiter` (3s intervals) |
| Environment Config | `python-dotenv` |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd new-proj
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> Get a free API key at https://console.groq.com

### 5. Configure your target company

Open `main.py` and update the initial state:

```python
initial_state = {
    "company_name": "Your Target Company",
    "website": "https://www.yourcompany.com",
    ...
}
```

### 6. Run the agent

```bash
python main.py
```

---

## 📤 Sample Output

```
===== COMPANY RESEARCH =====
Apollo Hospitals is one of India's largest private healthcare groups...

===== TECH ANALYSIS =====
The company maintains a well-developed digital presence with patient portals...

===== FINANCIAL ANALYSIS =====
Apollo Hospitals is a publicly listed company with strong revenue indicators...

===== MARKET RESEARCH =====
The Indian private healthcare sector is experiencing rapid growth...

===== COMPETITOR ANALYSIS =====
Key competitors include Fortis Healthcare, Max Healthcare, and Manipal...

===== AUTOMATION ANALYSIS =====
Highest-potential opportunity: AI-powered patient appointment & triage agent...

===== STATUS =====
decision_complete

===== FINAL DECISION =====
DECISION: HIGH_POTENTIAL
CONFIDENCE: 87
BEST_OPPORTUNITY: AI voice agent for patient appointment scheduling and triage
REASONS:
- Large operational scale with high volume of repetitive patient interactions
- Significant investment capacity as a listed healthcare group
- Competitors are not yet known to have AI agent-driven patient engagement
RISKS:
- Healthcare regulation may slow AI deployment
- Patient trust and data privacy are critical concerns
MISSING_INFORMATION:
- Internal CRM/EHR systems in use
- Current call center volume and costs
```

---

## 🔮 Planned Features

- [ ] `human_approval.py` — Human-in-the-loop gate before the final decision
- [ ] `proposal.py` — Auto-generate a client-ready AI automation proposal
- [ ] `tools/web_search.py` — Live web search to ground agents in real-time data
- [ ] `tools/website_scraper.py` — Scrape the company website for deeper context
- [ ] `tools/company_data.py` — Pull structured data from external company APIs
- [ ] `utils/retry.py` — Graceful retry logic for LLM API failures
- [ ] Export results to PDF or JSON report

---

## 📄 License

This project is private. All rights reserved.
