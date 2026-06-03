-- =====================================================
-- Query 1: Top 5 Funds by AUM
-- =====================================================

SELECT
    scheme_name,
    aum_cr
FROM fact_aum
ORDER BY aum_cr DESC
LIMIT 5;


-- =====================================================
-- Query 2: Average NAV per Month
-- =====================================================

SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- =====================================================
-- Query 3: SIP Transactions Year-over-Year
-- =====================================================

SELECT
    strftime('%Y', transaction_date) AS year,
    COUNT(*) AS sip_count
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;


-- =====================================================
-- Query 4: Transactions by State
-- =====================================================

SELECT
    state,
    COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY state
ORDER BY transaction_count DESC;


-- =====================================================
-- Query 5: Funds with Expense Ratio < 1%
-- =====================================================

SELECT
    scheme_name,
    expense_ratio
FROM fact_performance
WHERE expense_ratio < 1
ORDER BY expense_ratio;


-- =====================================================
-- Query 6: Top States by Investment Amount
-- =====================================================

SELECT
    state,
    SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC
LIMIT 10;


-- =====================================================
-- Query 7: Average Return by Category
-- =====================================================

SELECT
    category,
    ROUND(AVG(return_1yr_pct),2) AS avg_return
FROM fact_performance
GROUP BY category
ORDER BY avg_return DESC;


-- =====================================================
-- Query 8: Top Fund Houses by Average Return
-- =====================================================

SELECT
    fund_house,
    ROUND(AVG(return_1yr_pct),2) AS avg_return
FROM fact_performance
GROUP BY fund_house
ORDER BY avg_return DESC;


-- =====================================================
-- Query 9: Redemption Amount by State
-- =====================================================

SELECT
    state,
    SUM(amount_inr) AS redemption_amount
FROM fact_transactions
WHERE transaction_type = 'Redemption'
GROUP BY state
ORDER BY redemption_amount DESC;


-- =====================================================
-- Query 10: Best Performing Funds (5 Year Return)
-- =====================================================

SELECT
    scheme_name,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;