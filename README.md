# EU Innovation, AI & Energy Analytics

A multi-source data analytics project comparing **AI adoption, renewable energy, R&D investment, high-tech exports and economic indicators across 10 European economies** using Python and Pandas.

This repository is being developed as a reproducible MSc data-science project and portfolio case study in **data acquisition, cleaning, validation, multi-source integration, missing-data analysis, KPI construction and comparative visualisation**.

## Recruiter quick scan

**Skills demonstrated:** Python · Pandas · NumPy · data cleaning · data validation · joins/merges · missingness analysis · longitudinal data · KPI design · Eurostat · OECD · World Bank · Matplotlib · reproducible analytics

**Countries:** Austria, Germany, Denmark, Spain, Finland, France, Italy, Netherlands, Poland and Sweden.

## Analytical question

How do European economies differ in their adoption of artificial intelligence, innovation investment, renewable-energy transition and broader economic capacity — and what patterns become visible when these indicators are analysed together rather than in isolation?

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

The project also integrates World Bank series used to provide wider economic context, including:

- R&D expenditure as a percentage of GDP
- high-technology exports
- GDP per capita

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

The package includes small, testable helpers for the kinds of checks used throughout the project:

```python
from eu_analytics.quality import (
    coverage_summary,
    missingness_by_group,
    validate_expected_members,
    validate_unique_keys,
)
```

These utilities are intentionally separate from notebook presentation code so that data-quality logic can be tested independently.

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
- interpretation focused on economic and business meaning rather than chart volume.

## Why this project is relevant to data analyst roles

The main value of the project is not simply that it contains several charts. It demonstrates the work required **before** trustworthy visualisation:

1. acquire data from multiple institutional sources;
2. understand incompatible schemas and frequencies;
3. clean and standardise identifiers;
4. inspect missingness and temporal coverage;
5. construct comparable analytical tables;
6. choose KPIs that answer a concrete question;
7. communicate the result without overstating what the data proves.

That workflow maps directly to real analyst work involving operational datasets, dashboards, KPI reporting and stakeholder-facing analysis.

## Publication status

The reusable repository structure and automated quality checks are now in place. The next publication step is to add the **authoritative MSc analysis notebook and final visual outputs** once the current notebook is ready for portfolio release.

Until that source notebook is added, this repository should be treated as the reproducible project framework rather than the final academic submission.

## Author

**Stanley Osei-Wusu**
