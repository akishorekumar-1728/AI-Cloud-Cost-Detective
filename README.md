# AI Cloud Cost Detective

## Overview

AI Cloud Cost Detective is a FinOps-inspired cloud cost optimization platform that helps organizations monitor, analyze, and optimize cloud spending.

The application integrates with Azure Cost Management APIs to retrieve real cloud cost data, detect anomalies, identify expensive resources, estimate savings opportunities, and provide optimization recommendations through an interactive dashboard.

## Features

* Real Azure Cost Management API Integration
* Cloud Cost Analysis Dashboard
* Resource-wise Cost Breakdown
* Cost Distribution Visualizations
* High Cost Resource Detection
* Cost Anomaly Detection
* Savings Estimation
* Cost Optimization Recommendations
* Dockerized Deployment
* Streamlit-based User Interface

## Tech Stack

* Python
* Streamlit
* Azure Cost Management API
* Azure Identity
* Pandas
* Plotly
* Docker

## Project Architecture

Azure Subscription
↓
Azure Cost Management API
↓
Python Backend
↓
Cost Analysis Engine
↓
Anomaly Detection Engine
↓
Savings Calculator
↓
Streamlit Dashboard

## Installation

```bash
git clone <repository-url>

cd AI-Cloud-Cost-Detective

pip install -r requirements.txt

streamlit run app.py
```

## Docker

```bash
docker build -t ai-cloud-cost-detective .

docker run -p 8501:8501 ai-cloud-cost-detective
```

## Future Enhancements

* Multi-cloud support (AWS, Azure, GCP)
* AI-powered cost forecasting
* Slack/Teams alerts
* Automated optimization recommendations
* FinOps reporting

## Author

A. Kishore Kumar
Final Year Information Technology Student
Cloud | DevOps | Azure | Kubernetes
