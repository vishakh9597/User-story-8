from datetime import datetime
import logging

logger = logging.getLogger(__name__)

MARCH_2024_START = datetime(2024, 3, 1)
MARCH_2024_END = datetime(2024, 3, 31)

def aggregate_usage(usage_records):
    usage_map = {}

    for record in usage_records:
        sub_id = record.get("subscription_id")
        date_str = record.get("usage_date")
        data_used = record.get("data_used_gb", 0)

        try:
            usage_date = datetime.strptime(date_str, "%Y-%m-%d")
        except Exception:
            logger.warning(f"Invalid date skipped: {date_str}")
            continue

        if not (MARCH_2024_START <= usage_date <= MARCH_2024_END):
            continue

        try:
            data_used = float(data_used)
        except:
            logger.warning(f"Invalid usage value defaulted to 0 for {sub_id}")
            data_used = 0

        usage_map[sub_id] = usage_map.get(sub_id, 0) + data_used

    return usage_map