<div align="center">

# 🤖 AI Business Intelligence Agent

**An autonomous, multi-agent AI pipeline that researches any company and scores it as a prospect for AI automation — in seconds.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Orchestration-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain-ai.github.io/langgraph/)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com/)
[![Groq](https://img.shields.io/badge/Groq-LLaMA%203.1-F55036?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com/)
[![License](https://img.shields.io/badge/License-Private-red?style=for-the-badge)](LICENSE)

</div>

<div align="center">

### ⚡ Powered by Groq — 100% Free, No API Costs

> 🆓 This entire project runs on **Groq's free API tier** — no credit card, no billing, no hidden charges. Clone it, run it, and analyze companies at **absolutely zero cost**.

</div>

---

## 📖 Overview

The **AI Business Intelligence Agent** is a production-grade, agentic pipeline designed for AI automation consultancies and sales teams. Feed it just a **company name** and a **website URL** — it autonomously deploys a coordinated swarm of specialized AI research agents, synthesizes their findings, and delivers a structured, confidence-scored intelligence report with a clear `HIGH / MEDIUM / LOW` verdict.

No manual research. No guesswork. Just actionable intelligence.

> **Powered by:** LangGraph (state-machine orchestration) · LangChain · Groq (LLaMA 3.1 8B Instant)

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🧠 **Multi-Agent Architecture** | 9 specialized AI agents, each with a focused research mandate |
| ⚡ **Parallel Execution** | 5 research agents run concurrently after initial analysis |
| 🔒 **Structured Decision Output** | Pydantic-validated JSON — never hallucinated fields |
| 🛡️ **Built-in Rate Limiter** | Thread-safe, 3-second interval guard on all LLM calls |
| 📊 **Confidence Scoring** | Every decision comes with a 0–100 confidence percentage |
| 🔄 **LangGraph State Graph** | Full stateful orchestration with conditional routing |
| 🏗️ **Modular & Extensible** | Add new agents, tools, or export formats with minimal friction |

---

## 🧠 How It Works

Given only a company name and URL, the system executes a **sequential + parallel** research pipeline:

```
START
  │
  ▼
┌─────────────────────┐
│   initial_analysis  │  ← Creates a starter profile to seed all research agents
└─────────┬───────────┘
          │
  ┌───────┴────────────────────────────────────────────────────────┐
  │               PARALLEL RESEARCH (runs concurrently)             │
  ▼               ▼                  ▼             ▼               ▼
company_research  tech_analysis  financial_analysis  market_research  competitor_analysis
  │               │                  │             │               │
  └───────┬───────┴──────────────────┴─────────────┴───────────────┘
          │
          ▼
┌──────────────────────┐
│  automation_analysis │  ← Synthesizes all research → identifies top AI opportunity
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│       aggregate      │  ← Merges all findings into one structured state object
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    decision_agent    │  ← Issues HIGH / MEDIUM / LOW verdict + confidence score
└──────────┬───────────┘
           │  (conditional routing)
           ▼
┌──────────────────────┐
│     final_report     │  ← Formats and surfaces the structured output
└──────────┬───────────┘
           │
          END
```

### Agent Breakdown

| # | Agent | Module | Responsibility |
|---|-------|--------|----------------|
| 1 | **Initial Analysis** | `nodes/initial_analysis.py` | Generates a short starter profile (name, type, what they do) to bootstrap all downstream agents |
| 2a | **Company Research** | `nodes/company_research.py` | Full business profile — products, customers, model, key characteristics, and potential pain points |
| 2b | **Tech Analysis** | `nodes/tech_analysis.py` | Website & digital presence, inferred tech stack, automation readiness, technical weaknesses |
| 2c | **Financial Analysis** | `nodes/financial_analysis.py` | Business scale, revenue model, investment capacity, ROI potential, financial risks |
| 2d | **Market Research** | `nodes/market_research.py` | Industry dynamics, market trends, AI adoption landscape, demand signals |
| 2e | **Competitor Analysis** | `nodes/competitor_analysis.py` | Competitive landscape, differentiation gaps, tech advantage opportunities |
| 3 | **Automation Analysis** | `nodes/automation_analysis.py` | Synthesizes all parallel research → surfaces the single highest-value AI automation opportunity |
| 4 | **Aggregate** | `nodes/aggregate.py` | Merges all agent outputs into one clean, unified state dictionary |
| 5 | **Decision Agent** | `nodes/decision.py` | Final verdict: `HIGH_POTENTIAL`, `MEDIUM_POTENTIAL`, or `LOW_POTENTIAL` with confidence score, reasons, risks, evidence, and missing info |

> ⚡ **Agents 2a–2e run in parallel**, making the pipeline highly efficient even under a rate limiter.

---

## 🗂️ Project Structure

```
ai-biz-intel/
│
├── main.py                      # Entry point — set your target company here
│
├── graph/
│   └── workflow.py              # LangGraph graph: nodes, edges, conditional routing
│
├── nodes/
│   ├── initial_analysis.py      # Agent 1  — starter company profile
│   ├── company_research.py      # Agent 2a — business profile & pain points
│   ├── tech_analysis.py         # Agent 2b — technology & digital maturity
│   ├── financial_analysis.py    # Agent 2c — financial strength & ROI potential
│   ├── market_research.py       # Agent 2d — market & industry dynamics
│   ├── competitor_analysis.py   # Agent 2e — competitive landscape
│   ├── automation_analysis.py   # Agent 3  — top AI opportunity synthesis
│   ├── aggregate.py             # Agent 4  — findings aggregator
│   ├── decision.py              # Agent 5  — final HIGH/MEDIUM/LOW decision
│   └── final_report.py          # Formats and surfaces the structured final report
│
├── models/
│   └── decision.py              # Pydantic model — validates the Decision Agent's output
│
├── state/
│   └── state.py                 # LangGraph shared state schema (DealState TypedDict)
│
├── config/
│   └── llm.py                   # LLM config — Groq client + rate-limited wrapper
│
├── utils/
│   └── rate_limiter.py          # Thread-safe rate limiter (3s minimum between calls)
│
├── requirements.txt             # Python dependencies
├── .env                         # API keys (never committed)
└── .gitignore
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Language** | Python 3.10+ |
| **Agent Orchestration** | [LangGraph](https://langchain-ai.github.io/langgraph/) — `StateGraph` with `START` / `END` / conditional edges |
| **LLM Framework** | [LangChain](https://www.langchain.com/) — prompt composition and structured output |
| **LLM Provider** | [Groq](https://groq.com/) — `llama-3.1-8b-instant` (ultra-fast inference) |
| **Output Validation** | [Pydantic v2](https://docs.pydantic.dev/) — `DecisionResult` schema enforced on every run |
| **State Management** | Python `TypedDict` — `DealState` passed through the entire graph |
| **Rate Limiting** | Custom thread-safe `RateLimiter` — 3-second intervals, mutex-locked |
| **Config Management** | `python-dotenv` — `.env`-based API key injection |

---

## 🚀 Getting Started

### Prerequisites

- Python **3.10 or higher**
- A free [Groq API key](https://console.groq.com)

---

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd ai-biz-intel
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> Get your free API key at [https://console.groq.com](https://console.groq.com)

### 5. Set your target company

Open `main.py` and update the `initial_state` dictionary:

```python
initial_state = {
    "company_name": "Your Target Company",
    "website":      "https://www.yourcompany.com",

    # Leave the rest as-is — the agents populate these fields
    "company_research":    {},
    "tech_analysis":       {},
    "financial_analysis":  {},
    "market_research":     {},
    "competitor_analysis": {},
    "automation_analysis": {},
    "aggregated_findings": {},
    "decision":            {},
    "proposal":            "",
    "errors":              [],
    "status":              "starting"
}
```

### 6. Run

```bash
python main.py
```

---

## 📤 Sample Output

The following is a representative output for **Apollo Hospitals**:

```
===== GRAPH COMPLETED =====

===== FINAL REPORT =====

COMPANY:    Apollo Hospitals
WEBSITE:    https://www.apollohospitals.com

DECISION:   HIGH_POTENTIAL
CONFIDENCE: 87%

BEST OPPORTUNITY:
AI-powered voice agent for patient appointment scheduling and triage

REASONS:
- Large operational scale with high volume of repetitive patient interactions
- Significant investment capacity as a listed healthcare group
- Competitors are not yet known to deploy AI-agent-driven patient engagement at scale

RISKS:
- Healthcare regulation in India may slow or constrain AI deployment
- Patient trust and data privacy are critical concerns that must be addressed upfront
- Integration with legacy EHR/HIS systems may be technically complex

EVIDENCE:
- Apollo Hospitals is publicly listed with documented multi-city operations
- The company maintains patient-facing digital systems including app and portal
- The Indian private healthcare market is undergoing significant digital transformation

ASSUMPTIONS:
- High call-center volume is assumed from the scale of operations, not confirmed
- AI adoption budget is inferred from listed-company status, not from disclosed financials

MISSING INFORMATION:
- Current CRM / EHR systems in use
- Existing call-center volume and associated costs
- Internal IT roadmap and digital strategy priorities

===== END OF REPORT =====
```

---

## 🔌 Decision Output Schema

The `DecisionAgent` returns a Pydantic-validated object (`DecisionResult`) with the following guaranteed fields:

```python
class DecisionResult(BaseModel):
    decision:            str        # "HIGH_POTENTIAL" | "MEDIUM_POTENTIAL" | "LOW_POTENTIAL"
    confidence:          int        # 0–100 integer confidence score
    best_opportunity:    str        # The single highest-value AI automation opportunity
    reasons:             List[str]  # Why this verdict was reached
    risks:               List[str]  # Risks that could block or reduce the opportunity
    evidence:            List[str]  # Confirmed, factual supporting information
    assumptions:         List[str]  # Inferred (not confirmed) conclusions
    missing_information: List[str]  # Data gaps that would improve the decision quality
```

> All LLM output is validated by Pydantic before being written to state. Malformed responses raise a `ValidationError` — hallucinated or incomplete JSON is never silently accepted.

---

## 🛡️ Rate Limiter Design

The `RateLimiter` in `utils/rate_limiter.py` is a **thread-safe** utility that enforces a minimum 3-second gap between any two consecutive LLM calls. This is critical for preventing Groq API rate-limit errors when the parallel research agents all call the LLM in rapid succession.

```python
class RateLimiter:
    def __init__(self, min_interval=3):
        self.lock = threading.Lock()   # Mutex ensures only one thread proceeds at a time
        ...

    def wait(self):
        with self.lock:
            elapsed = time.time() - self.last_request
            if elapsed < self.min_interval:
                time.sleep(self.min_interval - elapsed)
            self.last_request = time.time()
```

Every LLM call — both `.invoke()` and `.with_structured_output().invoke()` — passes through this limiter automatically via the `RateLimitedLLM` wrapper in `config/llm.py`.

---

## 🔮 Roadmap

The following features are planned for future iterations:

- [ ] **`human_approval` node** — Human-in-the-loop gate inserted before the final decision; blocks execution until a human reviewer approves or rejects
- [ ] **`proposal` node** — Auto-generates a polished, client-ready AI automation proposal document based on the decision output
- [ ] **`tools/web_search.py`** — Live web search tool to ground agents in real-time, up-to-date company information
- [ ] **`tools/website_scraper.py`** — Scrape the target company's website for richer context (pricing, team, case studies)
- [ ] **`tools/company_data.py`** — Pull structured firmographic data from external APIs (e.g., Clearbit, Apollo.io)
- [ ] **`utils/retry.py`** — Exponential backoff retry logic for transient LLM API failures
- [ ] **Async execution** — Replace sequential LangGraph edges with true async parallel execution for maximum speed
- [ ] **JSON / PDF export** — Export the final report as a structured JSON file or a formatted PDF

---

## 🤝 Contributing

This project is currently **private**. Contributions are by invitation only.

If you have been granted access and would like to contribute:

1. Create a feature branch: `git checkout -b feature/your-feature-name`
2. Make your changes with clear, focused commits
3. Submit a pull request with a clear description of what was changed and why

---

## 📄 License

This project is **proprietary and private**. All rights reserved.

Unauthorized copying, distribution, or modification of this codebase — in whole or in part — is strictly prohibited.

---

<div align="center">

Built with ❤️ using **LangGraph** · **LangChain** · **Groq**

</div>
