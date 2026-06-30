"""
Overall inter-rater reliability analysis for IRR.xlsx.

This program reads the cleaned Excel file and reports overall agreement and
Cohen's Kappa statistics for the five evaluation dimensions in the dataset.
"""
print("Program started!")

import pandas as pd
from sklearn.metrics import cohen_kappa_score


EXCEL_FILE = "IRR.xlsx"


def load_dataset(file_path):
    """Read the Excel file while preserving N/A as an error taxonomy category."""
    return pd.read_excel(file_path, engine="openpyxl", keep_default_na=False)


def interpret_kappa(kappa_value):
    """Return the Landis and Koch interpretation for a Kappa value."""
    if kappa_value < 0:
        return "Poor"
    if kappa_value <= 0.20:
        return "Slight"
    if kappa_value <= 0.40:
        return "Fair"
    if kappa_value <= 0.60:
        return "Moderate"
    if kappa_value <= 0.80:
        return "Substantial"
    return "Almost Perfect"


def calculate_percentage_agreement(rater_one, rater_two):
    """Calculate the percentage of rows where both raters assigned the same value."""
    agreement_rate = (rater_one == rater_two).mean()
    return agreement_rate * 100


def calculate_reliability(df, metric_name, member_one_column, member_two_column, weights=None):
    """Calculate percentage agreement, Cohen's Kappa, and interpretation for one metric."""
    member_one_scores = df[member_one_column]
    member_two_scores = df[member_two_column]

    percentage_agreement = calculate_percentage_agreement(
        member_one_scores,
        member_two_scores,
    )
    kappa = cohen_kappa_score(
        member_one_scores,
        member_two_scores,
        weights=weights,
    )

    return {
        "metric": metric_name,
        "statistic": (
            "Weighted Cohen's Kappa (quadratic weights)"
            if weights == "quadratic"
            else "Cohen's Kappa"
        ),
        "percentage_agreement": percentage_agreement,
        "kappa": kappa,
        "interpretation": interpret_kappa(kappa),
    }


def build_reliability_results(df):
    """Compute reliability results for all five evaluation dimensions."""
    # Define each evaluation dimension and its corresponding scoring method.
    metrics = [
        {
            "metric_name": "Final Answer",
            "member_one_column": "Member1_FA",
            "member_two_column": "Member2_FA",
            "weights": None,
        },
        {
            "metric_name": "Programming Correctness",
            "member_one_column": "Member1_PC",
            "member_two_column": "Member2_PC",
            "weights": "quadratic",
        },
        {
            "metric_name": "Reasoning Quality",
            "member_one_column": "Member1_RQ",
            "member_two_column": "Member2_RQ",
            "weights": "quadratic",
        },
        {
            "metric_name": "Hallucination",
            "member_one_column": "Member1_HAL",
            "member_two_column": "Member2_HAL",
            "weights": None,
        },
        {
            "metric_name": "Error Taxonomy",
            "member_one_column": "Member1_ERR",
            "member_two_column": "Member2_ERR",
            "weights": None,
        },
    ]

    return [
        calculate_reliability(
            df,
            metric["metric_name"],
            metric["member_one_column"],
            metric["member_two_column"],
            metric["weights"],
        )
        for metric in metrics
    ]


def print_report(results):
    """Display the inter-rater reliability results in a neat terminal report."""
    print("=" * 52)
    print("INTER-RATER RELIABILITY ANALYSIS")
    print("=" * 52)
    print()

    for result in results:
        print(f"Metric: {result['metric']}")
        print(f"Statistic: {result['statistic']}")
        print(f"Percentage Agreement: {result['percentage_agreement']:.3f}%")
        print(f"Kappa Value: {result['kappa']:.3f}")
        print(f"Interpretation: {result['interpretation']}")
        print()

    print("Analysis Complete.")
    


def main():
    """Run the full inter-rater reliability analysis."""
    print("Reading IRR.xlsx...\n")
    df = load_dataset(EXCEL_FILE)
    print(f"Total responses analysed: {len(df)}\n")
    results = build_reliability_results(df)
    print_report(results)
    print()


if __name__ == "__main__":
    main()
