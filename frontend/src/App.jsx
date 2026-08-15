import { useState, useEffect, useRef } from "react";
import "./styles.css";

function App() {
  const [companyName, setCompanyName] = useState("");
  const [website, setWebsite] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [activeSection, setActiveSection] = useState("section-input");
  const contentRef = useRef(null);

  // Scroll to a section inside the content pane
  const scrollToSection = (id) => {
    const el = document.getElementById(id);
    if (el && contentRef.current) {
      contentRef.current.scrollTo({
        top: el.offsetTop - 24,
        behavior: "smooth",
      });
    }
  };

  // Track which section is in view
  useEffect(() => {
    const sections = [
      "section-input",
      "section-assessment",
      "section-opportunity",
      "section-intelligence",
    ];
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            setActiveSection(entry.target.id);
          }
        });
      },
      {
        root: contentRef.current,
        threshold: 0.3,
      }
    );
    sections.forEach((id) => {
      const el = document.getElementById(id);
      if (el) observer.observe(el);
    });
    return () => observer.disconnect();
  }, [result]);

  const analyzeCompany = async () => {
    if (!companyName || !website) return;

    setLoading(true);
    setResult(null);
    setError("");

    try {
      const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";
      const response = await fetch(`${API_URL}/analyze`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          company_name: companyName,
          website: website,
        }),
      });

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(errorText || "Analysis failed");
      }

      const data = await response.json();

      setResult(data);
    } catch (err) {
      console.error(err);
      setError(
        err.message || "Could not analyze the company."
      );
    } finally {
      setLoading(false);
    }
  };

  const listItems = (items) => {
    if (!items) return [];

    if (Array.isArray(items)) {
      return items;
    }

    if (typeof items === "string") {
      return [items];
    }

    return [];
  };

  const renderList = (items) => {
    const values = listItems(items);

    if (!values.length) {
      return (
        <div className="empty-state">
          NO DATA AVAILABLE
        </div>
      );
    }

    return (
      <div className="intel-list">
        {values.map((item, index) => (
          <div className="intel-item" key={index}>
            <span className="item-number">
              {String(index + 1).padStart(2, "0")}
            </span>

            <p>{String(item)}</p>
          </div>
        ))}
      </div>
    );
  };

  // The backend wraps all report fields inside result.proposal
  const report = result?.proposal || result || null;

  const confidence =
    typeof report?.confidence === "number"
      ? report.confidence
      : Number(report?.confidence || 0);

  const decision =
    typeof report?.decision === "string"
      ? report.decision
      : "PENDING";

  return (
    <div className="console">

      {/* =========================================
          TOP BAR
      ========================================= */}

      <header className="topbar">

        <div className="brand">
          <div className="brand-mark">
            DA
          </div>

          <div>
            <div className="brand-name">
              DEAL ANALYZER
            </div>

            <div className="brand-sub">
              INTELLIGENCE SYSTEM
            </div>
          </div>
        </div>

        <div className="system-status">
          <span className="status-dot"></span>
          SYSTEM ONLINE
        </div>

      </header>


      {/* =========================================
          MAIN LAYOUT
      ========================================= */}

      <main className="workspace">



        {/* =========================================
            CONTENT
        ========================================= */}

        <section className="content" ref={contentRef}>

          {/* PAGE HEADER */}

          <div id="section-input" className="page-heading">

            <div>
              <div className="eyebrow">
                DEAL INTELLIGENCE / 001
              </div>

              <h1>
                Company
                <br />
                Assessment
              </h1>
            </div>

            <div className="heading-meta">
              <span>MODE</span>
              <strong>MULTI-AGENT</strong>

              <span>STATUS</span>
              <strong>
                {loading ? "PROCESSING" : "READY"}
              </strong>
            </div>

          </div>


          {/* =========================================
              INPUT TERMINAL
          ========================================= */}

          <section className="input-panel">

            <div className="panel-header">

              <span>
                ANALYSIS TARGET
              </span>

              <span className="panel-id">
                INPUT / 001
              </span>

            </div>

            <div className="input-grid">

              <div className="field">

                <label>
                  COMPANY NAME
                </label>

                <input
                  type="text"
                  value={companyName}
                  placeholder="e.g. Apollo Hospitals"
                  onChange={(e) =>
                    setCompanyName(e.target.value)
                  }
                />

              </div>


              <div className="field">

                <label>
                  COMPANY WEBSITE
                </label>

                <input
                  type="text"
                  value={website}
                  placeholder="https://example.com"
                  onChange={(e) =>
                    setWebsite(e.target.value)
                  }
                />

              </div>


              <button
                className="analyze-button"
                onClick={analyzeCompany}
                disabled={
                  loading ||
                  !companyName ||
                  !website
                }
              >
                <span>
                  {loading
                    ? "PROCESSING"
                    : "RUN ANALYSIS"}
                </span>

                <span className="button-arrow">
                  →
                </span>
              </button>

            </div>

          </section>


          {/* =========================================
              LOADING
          ========================================= */}

          {loading && (

            <section className="processing-panel">

              <div className="processing-top">

                <span className="processing-label">
                  ANALYSIS IN PROGRESS
                </span>

                <span className="processing-time">
                  RUNNING
                </span>

              </div>

              <div className="progress-line">
                <div className="progress-fill"></div>
              </div>

              <div className="agent-grid">

                <div className="agent active-agent">
                  <span>01</span>
                  COMPANY RESEARCH
                  <b>RUNNING</b>
                </div>

                <div className="agent active-agent">
                  <span>02</span>
                  TECHNOLOGY
                  <b>RUNNING</b>
                </div>

                <div className="agent active-agent">
                  <span>03</span>
                  FINANCIAL
                  <b>RUNNING</b>
                </div>

                <div className="agent active-agent">
                  <span>04</span>
                  MARKET
                  <b>RUNNING</b>
                </div>

                <div className="agent active-agent">
                  <span>05</span>
                  COMPETITORS
                  <b>RUNNING</b>
                </div>

                <div className="agent active-agent">
                  <span>06</span>
                  AUTOMATION
                  <b>RUNNING</b>
                </div>

              </div>

            </section>
          )}


          {/* =========================================
              ERROR
          ========================================= */}

          {error && (

            <section className="error-panel">

              <div className="error-code">
                ERROR
              </div>

              <div>
                <strong>
                  ANALYSIS FAILED
                </strong>

                <p>{error}</p>
              </div>

            </section>

          )}


          {/* =========================================
              RESULTS
          ========================================= */}

          {report && !loading && (

            <section className="results">

              {/* TARGET */}

              <div className="target-strip">

                <div>
                  <span className="micro-label">
                    TARGET
                  </span>

                  <strong>
                    {companyName}
                  </strong>
                </div>

                <a
                  href={website}
                  target="_blank"
                  rel="noreferrer"
                >
                  {website}
                  ↗
                </a>

              </div>


              {/* DECISION + CONFIDENCE */}

              <div id="section-assessment" className="decision-grid">

                <div className="decision-panel" data-decision={decision.toUpperCase()}>

                  <span className="micro-label">
                    FINAL ASSESSMENT
                  </span>

                  <div className="decision-value">
                    {decision}
                  </div>

                  <div className="decision-line">
                    <span></span>
                  </div>

                  <p>
                    Automated assessment generated
                    from the multi-agent research
                    pipeline.
                  </p>

                </div>


                <div className="confidence-panel">

                  <span className="micro-label">
                    CONFIDENCE
                  </span>

                  <div className="confidence-number">
                    {confidence}
                    <small>%</small>
                  </div>

                  <div className="confidence-track">
                    <div
                      className="confidence-fill"
                      style={{
                        width: `${Math.min(
                          Math.max(confidence, 0),
                          100
                        )}%`,
                      }}
                    ></div>
                  </div>

                  <div className="confidence-meta">
                    <span>0</span>
                    <span>50</span>
                    <span>100</span>
                  </div>

                </div>

              </div>


              {/* OPPORTUNITY */}

              {report.best_opportunity && (

                <section id="section-opportunity" className="opportunity">

                  <div className="opportunity-index">
                    01
                  </div>

                  <div>

                    <span className="micro-label">
                      PRIMARY OPPORTUNITY
                    </span>

                    <h2>
                      {String(
                        report.best_opportunity
                      )}
                    </h2>

                  </div>



                </section>

              )}


              {/* INTELLIGENCE */}

              <div id="section-intelligence" className="section-heading">

                <div>
                  <span>
                    02 / INTELLIGENCE
                  </span>

                  <h2>
                    Assessment Signals
                  </h2>
                </div>

                <p>
                  Structured findings generated
                  by the analysis pipeline.
                </p>

              </div>


              {/* REASONS */}

              <section className="intel-panel">

                <div className="intel-header">

                  <div>
                    <span>
                      SIGNAL / POSITIVE
                    </span>

                    <h3>
                      Why This Company?
                    </h3>
                  </div>

                  <span className="signal positive">
                    POSITIVE
                  </span>

                </div>

                {renderList(report.reasons)}

              </section>


              {/* RISKS */}

              <section className="intel-panel">

                <div className="intel-header">

                  <div>
                    <span>
                      SIGNAL / RISK
                    </span>

                    <h3>
                      Risk Factors
                    </h3>
                  </div>

                  <span className="signal warning">
                    REVIEW
                  </span>

                </div>

                {renderList(report.risks)}

              </section>


              {/* EVIDENCE */}

              <section className="intel-panel">

                <div className="intel-header">

                  <div>
                    <span>
                      SIGNAL / EVIDENCE
                    </span>

                    <h3>
                      Supporting Evidence
                    </h3>
                  </div>

                  <span className="signal neutral">
                    VERIFIED
                  </span>

                </div>

                {renderList(report.evidence)}

              </section>


              {/* ASSUMPTIONS */}

              <section className="intel-panel">

                <div className="intel-header">

                  <div>
                    <span>
                      SIGNAL / ASSUMPTION
                    </span>

                    <h3>
                      Assumptions
                    </h3>
                  </div>

                  <span className="signal warning">
                    CAUTION
                  </span>

                </div>

                {renderList(report.assumptions)}

              </section>


              {/* MISSING */}

              <section className="intel-panel missing-panel">

                <div className="intel-header">

                  <div>
                    <span>
                      SIGNAL / DATA GAP
                    </span>

                    <h3>
                      Missing Information
                    </h3>
                  </div>

                  <span className="signal alert">
                    INCOMPLETE
                  </span>

                </div>

                {renderList(
                  report.missing_information
                )}

              </section>


              {/* FOOTER */}

              <footer className="report-footer">

                <div>
                  AI DEAL ANALYZER
                </div>

                <div>
                  LANGGRAPH MULTI-AGENT SYSTEM
                </div>

                <div>
                  REPORT COMPLETE
                </div>

              </footer>

            </section>

          )}

        </section>

      </main>

    </div>
  );
}

export default App;