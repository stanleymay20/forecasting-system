# Data

This project combines institutional datasets from **Eurostat, OECD and the World Bank**.

Raw third-party data should only be committed when redistribution is appropriate and the source licence permits it. Otherwise, this directory should contain small derived extracts, schemas, data dictionaries or documented acquisition instructions.

## Working source families

### Eurostat

- Enterprise AI adoption indicators
- Enterprise-size breakdowns
- Renewable-energy indicators

### OECD

- Research and development indicators
- Growth / change measures used in the working analysis

### World Bank

- R&D expenditure (% of GDP)
- High-technology exports
- GDP per capita

## Selected countries

The analysis is scoped to:

```text
AUT  Austria
DEU  Germany
DNK  Denmark
ESP  Spain
FIN  Finland
FRA  France
ITA  Italy
NLD  Netherlands
POL  Poland
SWE  Sweden
```

## Data handling rules

1. Preserve source identifiers before harmonisation.
2. Keep country-code mappings explicit.
3. Never silently replace missing values with zero.
4. Check duplicate country/year/indicator keys before merges.
5. Record the observed time range for every source.
6. Compare indicators only over defensible overlapping periods.
7. Keep source-specific units and transformations documented.
8. Regenerate coverage tables from source data rather than manually maintaining final statistics.

The reusable checks in `src/eu_analytics/quality.py` support these rules.
