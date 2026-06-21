import pandas as pd
import numpy as np

def parse_dd_hh_mm_ss(val):
    """
    Parse duration in DD:HH:MM:SS format into seconds
    Example: '00:00:36:28'
    """
    if pd.isna(val):
        return np.nan

    try:
        parts = str(val).split(":")
        if len(parts) != 4:
            return np.nan

        days, hours, minutes, seconds = map(int, parts)
        return (
            days * 24 * 3600 +
            hours * 3600 +
            minutes * 60 +
            seconds
        )
    except:
        return np.nan


def add_features(df):
    # Rename columns
    df = df.rename(columns={
        'name': 'UserID',
        'start_time': 'SessionStart',
        'usage_time': 'usage_time_raw',
        'total_transfer': 'DataTransferred',
        'seession_break_reason': 'Status'
    })

    # Parse datetime
    df['SessionStart'] = pd.to_datetime(df['SessionStart'], errors='coerce')

    # Parse duration
    df['usage_seconds'] = df['usage_time_raw'].apply(parse_dd_hh_mm_ss)

    # Keep valid rows
    df = df[
        df['SessionStart'].notna() &
        df['usage_seconds'].notna() &
        (df['usage_seconds'] > 0)
    ]

    # Feature engineering
    df['hour'] = df['SessionStart'].dt.hour
    df['duration_min'] = df['usage_seconds'] / 60

    # Target: Wi-Fi load (KB per minute)
    df['wifi_load'] = df['DataTransferred'] / df['duration_min']

    return df
