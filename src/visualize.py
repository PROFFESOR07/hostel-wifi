import matplotlib.pyplot as plt

def plot_predictions(y_test, y_pred):
    plt.figure()
    plt.scatter(y_test, y_pred, alpha=0.6)
    plt.xlabel("Actual Wi-Fi Load")
    plt.ylabel("Predicted Wi-Fi Load")
    plt.title("Predicted vs Actual Wi-Fi Load")
    plt.show()


def plot_peak_hours(df):
    peak = df.groupby('hour')['wifi_load'].mean()

    plt.figure()
    peak.plot(kind='bar')
    plt.title("Average Wi-Fi Load by Hour")
    plt.xlabel("Hour of Day")
    plt.ylabel("Average Wi-Fi Load")
    plt.show()
