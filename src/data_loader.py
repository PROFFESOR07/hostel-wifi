import pandas as pd

def load_data(path):
    """
    Load dataset and basic cleaning
    """
    df = pd.read_csv(path)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Parse datetime
    df['start_time'] = pd.to_datetime(df['start_time'])

    return df
