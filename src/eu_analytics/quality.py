"""Small, dependency-light data-quality helpers for multi-source indicator analysis.

The functions in this module do not impute or alter analytical values. They surface
coverage, missingness and key-integrity problems so downstream analysis can make an
explicit decision about how to handle them.
"""

from __future__ import annotations

from collections.abc import Iterable

import pandas as pd


def _require_columns(frame: pd.DataFrame, columns: Iterable[str]) -> None:
    missing = [column for column in columns if column not in frame.columns]
    if missing:
        raise KeyError(f"Missing required columns: {missing}")


def validate_unique_keys(frame: pd.DataFrame, keys: list[str]) -> pd.DataFrame:
    """Return duplicate key rows; an empty result means the key is unique.

    The full duplicate groups are returned rather than a boolean so an analyst can
    inspect the exact records responsible for an integrity failure.
    """
    _require_columns(frame, keys)
    return frame.loc[frame.duplicated(subset=keys, keep=False)].sort_values(keys)


def validate_expected_members(
    frame: pd.DataFrame,
    column: str,
    expected: Iterable[str],
) -> dict[str, list[str]]:
    """Compare observed categorical members with an expected set.

    Null values are excluded from the observed member set and should be inspected via
    missingness checks instead.
    """
    _require_columns(frame, [column])
    expected_set = {str(item) for item in expected}
    observed_set = {str(item) for item in frame[column].dropna().unique()}
    return {
        "missing": sorted(expected_set - observed_set),
        "unexpected": sorted(observed_set - expected_set),
    }


def coverage_summary(
    frame: pd.DataFrame,
    group_col: str,
    year_col: str,
    value_col: str,
) -> pd.DataFrame:
    """Summarise observed time coverage and non-null values by group.

    Rows with null years are excluded from first/last-year calculations. A row with a
    present year but a null analytical value contributes to row_count but not
    non_null_values.
    """
    _require_columns(frame, [group_col, year_col, value_col])

    work = frame[[group_col, year_col, value_col]].copy()
    work[year_col] = pd.to_numeric(work[year_col], errors="coerce")

    rows = []
    for group, subset in work.groupby(group_col, dropna=False):
        years = subset[year_col].dropna()
        rows.append(
            {
                group_col: group,
                "first_year": int(years.min()) if not years.empty else pd.NA,
                "latest_year": int(years.max()) if not years.empty else pd.NA,
                "observed_years": int(years.nunique()),
                "row_count": int(len(subset)),
                "non_null_values": int(subset[value_col].notna().sum()),
                "missing_values": int(subset[value_col].isna().sum()),
            }
        )

    return pd.DataFrame(rows).sort_values(group_col).reset_index(drop=True)


def missingness_by_group(
    frame: pd.DataFrame,
    group_col: str,
    value_cols: list[str],
) -> pd.DataFrame:
    """Return missing-value counts and rates for each group and value column."""
    _require_columns(frame, [group_col, *value_cols])

    rows = []
    for group, subset in frame.groupby(group_col, dropna=False):
        denominator = len(subset)
        for value_col in value_cols:
            missing_count = int(subset[value_col].isna().sum())
            rows.append(
                {
                    group_col: group,
                    "variable": value_col,
                    "rows": int(denominator),
                    "missing": missing_count,
                    "missing_rate": (
                        missing_count / denominator if denominator else float("nan")
                    ),
                }
            )

    return pd.DataFrame(rows).sort_values([group_col, "variable"]).reset_index(drop=True)


def latest_available_year(
    frame: pd.DataFrame,
    group_col: str,
    year_col: str,
    value_col: str,
) -> pd.DataFrame:
    """Return the latest year containing a non-null value for each group."""
    _require_columns(frame, [group_col, year_col, value_col])

    work = frame[[group_col, year_col, value_col]].copy()
    work[year_col] = pd.to_numeric(work[year_col], errors="coerce")
    work = work.loc[work[year_col].notna() & work[value_col].notna()]

    if work.empty:
        return pd.DataFrame(columns=[group_col, "latest_available_year"])

    result = (
        work.groupby(group_col, dropna=False)[year_col]
        .max()
        .rename("latest_available_year")
        .reset_index()
    )
    result["latest_available_year"] = result["latest_available_year"].astype(int)
    return result.sort_values(group_col).reset_index(drop=True)
