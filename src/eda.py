import matplotlib.pyplot as plt

def plot_hourly_usage(df, save_path=None):
    """
    Plots total data usage by hour (safe version)
    """
    if 'hour' not in df.columns or df.empty:
        print(" Not enough data to plot hourly usage.")
        return

    hourly = df.groupby('hour')['DataTransferred'].sum()

    if hourly.empty:
        print(" Hourly usage data is empty. Skipping plot.")
        return

    plt.figure()
    hourly.plot(kind='bar')
    plt.title("Total Data Usage by Hour")
    plt.xlabel("Hour of Day")
    plt.ylabel("Total Data Transferred")

    if save_path:
        plt.savefig(save_path)
    plt.show()



def heavy_users(df, top_n=10):
    """
    Identify data-hungry users
    """
    return (
        df.groupby('UserID')['DataTransferred']
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
    )


def idle_timeout_sessions(df):
    """
    Analyze idle timeout excuses 
    """
    return df[df['Status'].str.contains('idle', case=False, na=False)]
