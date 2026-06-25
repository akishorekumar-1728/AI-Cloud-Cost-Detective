import pandas as pd

def detect_anomalies():

    df = pd.read_csv("data/cost_history.csv")

    anomalies = []

    for _, row in df.iterrows():

        previous = row["Previous_Cost"]
        current = row["Current_Cost"]

        if current > previous * 2:

            anomalies.append({
                "Resource": row["Resource"],
                "Previous Cost": previous,
                "Current Cost": current,
                "Increase %": round(
                    ((current - previous) / previous) * 100,
                    2
                )
            })

    return anomalies