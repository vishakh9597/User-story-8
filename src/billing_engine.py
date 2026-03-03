def calculate_bill(status, monthly_fee, usage, usage_limit):
    monthly_fee = float(monthly_fee)
    usage_limit = float(usage_limit)

    if status == "CANCELLED":
        return 0, 0

    if status == "SUSPENDED":
        return monthly_fee, 0

    if usage <= usage_limit:
        return monthly_fee, 0

    overage = usage - usage_limit
    overage_charge = overage * 10
    total_bill = monthly_fee + overage_charge

    return total_bill, overage