-- FUND DIMENSION

CREATE TABLE IF NOT EXISTS dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    plan TEXT
);


-- DATE DIMENSION
CREATE TABLE IF NOT EXISTS dim_Date(
    date_id INTEGER PRIMARY KEY,
    full_date DATE,
    year INTEGER,
    quarter INTEGER,
    month INTEGER,
    day INTEGER
);


-- NAV FACT

CREATE TABLE IF NOT EXISTS fact_nav (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    nav_date DATE,
    nav REAL,

    FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code)
);


-- TRANSACTIONS FACT

CREATE TABLE IF NOT EXISTS fact_transactions ( 
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    investor_id TEXT,
    transaction_date DATE,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    kyc_status TEXT,

    FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code)
);


-- PERFORMANCE FACT

CREATE TABLE IF NOT EXISTS fact_performance ( 
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,

    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,

    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,
    expense_ratio_pct REAL,

    FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code)
);


-- AUM FACT


CREATE TABLE IF NOT EXISTS fact_aum (
    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,

    aum_date DATE,
    fund_house TEXT,

    aum_lakh_crore REAL,
    aum_crore REAL,
    num_schemes INTEGER
);