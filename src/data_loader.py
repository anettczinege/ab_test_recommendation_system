import pandas as pd

def load_cleaned_data(path="../data/processed/streaming_ab_test_sessions_cleaned.csv"):
    """
    Load cleaned A/B test dataset and enforce schema consistency.
    """

    df = pd.read_csv(path)

    # Convert datetime columns
    df["session_start"] = pd.to_datetime(df["session_start"])
    df["session_end"] = pd.to_datetime(df["session_end"])

    # Convert identifier columns
    df["user_id"] = df["user_id"].astype("string")
    df["session_id"] = df["session_id"].astype("string")
    df["app_version"] = df["app_version"].astype("string")

    # Convert categorical columns
    categorical_columns = [
        "group",
        "device_type",
        "os",
        "language_preference",
        "referral_source",
        "subscription_type"
    ]

    df[categorical_columns] = df[categorical_columns].astype("category")

    # Convert boolean column
    df["is_premium_user"] = df["is_premium_user"].astype("boolean")

    return df
