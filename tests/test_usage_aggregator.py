import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from src.usage_aggregator import aggregate_usage

class TestUsageAggregator(unittest.TestCase):

    def test_multiple_usage_records(self):
        records = [
            {"subscription_id": "1", "usage_date": "2024-03-10", "data_used_gb": "10"},
            {"subscription_id": "1", "usage_date": "2024-03-15", "data_used_gb": "20"},
        ]
        result = aggregate_usage(records)
        self.assertEqual(result["1"], 30)

    def test_no_usage_records(self):
        result = aggregate_usage([])
        self.assertEqual(result, {})

    def test_invalid_usage_dates(self):
        records = [
            {"subscription_id": "1", "usage_date": "invalid", "data_used_gb": "10"},
        ]
        result = aggregate_usage(records)
        self.assertEqual(result, {})


if __name__ == "__main__":
    unittest.main()