import csv
import json

def write_billing_output(file_path, records):
    fieldnames = [
        "subscription_id",
        "customer_id",
        "plan",
        "total_usage_gb",
        "overage_gb",
        "total_bill",
        "final_status"
    ]

    with open(file_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)


def write_summary(file_path, records):
    total_subscriptions = len(records)
    active = sum(1 for r in records if r["final_status"] == "ACTIVE")
    suspended = sum(1 for r in records if r["final_status"] == "SUSPENDED")
    cancelled = sum(1 for r in records if r["final_status"] == "CANCELLED")
    total_revenue = sum(float(r["total_bill"]) for r in records)
    average_bill = total_revenue / total_subscriptions if total_subscriptions else 0

    summary = {
        "total_subscriptions": total_subscriptions,
        "active_subscriptions": active,
        "suspended_subscriptions": suspended,
        "cancelled_subscriptions": cancelled,
        "total_revenue": total_revenue,
        "average_bill": average_bill
    }

    with open(file_path, "w") as f:
        json.dump(summary, f, indent=4)