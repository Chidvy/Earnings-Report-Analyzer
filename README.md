markdown# Earnings Report Analyzer

An LLM-driven financial document intelligence system that automates earnings report analysis — extracting structured metrics, generating analyst-grade narratives, and enabling interactive document exploration via multi-turn Q&A.

---

## Problem → Solution → Impact

**Problem:** Financial analysts spend 45–60 minutes reviewing earnings reports to extract key metrics, summarize results, and identify risks. The document is long, data is scattered, and follow-up questions require re-reading.

**Solution:** Automated extraction pipeline that reads the report once, returns structured metrics (JSON), generates analyst-style narrative, and enables multi-turn Q&A.

**Impact:** Reduces first-pass review time to under 5 minutes. Metrics are immediately usable in dashboards or further analysis.

---

## Demo
$ python earnings_analyzer.py apple_q4_2024.pdf
============================================================
EARNINGS REPORT ANALYZER
Loading PDF: apple_q4_2024.pdf
Extracted 42,891 characters from 18 pages.
[1/2] Extracting structured metrics...
[2/2] Writing analyst narrative summary...
============================================================
STRUCTURED EXTRACTION
Company: Apple Inc.
Period: Q4 FY2024
Revenue: $94.9B (+6.1% YoY)
EPS: $1.64 (+12% YoY)
Services Revenue: $24.97B (+12% YoY)
iPhone Revenue: $46.2B (+6% YoY)
Key Themes: Services growth | AI integration | Emerging markets
Risks: China competition | Regulatory pressure
Management Tone: Bullish
============================================================
ANALYST SUMMARY
Apple reported strong fourth-quarter results, with revenue of $94.9B
exceeding consensus by approximately $1.2B and EPS of $1.64 beating
estimates by $0.08. Services revenue reached a record $24.97B, up 12%
year-over-year, demonstrating successful diversification beyond hardware.
Gross margin expanded 300 basis points to 45.9%, driving significant EPS
growth...

Q&A Mode — Ask anything about Apple's earnings
You: What drove the Services beat?
Analyst: Services revenue of $24.97B, a record quarter, was driven by
growth across the App Store, Apple Music, iCloud, and AppleCare.
Management cited 1B+ paid subscriptions globally...


## What This Demonstrates

- Applied GenAI to automate financial document review workflows
- Built Python pipelines for unstructured PDF extraction into structured JSON
- Designed analyst-style summaries for executive and investment-facing use cases
- Created interactive Q&A layers for document exploration without rereading
- Demonstrated product thinking through limitations, extensibility, and future roadmap



## Note on LLM Outputs

LLM-generated outputs should be reviewed before use in investment, financial reporting, or compliance workflows. Future versions will add page-level source citations and validation checks to enable audit trails for every extracted metric.

---

## Design Decisions

| Choice | Why It Matters |
|---|---|
| Two-pass extraction and summary | Separates factual metric extraction from narrative generation for clarity and reusability |
| JSON-first output | Enables downstream dashboards, alerts, and comparison workflows without re-parsing |
| Multi-turn Q&A with history | Allows analysts to ask follow-up questions without rereading the document or losing context |
| 80K character truncation | Controls API cost and context size while covering most earnings reports |
| LLM-based extraction | Handles varied report formats and layouts without custom parsing rules |


## Limitations & Future Work

**Current limitations:** Does not yet validate extracted metrics against source tables, does not perform multi-quarter trend analysis, and requires manual report selection.

**Future improvements:**
- Batch processing across multiple quarters with trend analysis and period-over-period comparison
- Page-level source citations for every extracted metric to enable verification
- Multi-company side-by-side earnings comparison
- Dashboard integration for real-time earnings monitoring
- Healthcare variant for clinical trial and hospital financial reporting

## Note on LLM Outputs

LLM-generated outputs should be reviewed before use in investment, financial reporting, or compliance workflows. Future versions will add page-level source citations and validation checks to enable audit trails for every extracted metric.

---

## Tech Stack

- Python 3.9+
- [Anthropic Python SDK](https://github.com/anthropic/anthropic-sdk-python)
- Large Language Model API (Claude / OpenAI compatible)

---

## Author

**Durga Meduri** — Business Analytics Manager | MS Business Analytics, UMass Boston

[LinkedIn](https://www.linkedin.com/in/durga-c-meduri/) | [GitHub](https://github.com/Chidvy)
