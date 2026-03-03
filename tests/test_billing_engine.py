import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from src.billing_engine import calculate_bill

class TestBillingEngine(unittest.TestCase):

    def test_bill_without_overage(self):
        bill, overage = calculate_bill("ACTIVE", 100, 50, 100)
        self.assertEqual(bill, 100)
        self.assertEqual(overage, 0)

    def test_bill_with_overage(self):
        bill, overage = calculate_bill("ACTIVE", 100, 150, 100)
        self.assertEqual(bill, 600)
        self.assertEqual(overage, 50)

    def test_suspended_subscription_billing(self):
        bill, overage = calculate_bill("SUSPENDED", 100, 200, 100)
        self.assertEqual(bill, 100)
        self.assertEqual(overage, 0)

    def test_cancelled_subscription_billing(self):
        bill, overage = calculate_bill("CANCELLED", 100, 200, 100)
        self.assertEqual(bill, 0)


if __name__ == "__main__":
    unittest.main()