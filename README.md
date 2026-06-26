# ☁️ AI Cloud Cost Detective

## Overview

AI Cloud Cost Detective is a FinOps-inspired cloud cost optimization platform built using Python, Streamlit, and Microsoft Azure. The application helps organizations monitor, analyze, and optimize cloud spending by integrating with the Azure Cost Management API.

It provides real-time cloud cost insights, identifies high-cost resources, detects spending anomalies, estimates potential savings, and offers optimization recommendations through an interactive dashboard.

---

## Features

* ✅ Azure Cost Management API Integration
* ✅ Real-Time Cloud Cost Analysis
* ✅ Interactive Streamlit Dashboard
* ✅ Resource-wise Cost Breakdown
* ✅ Cost Distribution Charts
* ✅ High-Cost Resource Detection
* ✅ Cost Anomaly Detection
* ✅ Savings Calculator
* ✅ AI-based Cost Optimization Recommendations
* ✅ Docker Support

---

## Tech Stack

| Category         | Technologies              |
| ---------------- | ------------------------- |
| Language         | Python                    |
| Frontend         | Streamlit                 |
| Cloud            | Microsoft Azure           |
| APIs             | Azure Cost Management API |
| Authentication   | Azure Identity            |
| Visualization    | Plotly                    |
| Data Processing  | Pandas                    |
| Containerization | Docker                    |

---

## Project Architecture

```text
Azure Subscription
        │
        ▼
Azure Cost Management API
        │
        ▼
Python Backend
        │
 ┌───────────────┐
 │ Cost Analysis │
 └───────────────┘
        │
        ▼
Anomaly Detection
        │
        ▼
Savings Calculator
        │
        ▼
AI Recommendations
        │
        ▼
Streamlit Dashboard
```

---

## Screenshots

Add your screenshots here after uploading them.

* Dashboard
* Cost Analysis
* Azure Cost Integration
* Charts
* Anomaly Detection

---

## Installation

```bash
git clone https://github.com/your-username/AI-Cloud-Cost-Detective.git

cd AI-Cloud-Cost-Detective

pip install -r requirements.txt

streamlit run app.py
```

---

## Docker

```bash
docker build -t ai-cloud-cost-detective .

docker run --env-file .env -p 8501:8501 ai-cloud-cost-detective
```

---

## Future Enhancements

* AWS Cost Explorer Integration
* Google Cloud Billing Integration
* AI Cost Forecasting
* Email Alerts
* Slack & Microsoft Teams Notifications
* Monthly FinOps Reports
* Cost Optimization Automation

---

## Author

**A. Kishore Kumar**

Final Year B.Tech Information Technology Student

Cloud Computing | DevOps | Azure | Docker | Kubernetes | Python
