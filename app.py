import streamlit as st
import pandas as pd
import plotly.express as px

from recommendations import generate_recommendation
from anomaly_detector import detect_anomalies
from savings_calculator import calculate_savings
from azure_cost_service import get_azure_cost_data

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Cloud Cost Detective",
    page_icon="☁️",
    layout="wide"
)

st.title("☁️ AI Cloud Cost Detective")

# -----------------------------
# Load Sample Cost Data
# -----------------------------

df = pd.read_csv("data/sample_cost.csv")

# -----------------------------
# Cloud Cost Data
# -----------------------------

st.subheader("📋 Cloud Cost Data")

st.dataframe(df)

# -----------------------------
# Cost Metrics
# -----------------------------

total_cost = df["Cost"].sum()

savings_data = calculate_savings(total_cost)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "💰 Total Monthly Cost",
        f"₹{total_cost}"
    )

with col2:
    st.metric(
        "💵 Potential Savings",
        f"₹{savings_data['savings']}"
    )

with col3:
    st.metric(
        "✅ Optimized Cost",
        f"₹{savings_data['optimized_cost']}"
    )

# -----------------------------
# Azure Cost Data
# -----------------------------

st.subheader("☁️ Real Azure Cost Data")

azure_data = get_azure_cost_data()
if isinstance(azure_data, dict) and "error" in azure_data:
    st.error(f"Azure Error: {azure_data['error']}")

if azure_data:

    rows = azure_data["properties"]["rows"]

    azure_total = sum(row[0] for row in rows)

    st.metric(
        "Azure Month-To-Date Cost",
        f"₹{round(azure_total, 2)}"
    )

else:
    st.warning("Unable to fetch Azure Cost Data")

# -----------------------------
# Most Expensive Resource
# -----------------------------

highest_resource = df.loc[df["Cost"].idxmax()]

st.subheader("🔴 Most Expensive Resource")

st.success(
    f"{highest_resource['Resource']} - ₹{highest_resource['Cost']}"
)

# -----------------------------
# High Cost Resources
# -----------------------------

st.subheader("⚠️ High Cost Resources (> ₹10000)")

high_cost = df[df["Cost"] > 10000]

st.dataframe(
    high_cost[["Resource", "Cost"]]
)

# -----------------------------
# Bar Chart
# -----------------------------

st.subheader("📊 Cost Distribution")

fig = px.bar(
    df,
    x="Resource",
    y="Cost",
    color="Type",
    title="Cloud Resource Cost Breakdown"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# Pie Chart
# -----------------------------

st.subheader("🥧 Cost Share by Resource")

pie_fig = px.pie(
    df,
    names="Resource",
    values="Cost",
    title="Cost Percentage Distribution"
)

st.plotly_chart(
    pie_fig,
    use_container_width=True
)

# -----------------------------
# AI Recommendations
# -----------------------------

st.subheader("🤖 AI Cost Optimization Recommendations")

for _, row in df.iterrows():

    recommendation = generate_recommendation(
        row["Resource"],
        row["Type"],
        row["Cost"]
    )

    with st.expander(
        f"{row['Resource']} - ₹{row['Cost']}"
    ):
        st.write(recommendation)

# -----------------------------
# Cost Anomaly Detection
# -----------------------------

st.subheader("🚨 Cost Anomaly Alerts")

anomalies = detect_anomalies()

if anomalies:

    for anomaly in anomalies:

        st.error(
            f"""
Resource: {anomaly['Resource']}

Previous Cost: ₹{anomaly['Previous Cost']}

Current Cost: ₹{anomaly['Current Cost']}

Increase: {anomaly['Increase %']}%
"""
        )

else:
    st.success("No anomalies detected.")

# -----------------------------
# Footer
# -----------------------------

st.markdown("---")
st.caption(
    "AI Cloud Cost Detective | Azure + Python + Streamlit + FinOps"
)

st.subheader("☁️ Real Azure Cost Data")

try:

    azure_data = get_azure_cost_data()

    if azure_data:

        rows = azure_data["properties"]["rows"]

        azure_total = sum(
            row[0] for row in rows
        )

        st.metric(
            "Azure Month-To-Date Cost",
            f"₹{round(azure_total, 2)}"
        )

    else:

        st.warning(
            "Azure cost data unavailable."
        )

except Exception as e:

    st.error(
        f"Azure Error: {e}"
    )