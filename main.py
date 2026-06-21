import pandas as pd
from src.data_loader import load_data
from src.feature_engineering import add_features
from src.model import get_model
from src.train import train_model
from src.evaluate import evaluate_model

DATA_PATH = "data/Internetusage_Beginnertask03.csv"

def main():
    # Load & preprocess
    df = load_data(DATA_PATH)
    df = add_features(df)

    print("Rows after feature engineering:", len(df))
    if len(df) < 10:
        print(" Not enough data to train model.")
        return

    # Features & target
    features = ['hour', 'duration_min']
    X = df[features]
    y = df['wifi_load']

    # Train model
    model = get_model()
    model, X_test, y_test = train_model(model, X, y)

    # Evaluate
    mae, rmse, _ = evaluate_model(model, X_test, y_test)

    print("\nModel Performance")
    print("----------------")
    print(f"MAE  : {mae:.2f}")
    print(f"RMSE : {rmse:.2f}")

    # Best hours (lowest average load)
    best_hours = (
        df.groupby('hour')['wifi_load']
        .mean()
        .sort_values()
        .head(3)
        .index
        .tolist()
    )

    print("\nBest hours for binge-watching / downloads:", best_hours)

    # ---------------- USER INPUT SECTION ---------------- #

    print("\n--- Wi-Fi Load Prediction (User Input) ---")

    try:
        hour = int(input("Enter hour of day (0-23): "))
        duration = float(input("Enter expected session duration (minutes): "))

        user_df = pd.DataFrame(
            [[hour, duration]],
            columns=['hour', 'duration_min']
        )

        predicted_load = model.predict(user_df)[0]

        # Hour-wise 75th percentile baseline
        hourly_p75 = df.groupby('hour')['wifi_load'].quantile(0.75)
        baseline = hourly_p75.get(hour, y.quantile(0.75))

        print(
            f"\nPredicted Wi-Fi load: "
            f"{predicted_load:.2f} KB/min "
            f"({predicted_load/1024:.2f} MB/min)"
        )
        print(f"75th percentile load at {hour}:00 → {baseline:.2f} KB/min")

        if predicted_load > baseline:
            print(" Heavier than most sessions at this hour")
        else:
            print(" Lighter than most sessions at this hour")

    except:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
