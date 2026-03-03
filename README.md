# UserStory8
# Subscription Billing & Status Evaluation Engine

## Project Overview

This project implements a **Subscription Billing & Status Evaluation Engine** in Python.

The system processes subscription and usage data for March 2024, applies business rules, calculates billing amounts, evaluates final subscription statuses, and generates structured billing reports.

##  Project Structure
```
project/
├── data/
│   ├── subscriptions.csv
│   └── usage.csv
│
├── src/
│   ├── loader.py
│   ├── usage_aggregator.py
│   ├── billing_engine.py
│   ├── status_engine.py
│   ├── reporter.py
│   └── main.py
│
├── tests/
│   ├── test_billing_engine.py
│   ├── test_status_engine.py
│   └── test_usage_aggregator.py
│
├── logs/
│   └── billing.log
│
├── billing_output.csv
├── billing_summary.json
└── README.md
```
---

## Input Files

### 1️subscriptions.csv

| Column | Description |
|---------|-------------|
| subscription_id | Unique subscription ID |
| customer_id | Customer identifier |
| plan | Plan name |
| monthly_fee | Monthly subscription fee |
| usage_limit_gb | Monthly usage limit |
| status | ACTIVE, SUSPENDED, CANCELLED |
| start_date | Subscription start date |
| end_date | Optional end date |

---

### 2️usage.csv

| Column | Description |
|---------|-------------|
| subscription_id | Subscription ID |
| usage_date | Date of usage (YYYY-MM-DD) |
| data_used_gb | Data usage in GB |

---

## Processing Scope

- Only usage for **March 2024** is considered
- CANCELLED subscriptions are not billed
- Subscriptions with no usage assume usage = 0
- Invalid records are skipped and logged
- Application must not crash due to bad data

---

## Business Rules

### 1️Usage Aggregation
- Aggregate total usage per subscription
- Ignore invalid date formats
- Consider only March 2024

---

### Billing Rules

If:
- usage ≤ usage_limit → total_bill = monthly_fee
- usage > usage_limit →  
  overage = usage - limit  
  overage_charge = overage × 10  
  total_bill = monthly_fee + overage_charge
- status = SUSPENDED → bill only monthly_fee
- status = CANCELLED → bill = 0

---

### Status Evaluation Rules

- If usage > 150% of limit → final_status = SUSPENDED
- If previous status was SUSPENDED and usage ≤ limit → final_status = ACTIVE
- CANCELLED status never changes

---

## Output Files

### billing_output.csv

| Column | Description |
|---------|-------------|
| subscription_id |
| customer_id |
| plan |
| total_usage_gb |
| overage_gb |
| total_bill |
| final_status |

---

### billing_summary.json

Contains:

- total_subscriptions
- active_subscriptions
- suspended_subscriptions
- cancelled_subscriptions
- total_revenue
- average_bill

---

## Logging

- Uses Python `logging` module
- Logs stored in:

## Unit Test Coverage

The project includes tests for:

Billing Logic

- test_bill_without_overage

- test_bill_with_overage

- test_suspended_subscription_billing

- test_cancelled_subscription_billing

Status Evaluation

- test_active_to_suspended_transition

- test_suspended_to_active_transition

- test_cancelled_status_unchanged

Usage Aggregation

- test_multiple_usage_records

- test_no_usage_records

- test_invalid_usage_dates

All tests pass successfully.

## Error Handling & Edge Cases Covered

- Missing numeric values default to 0

- Invalid dates skipped safely

- Missing usage records handled

- CANCELLED subscriptions not billed

- No crash on malformed records

- Empty input files handled

## Assumptions Made

- Input date format is YYYY-MM-DD

- Only March 2024 billing is required

- monthly_fee and usage_limit_gb are numeric

- Subscription status values are uppercase

- Usage overage cost is fixed at 10 per GB# User-story-8
