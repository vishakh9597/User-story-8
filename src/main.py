import logging
from loader import load_csv
from usage_aggregator import aggregate_usage
from billing_engine import calculate_bill
from status_engine import evaluate_status
from reporter import write_billing_output, write_summary

logging.basicConfig(
    filename="logs/billing.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    subscriptions = load_csv("data/subscriptions.csv")
    usage_records = load_csv("data/usage.csv")

    usage_map = aggregate_usage(usage_records)

    output_records = []

    for sub in subscriptions:
        if sub["status"] == "CANCELLED":
            usage = 0
        else:
            usage = usage_map.get(sub["subscription_id"], 0)

        total_bill, overage = calculate_bill(
            sub["status"],
            sub["monthly_fee"],
            usage,
            sub["usage_limit_gb"]
        )

        final_status = evaluate_status(
            sub["status"],
            usage,
            sub["usage_limit_gb"]
        )

        output_records.append({
            "subscription_id": sub["subscription_id"],
            "customer_id": sub["customer_id"],
            "plan": sub["plan"],
            "total_usage_gb": usage,
            "overage_gb": overage,
            "total_bill": total_bill,
            "final_status": final_status
        })

    write_billing_output("billing_output.csv", output_records)
    write_summary("billing_summary.json", output_records)

if __name__ == "__main__":
    main()