# Data Dictionary

## Project

Mutual Fund Analytics Dashboard

## Database

bluestock_mf.db

---

# fact_nav

Stores historical Net Asset Value (NAV) records for mutual fund schemes.

| Column    | Data Type | Business Definition           |
| --------- | --------- | ----------------------------- |
| amfi_code | INTEGER   | Unique AMFI scheme identifier |
| date      | DATE      | NAV date                      |
| nav       | REAL      | Net Asset Value of scheme     |

Source: nav_history_clean.csv

---

# fact_transactions

Stores investor transaction records.

| Column             | Data Type | Business Definition           |
| ------------------ | --------- | ----------------------------- |
| investor_id        | TEXT      | Unique investor identifier    |
| transaction_date   | DATE      | Date of transaction           |
| amfi_code          | INTEGER   | Mutual fund scheme identifier |
| transaction_type   | TEXT      | SIP, Lumpsum, or Redemption   |
| amount_inr         | REAL      | Transaction amount in INR     |
| state              | TEXT      | Investor state                |
| city               | TEXT      | Investor city                 |
| city_tier          | TEXT      | T30/B30 city classification   |
| age_group          | TEXT      | Investor age segment          |
| gender             | TEXT      | Investor gender               |
| annual_income_lakh | REAL      | Annual income in lakhs        |

Source: investor_transactions_clean.csv

---

# fact_performance

Stores mutual fund performance metrics.

| Column         | Data Type | Business Definition           |
| -------------- | --------- | ----------------------------- |
| amfi_code      | INTEGER   | Mutual fund scheme identifier |
| scheme_name    | TEXT      | Name of scheme                |
| fund_house     | TEXT      | Asset management company      |
| category       | TEXT      | Scheme category               |
| plan           | TEXT      | Direct or Regular plan        |
| return_1yr_pct | REAL      | One year return percentage    |
| return_3yr_pct | REAL      | Three year return percentage  |
| return_5yr_pct | REAL      | Five year return percentage   |
| expense_ratio  | REAL      | Expense ratio percentage      |

Source: scheme_performance_clean.csv

---

# fact_aum

Stores Assets Under Management values.

| Column      | Data Type | Business Definition               |
| ----------- | --------- | --------------------------------- |
| amfi_code   | INTEGER   | Mutual fund scheme identifier     |
| scheme_name | TEXT      | Scheme name                       |
| aum_cr      | REAL      | Assets Under Management in Crores |

Source: AUM dataset

---

# dim_fund

Dimension table containing fund details.

| Column      | Data Type | Business Definition       |
| ----------- | --------- | ------------------------- |
| amfi_code   | INTEGER   | Primary scheme identifier |
| scheme_name | TEXT      | Mutual fund scheme name   |
| fund_house  | TEXT      | Asset management company  |
| category    | TEXT      | Fund category             |
| plan        | TEXT      | Direct or Regular         |

Source: scheme_performance_clean.csv

---

# dim_date

Calendar dimension.

| Column     | Data Type | Business Definition |
| ---------- | --------- | ------------------- |
| date_key   | INTEGER   | YYYYMMDD date key   |
| date       | DATE      | Calendar date       |
| year       | INTEGER   | Calendar year       |
| quarter    | INTEGER   | Quarter of year     |
| month      | INTEGER   | Month number        |
| month_name | TEXT      | Month name          |
| day        | INTEGER   | Day of month        |

Generated from transaction and NAV dates.

---

# Relationships

fact_nav.amfi_code → dim_fund.amfi_code

fact_transactions.amfi_code → dim_fund.amfi_code

fact_performance.amfi_code → dim_fund.amfi_code

fact_aum.amfi_code → dim_fund.amfi_code

fact_nav.date → dim_date.date

fact_transactions.transaction_date → dim_date.date

---

# Author

Bluestock Fintech Internship Project
