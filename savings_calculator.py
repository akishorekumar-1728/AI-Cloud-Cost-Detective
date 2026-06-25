def calculate_savings(total_cost):

    savings_percent = 0.20  # 20%

    savings = total_cost * savings_percent

    optimized_cost = total_cost - savings

    return {
        "savings": round(savings, 2),
        "optimized_cost": round(optimized_cost, 2)
    }