import pandas as pd

# Read CSV
df = pd.read_csv("data/sample_cost.csv")

print("\n===== Cloud Cost Data =====")
print(df)

# Total Monthly Cost
total_cost = df["Cost"].sum()

# Most Expensive Resource
highest_resource = df.loc[df["Cost"].idxmax()]

# High Cost Resources (>10000)
high_cost_resources = df[df["Cost"] > 10000]

print("\n===== Cost Summary =====")
print(f"Total Monthly Cost: ₹{total_cost}")

print("\nMost Expensive Resource:")
print(f"{highest_resource['Resource']} - ₹{highest_resource['Cost']}")

print("\nHigh Cost Resources (> ₹10000):")
print(high_cost_resources[["Resource", "Cost"]])