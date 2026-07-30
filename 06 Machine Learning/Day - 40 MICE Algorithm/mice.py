"""
MICE: Multiple Imputation by Chained Equations
================================================

This script shows two ways to do MICE-style imputation:

1. Using scikit-learn's IterativeImputer (production-ready, fast)
2. A from-scratch implementation (to show exactly what's happening
   under the hood — the "chained equations" part)

Run with: python mice_algorithm.py
"""

import numpy as np
import pandas as pd
from sklearn.experimental import enable_iterative_imputer  # noqa: F401
from sklearn.impute import IterativeImputer
from sklearn.linear_model import BayesianRidge, LinearRegression


# ---------------------------------------------------------------
# 1. Create a toy dataset with missing values (MAR - missing at random)
# ---------------------------------------------------------------
def make_toy_data(n=200, seed=0):
    rng = np.random.default_rng(seed)

    age = rng.normal(40, 12, n)
    income = 2000 + 500 * age + rng.normal(0, 5000, n)
    hours_worked = 20 + 0.3 * age + rng.normal(0, 5, n)

    df = pd.DataFrame({
        "age": age,
        "income": income,
        "hours_worked": hours_worked,
    })

    # Introduce missingness: income more likely missing for younger people,
    # hours_worked missing at random
    miss_income = rng.random(n) < (0.35 - 0.005 * age)
    miss_hours = rng.random(n) < 0.15

    df.loc[miss_income, "income"] = np.nan
    df.loc[miss_hours, "hours_worked"] = np.nan

    return df


# ---------------------------------------------------------------
# 2a. MICE via scikit-learn (the practical way to actually use this)
# ---------------------------------------------------------------
def sklearn_mice(df, n_imputations=5, random_state=0):
    """
    Runs IterativeImputer multiple times with different random seeds
    to produce several completed datasets (true "multiple" imputation).
    Returns a list of completed DataFrames.
    """
    completed_datasets = []

    for i in range(n_imputations):
        imputer = IterativeImputer(
            estimator=BayesianRidge(),   # model used to predict each missing column
            max_iter=10,                 # number of chained-equation cycles
            sample_posterior=True,       # adds randomness -> different draw each time
            random_state=random_state + i,
        )
        imputed_array = imputer.fit_transform(df)
        completed_datasets.append(
            pd.DataFrame(imputed_array, columns=df.columns)
        )

    return completed_datasets


# ---------------------------------------------------------------
# 2b. MICE from scratch (shows the actual chained-equations logic)
# ---------------------------------------------------------------
def mice_from_scratch(df, n_cycles=10, seed=0):
    """
    Manual implementation of the core MICE loop:

      1. Fill all missing values with column means (placeholder)
      2. For each column with missing data, in turn:
           - regress it on all other columns using only rows where
             it was originally observed
           - predict the missing entries and update them
      3. Repeat for n_cycles so imputations stabilize
    """
    rng = np.random.default_rng(seed)
    data = df.copy()
    missing_mask = data.isna()
    cols_with_missing = missing_mask.columns[missing_mask.any()].tolist()

    # Step 1: initial mean fill
    for col in cols_with_missing:
        data[col] = data[col].fillna(data[col].mean())

    # Step 2 + 3: cycle through columns, refitting each time
    for cycle in range(n_cycles):
        for col in cols_with_missing:
            observed_rows = ~missing_mask[col]
            missing_rows = missing_mask[col]

            if missing_rows.sum() == 0:
                continue

            predictors = [c for c in data.columns if c != col]

            model = LinearRegression()
            model.fit(data.loc[observed_rows, predictors], data.loc[observed_rows, col])

            predictions = model.predict(data.loc[missing_rows, predictors])

            # add small noise so this isn't deterministic single imputation
            noise = rng.normal(0, data[col].std() * 0.1, size=predictions.shape)
            data.loc[missing_rows, col] = predictions + noise

    return data


# ---------------------------------------------------------------
# 3. Demo
# ---------------------------------------------------------------
if __name__ == "__main__":
    df = make_toy_data()
    print("Missing values per column:\n", df.isna().sum(), "\n")

    # --- scikit-learn approach ---
    imputed_sets = sklearn_mice(df, n_imputations=5)
    print(f"Generated {len(imputed_sets)} completed datasets via sklearn's IterativeImputer.")
    print("Mean income across the 5 imputed datasets (shows imputation variability):")
    print([round(d["income"].mean(), 1) for d in imputed_sets], "\n")

    # Pooling example: average an estimate across imputations (Rubin's rules, simplified)
    mean_income_estimate = np.mean([d["income"].mean() for d in imputed_sets])
    print(f"Pooled mean income estimate: {mean_income_estimate:.1f}\n")

    # --- from-scratch approach ---
    manual_result = mice_from_scratch(df, n_cycles=10)
    print("From-scratch MICE — first 5 rows of completed data:")
    print(manual_result.head(), "\n")
    print("Confirm no missing values remain:\n", manual_result.isna().sum())