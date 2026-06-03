# Mutual Fund Analytics Data Dictionary

## dim_fund

| Column | Type | Description |
|----------|----------|-------------|
| amfi_code | INTEGER | Unique fund identifier |
| scheme_name | TEXT | Mutual fund scheme name |
| fund_house | TEXT | AMC name |
| category | TEXT | Fund category |

---

## dim_date

| Column | Type | Description |
|----------|----------|-------------|
| date | DATE | Calendar date |
| year | INTEGER | Year |
| month | INTEGER | Month number |
| quarter | INTEGER | Quarter number |

---

## fact_nav

| Column | Type | Description |
|----------|----------|-------------|
| nav_id | INTEGER | Primary key |
| amfi_code | INTEGER | Fund identifier |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

---

## fact_transactions

| Column | Type | Description |
|----------|----------|-------------|
| transaction_id | INTEGER | Primary key |
| investor_id | INTEGER | Investor identifier |
| amfi_code | INTEGER | Fund identifier |
| transaction_date | DATE | Transaction date |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | REAL | Transaction amount in INR |
| state | TEXT | Investor state |
| kyc_status | TEXT | KYC verification status |

---

## fact_performance

| Column | Type | Description |
|----------|----------|-------------|
| performance_id | INTEGER | Primary key |
| amfi_code | INTEGER | Fund identifier |
| return_1yr_pct | REAL | 1-year return (%) |
| return_3yr_pct | REAL | 3-year return (%) |
| return_5yr_pct | REAL | 5-year return (%) |
| expense_ratio | REAL | Expense ratio (%) |

---

## fact_aum

| Column | Type | Description |
|----------|----------|-------------|
| aum_id | INTEGER | Primary key |
| aum_date | DATE | AUM reporting date |
| fund_house | TEXT | Asset Management Company |
| aum_lakh_crore | REAL | AUM in lakh crore |
| aum_crore | REAL | AUM in crore |
| num_schemes | INTEGER | Number of schemes |

---

## Source Files

| Source File | Target Table |
|------------|-------------|
| nav_history.csv | fact_nav |
| investor_transactions.csv | fact_transactions |
| scheme_performance.csv | fact_performance |
| monthly_aum.csv | fact_aum |