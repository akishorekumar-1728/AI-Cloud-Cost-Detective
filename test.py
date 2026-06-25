from recommendations import generate_recommendation

result = generate_recommendation(
    "AKS-Cluster",
    "Kubernetes",
    25000
)

print(result)