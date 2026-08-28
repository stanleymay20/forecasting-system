import pandas as pd

from eu_analytics.quality import (
    coverage_summary,
    latest_available_year,
    missingness_by_group,
    validate_expected_members,
    validate_unique_keys,
)


def sample_frame() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "country": ["DEU", "DEU", "FRA", "FRA"],
            "year": [2023, 2024, 2023, 2024],
            "value": [10.0, 12.0, None, 15.0],
            "secondary": [1.0, None, 3.0, 4.0],
        }
    )


def test_validate_unique_keys_returns_empty_when_unique():
    duplicates = validate_unique_keys(sample_frame(), ["country", "year"])
    assert duplicates.empty


def test_validate_unique_keys_returns_full_duplicate_group():
    frame = sample_frame()
    frame = pd.concat([frame, frame.iloc[[0]]], ignore_index=True)
    duplicates = validate_unique_keys(frame, ["country", "year"])
    assert len(duplicates) == 2
    assert set(duplicates["year"]) == {2023}


def test_validate_expected_members_surfaces_missing_and_unexpected():
    result = validate_expected_members(
        sample_frame(), "country", ["DEU", "FRA", "ITA"]
    )
    assert result == {"missing": ["ITA"], "unexpected": []}


def test_coverage_summary_preserves_missing_values():
    result = coverage_summary(sample_frame(), "country", "year", "value")
    france = result.loc[result["country"] == "FRA"].iloc[0]
    assert france["first_year"] == 2023
    assert france["latest_year"] == 2024
    assert france["observed_years"] == 2
    assert france["non_null_values"] == 1
    assert france["missing_values"] == 1


def test_missingness_by_group_calculates_rate():
    result = missingness_by_group(
        sample_frame(), "country", ["value", "secondary"]
    )
    france_value = result.loc[
        (result["country"] == "FRA") & (result["variable"] == "value")
    ].iloc[0]
    assert france_value["missing"] == 1
    assert france_value["missing_rate"] == 0.5


def test_latest_available_year_ignores_null_analytical_values():
    result = latest_available_year(sample_frame(), "country", "year", "value")
    latest = dict(zip(result["country"], result["latest_available_year"]))
    assert latest == {"DEU": 2024, "FRA": 2024}
