import pandas as pd
import numpy as np

def normalize_orders(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.lower().str.strip()
    if "order_status" in df.columns:
        df["order_status"] = df["order_status"].replace({
            "shipped ": "shipped",
            "canceled ": "canceled"
        })
    return df

def normalize_payments(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.lower().str.strip()
    if "payment_type" in df.columns:
        df["payment_type"] = df["payment_type"].replace({
            "creditcard": "credit_card",
            "credit card": "credit_card"
        })
        freq = df["payment_type"].value_counts(normalize=True)
        rare = freq[freq < 0.01].index
        df["payment_type"] = df["payment_type"].replace(rare, "other")
    return df

def normalize_reviews(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.lower().str.strip()
    return df

def normalize_all(orders: pd.DataFrame,
                  payments: pd.DataFrame,
                  reviews: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    orders_clean = normalize_orders(orders)
    payments_clean = normalize_payments(payments)
    reviews_clean = normalize_reviews(reviews)
    return orders_clean, payments_clean, reviews_clean

def log_transform_skewed(df, skew_threshold=1.0):
    """
    Apply log1p transformation to skewed continuous numeric columns.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe.
    skew_thresh : float, optional
        Minimum skewness for applying log transform (default = 1.0).
    unique_thresh : int, optional
        Minimum number of unique values to treat a column as continuous (default = 10).

    Returns
    -------
    pd.DataFrame
        Transformed dataframe with log applied where appropriate.
    """
    df = df.copy()
    # Columns to explicitly exclude
    exclude_cols = ["delivered_flag", "payment_sequential", "payment_installments"]

    for col in df.select_dtypes(include="number").columns:
        if col in exclude_cols:
            print(f"Skipped (excluded): {col}")
            continue

        skew = df[col].skew()
        if abs(skew) > skew_threshold:
            df[col] = np.log1p(df[col].clip(lower=0))  # log1p handles zeros safely
            print(f"Applied log transform on: {col} (skew={skew:.2f})")
        else:
            print(f"Skipped (low skew): {col} (skew={skew:.2f})")

    return df