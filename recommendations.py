def generate_recommendation(resource, resource_type, cost):

    if cost > 20000:
        return """
Problem:
Very high monthly cost.

Recommendation:
- Enable Autoscaling
- Use Spot Instances
- Remove Idle Resources
- Rightsize Compute Resources

Estimated Savings:
20-30%
"""

    elif cost > 10000:
        return """
Problem:
Moderately high monthly cost.

Recommendation:
- Review resource utilization
- Enable cost monitoring
- Optimize storage usage

Estimated Savings:
10-15%
"""

    else:
        return """
Problem:
Cost is within normal range.

Recommendation:
Continue monitoring resource usage.

Estimated Savings:
Minimal
"""