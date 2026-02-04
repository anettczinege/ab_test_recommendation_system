import numpy as np
import pandas as pd


# -----------------------------
# User-Level Click-Through Rate
# -----------------------------
def compute_user_ctr(total_clicks: pd.Series,
                     total_impressions: pd.Series) -> pd.Series:
    values = np.where(
        total_impressions > 0,
        total_clicks / total_impressions,
        0
    )
    return pd.Series(values, index=total_clicks.index)


# -----------------------------
# 7-Day Return Rate
# -----------------------------
def compute_7day_return_flag(df: pd.DataFrame) -> pd.Series:
    """
    Returns a Series indexed by user_id, indicating whether a user returned
    within 1–7 days after their first session.
    """

    df_sorted = df.sort_values(["user_id", "session_start"])

    first_sessions = (
        df_sorted.groupby("user_id", observed=True)["session_start"]
        .first()
    )

    df_sorted = df_sorted.merge(
        first_sessions.rename("first_session"),
        on="user_id"
    )

    df_sorted["days_since_first"] = (
        df_sorted["session_start"] - df_sorted["first_session"]
    ).dt.days

    return_flag = (
        df_sorted[
            (df_sorted["days_since_first"] > 0) &
            (df_sorted["days_since_first"] <= 7)
        ]
        .groupby("user_id", observed=True)
        .size()
        .gt(0)
        .astype(int)
    )

    return return_flag


# -----------------------------
# User-Level Completion Rate
# -----------------------------
def compute_user_completion_rate(total_completed: pd.Series,
                                 total_started: pd.Series) -> pd.Series:
    values = np.where(
        total_started > 0,
        total_completed / total_started,
        0
    )
    return pd.Series(values, index=total_completed.index)


# --------------------------------------------
# User-Level Average Minutes Watched per Session
# --------------------------------------------
def compute_avg_minutes_watched(total_watch_time: pd.Series,
                                total_sessions: pd.Series) -> pd.Series:
    values = np.where(
        total_sessions > 0,
        total_watch_time / total_sessions,
        0
    )
    return pd.Series(values, index=total_watch_time.index)

