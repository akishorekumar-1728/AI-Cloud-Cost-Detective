from anomaly_detector import detect_anomalies

results = detect_anomalies()

print("===== Anomaly Detection Results =====")

for item in results:
    print(item)