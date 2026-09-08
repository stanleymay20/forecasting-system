# EU Innovation, AI & Energy Analytics

A multi-source data analytics project comparing **AI adoption, renewable energy, R&D investment, high-tech exports and economic indicators across 10 European economies** using Python and Pandas.

This repository is being developed as a reproducible MSc data-science project and portfolio case study in **data acquisition, cleaning, validation, multi-source integration, missing-data analysis, KPI construction and comparative visualisation**.

## Recruiter / policy quick scan

**Skills demonstrated:** Python · Pandas · NumPy · data cleaning · data validation · joins/merges · missingness analysis · longitudinal data · KPI design · Eurostat · OECD · World Bank · Matplotlib · reproducible analytics

**Countries:** Austria, Germany, Denmark, Spain, Finland, France, Italy, Netherlands, Poland and Sweden.

## Analytical question

How do European economies differ in their adoption of artificial intelligence, innovation investment, renewable-energy transition and broader economic capacity — and what patterns become visible when these indicators are analysed together rather than in isolation?

## Why this matters for policy and sustainable development

Digital transformation, innovation capacity and energy transition are often discussed separately even though policy choices interact across all three. This project creates a reproducible evidence base for comparing those dimensions while making differences in coverage and reporting periods explicit.

The analytical workflow is relevant to questions such as:

- whether AI adoption is concentrated in particular enterprise-size groups;
- how innovation investment differs across economies;
- whether renewable-energy progress and technology capacity move together or diverge;
- how structural indicators such as GDP per capita and high-tech exports change the interpretation of headline rankings;
- where missing or non-comparable data prevents a defensible conclusion.

Potential Sustainable Development Goal relevance includes **SDG 7 (Affordable and Clean Energy), SDG 8 (Decent Work and Economic Growth), SDG 9 (Industry, Innovation and Infrastructure) and SDG 13 (Climate Action)**. This mapping identifies analytical domains; it is not a claim of UN endorsement or causal SDG impact.

## Data sources

### Eurostat — enterprise AI adoption

The working analysis uses enterprise AI indicators including measures such as:

- `E_AI_ADOWN`
- `E_AI_EC`
- `E_AI_P1ANY`
- `E_AI_TANY`

The current analysis contains observations for **2021, 2023, 2024 and 2025**, with enterprise-size breakdowns for small, medium, combined SME and large enterprises.

### Eurostat — renewable energy

A longitudinal renewable-energy series is used to compare the selected countries over time. The working analysis currently spans **2004–2025** for the selected-country extract.

### OECD — research & development

OECD R&D indicators are used to examine innovation investment and growth. The working filtered dataset currently covers **2016–2024** for the selected economies.

### World Bank — structural economic indicators

The project integrates World Bank series for wider economic context, including:

- R&D expenditure as a percentage of GDP;
- high-technology exports;
- GDP per capita.

The World Bank series have different availability windows and substantial variation in missingness, so coverage is treated explicitly rather than silently filled.

## Current data pipeline

```text
Eurostat AI adoption ───────┐
Eurostat renewable energy ──┤
OECD R&D ───────────────────┼─> schema review
World Bank indicators ──────┘       ↓
                               country filtering
                                      ↓
                               type normalisation
                                      ↓
                           missingness / coverage checks
                                      ↓
                         reshape + merge / aligned keys
                                      ↓
                        indicator-specific analytical tables
                                      ↓
                           comparative visualisations
                                      ↓
                         evidence-based interpretation
```

## Data-quality principles

This project deliberately avoids treating missing values as zero or pretending that every source has equal temporal coverage.

The analysis checks:

- expected-country coverage;
- observed year ranges;
- duplicate country/year keys;
- missing values by country and indicator;
- latest available observation by country;
- differences in source frequency and reporting windows;
- whether cross-source comparisons use genuinely comparable periods.

Reusable quality-control functions are provided in `src/eu_analytics/quality.py` and tested in `tests/`.

## Working coverage snapshot

| Dataset | Selected countries | Working time coverage |
| --- | ---: | --- |
| Eurostat AI adoption | 10 | 2021, 2023, 2024, 2025 |
| Eurostat renewable energy | 10 | 2004–2025 |
| OECD R&D | 10 | 2016–2024 |
| World Bank R&D (% GDP) | 10 | historical series, latest observations vary |
| World Bank high-tech exports | 10 | historical series, latest observations vary |
| World Bank GDP per capita | 10 | long-run historical series |

The table describes the current working analysis and should be regenerated from the final notebook before publication of final numerical conclusions.

## Repository structure

```text
.
├── .github/workflows/ci.yml
├── data/
│   └── README.md
├── notebooks/
│   └── README.md
├── src/
│   └── eu_analytics/
│       ├── __init__.py
│       └── quality.py
├── tests/
│   └── test_quality.py
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Reusable data-quality utilities

```python
from eu_analytics.quality import (
    coverage_summary,
    missingness_by_group,
    validate_expected_members,
    validate_unique_keys,
)
```

These utilities are intentionally separate from notebook presentation code so data-quality logic can be tested independently.

## Run the quality-control tests

```bash
git clone https://github.com/stanleymay20/forecasting-system.git
cd forecasting-system
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
pytest
```

GitHub Actions also runs the test suite automatically on pushes and pull requests.

## Analytical outputs being developed

The final analysis is designed to include:

- AI adoption comparison across countries and enterprise sizes;
- renewable-energy trajectories;
- R&D investment and growth comparisons;
- high-tech export and GDP context;
- coverage/missingness diagnostics before cross-source analysis;
- ranked and longitudinal visualisations;
- interpretation focused on economic and policy meaning rather than chart volume.

## Evidence boundaries

This repository demonstrates the reproducible analytical framework and automated quality checks. Cross-country patterns should not be interpreted as causal relationships without an appropriate research design, and apparent rankings should not override differences in temporal coverage or indicator definitions.

The authoritative MSc analysis notebook and final visual outputs will be added when ready for portfolio release. Until then, this repository should be treated as the reproducible project framework rather than the final academic submission.

## Author

**Stanley Osei-Wusu**
