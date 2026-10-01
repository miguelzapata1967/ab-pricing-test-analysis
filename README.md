# Project Context & AI Assistance
This project was completed as part of my Data Engineering Academy studies and used as a learning exercise in operational analytics, demand forecasting, and inventory planning.

I used AI tools, including Claude, to help work through the project and understand the analytical methods. Claude performed the analysis, including the advanced forecasting, calculations, and generation of recommendations. These outputs are shared as AI-assisted educational work; I do not claim to have independently built or validated all of the models.

My participation involved working with Python with AI assistance, asking questions, studying the outputs, and learning how analytical results relate to operational decisions. Including this project in my portfolio documents that learning process and my developing ability to question assumptions, interpret results, and explain business implications.

ChatGPT/Codex assisted with organizing and writing the project documentation. The reported results remain subject to the limitations and validation needs described in the analysis and technical documents.


# Company XYZ Pricing A/B Test

A portfolio analysis of a pricing experiment comparing **$39** and **$59**, with emphasis on business impact, statistical evidence, data quality, and unresolved analytical questions.

## Headline Results

- **Conversion:** $39 = **1.990%**; $59 = **1.556%**
- **Conversion difference:** **0.434 percentage points** in favor of $39
- **Revenue per exposed user (RPU):** $39 = **$0.776**; $59 = **$0.918**
- **Observed RPU change at $59:** **+18.25%**
- **Conversion difference:** statistically significant (**z = 8.744, p = 2.25e-18**)
- **Observed valid-timestamp test period:** March 2–May 31, 2015

## Business Interpretation

The experiment shows a clear tradeoff: **$39 generated the higher observed conversion rate, while $59 generated the higher observed revenue per exposed user.**

For the specific objective of maximizing observed RPU among the two tested prices, $59 performed better on that metric. This does **not** establish that $59 maximizes net profit or long-term customer value because product costs, retention, churn, refunds, lifetime value, customer satisfaction, and other long-term outcomes are not supplied.

If the business intends to pursue **$59**, the next analytical phase should focus on improving customer acceptance of the higher price while protecting its observed RPU advantage. That would include additional testing of value proposition and messaging, acquisition and funnel behavior, investigation of unresolved anomalies, and defined conversion/RPU guardrails before broader rollout.

## Data-Quality & Investigation Highlights

The project preserves an audit trail rather than silently repairing uncertain data:

- **365** test/price assignment mismatches were isolated from clean pricing analysis.
- **5,177** invalid timestamps were preserved and excluded from analyses requiring reliable time information; otherwise-valid fields can still contribute to appropriate non-time analyses.
- **41,141** clean records lack geographic information and therefore do not contribute to geographic segmentation.
- **686 of 923 cities (74.3%)** have fewer than 100 users in at least one price group under an exploratory flag. The `<100` rule is descriptive, not a statistically derived reliability threshold.
- A notable **Linux/$59 anomaly** was identified: **1,926 users and zero recorded conversions**, compared with 34 conversions among 2,204 Linux users at $39. The supplied data cannot establish the root cause, so the issue remains explicitly documented as an open investigation item.
- Marketing, device, OS, and geographic segment findings are treated as exploratory where multiple-comparison and sample-size concerns limit interpretation.
- Aggregate monthly and weekly patterns can be described, but the supplied fields cannot isolate or rule out a novelty effect.
- The original predetermined sample-size target is unavailable, so the observed ~91-day period is not presented as the scientifically required stopping point.

## Portfolio Documents

- [`readme_analysis.md`](readme_analysis.md) — full business and data analysis, Questions 1–15, evidence boundaries, findings, limitations, and strategic implications.
- [`readme_tech.md`](readme_tech.md) — technical validation, cleaning, calculations, statistical methodology, segmentation rules, anomalies, audit trail, and reproducibility.
- `A_B_Testing_P1.py` — Python workflow used for validation, cleaning, analysis, and segmentation.

## Analytical Standard

The project follows a simple principle:

**Detected → examined → resolved when evidence permits → explicitly documented as unresolved when available evidence cannot support a defensible resolution.**

The goal is not to force every observation into a conclusion. It is to distinguish what the experiment demonstrates, what it suggests, and what requires additional evidence.

## 📊 Power BI Dashboard & Presentation

The Power BI dashboard provides a visual presentation of the A/B pricing experiment, including conversion performance, revenue per user, trends, segmentation, and key business findings.

➡️ **[View the Power BI Dashboard Presentation (PDF)](Docs/Pricing_AB_Test_Dashboard.pdf)**

The original Power BI file is also included in this repository:

`Pricing_AB_Test_Dashboard.pbix`
