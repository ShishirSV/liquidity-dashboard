def score_cash_allocation(df, risk_level):
    if risk_level == "Low":
        return 30
    elif risk_level == "Medium":
        return 15
    return 5
