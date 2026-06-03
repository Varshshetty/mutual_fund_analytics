import streamlit as st
import pandas as pd
import sqlite3
st.set_page_config(
    page_title="Mutual Fund Analytics",
    layout="wide"
)

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
db_path = BASE_DIR / "bluestock_mf.db"
conn = sqlite3.connect(db_path)

st.title("📈 Mutual Fund Analytics Dashboard")


# -----------------------------
# Database Connection
# -----------------------------

categories = pd.read_sql(
    "SELECT DISTINCT category FROM fact_performance",
    conn
)

selected_category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + categories["category"].tolist()
)

if selected_category == "All":
    where_clause = ""
else:
    where_clause = f"WHERE category = '{selected_category}'"
# -----------------------------
# KPI Queries
# -----------------------------
nav_count = pd.read_sql(
    "SELECT COUNT(*) as total FROM fact_nav",
    conn
)

performance_count = pd.read_sql(
    "SELECT COUNT(*) as total FROM fact_performance",
    conn
)

transaction_count = pd.read_sql(
    "SELECT COUNT(*) as total FROM fact_transactions",
    conn
)

# -----------------------------
# KPI Cards
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div style="
        padding:20px;
        border-radius:10px;
        background-color:#1f77b4;
        color:white;
        text-align:center;">
        <h3>NAV Records</h3>
        <h1>{nav_count['total'][0]:,}</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="
        padding:20px;
        border-radius:10px;
        background-color:#2ca02c;
        color:white;
        text-align:center;">
        <h3>Performance Records</h3>
        <h1>{performance_count['total'][0]:,}</h1>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style="
        padding:20px;
        border-radius:10px;
        background-color:#ff7f0e;
        color:white;
        text-align:center;">
        <h3>Transaction Records</h3>
        <h1>{transaction_count['total'][0]:,}</h1>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# Data Preview
# -----------------------------
st.divider()

st.subheader("Data Preview (NAV Table)")

nav_df = pd.read_sql(
    "SELECT * FROM fact_nav LIMIT 10",
    conn
)

st.dataframe(nav_df, use_container_width=True)

# ----------------------------
# Performance Preview
# ----------------------------
st.divider()

st.subheader("Performance Data")

performance_df = pd.read_sql(
    f"""
    SELECT *
    FROM fact_performance
    {where_clause}
    LIMIT 10
    """,
    conn
)

st.dataframe(performance_df, use_container_width=True)

# -----------------------------
# Transaction Preview
# -----------------------------
st.subheader("Transaction Data")

transaction_df = pd.read_sql(
    "SELECT * FROM fact_transactions LIMIT 10",
    conn
)

st.dataframe(transaction_df, use_container_width=True)

st.divider()

st.subheader("Transaction Type Distribution")

tx_chart = pd.read_sql("""
SELECT transaction_type,
       COUNT(*) as total
FROM fact_transactions
GROUP BY transaction_type
""", conn)

st.bar_chart(
    tx_chart.set_index("transaction_type")
)

st.divider()

st.subheader("Top Categories by Average Return")

cat_chart = pd.read_sql("""
SELECT category,
       AVG(return_1yr_pct) as avg_return
FROM fact_performance
GROUP BY category
ORDER BY avg_return DESC
""", conn)

st.bar_chart(
    cat_chart.set_index("category")
)

st.divider()

st.subheader("Fund House Distribution")

fund_house_df = pd.read_sql("""
SELECT fund_house,
       COUNT(*) as total_funds
FROM fact_performance
GROUP BY fund_house
ORDER BY total_funds DESC
""", conn)

st.bar_chart(
    fund_house_df.set_index("fund_house")
)

st.divider()

st.subheader("State-wise Investment Amount")

state_df = pd.read_sql("""
SELECT state,
       SUM(amount_inr) as total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC
""", conn)

st.bar_chart(
    state_df.set_index("state")
)

st.divider()

st.subheader("Average Return by Fund House")
return_df = pd.read_sql(
    f"""
    SELECT fund_house,
           AVG(return_1yr_pct) as avg_return
    FROM fact_performance
    {where_clause}
    GROUP BY fund_house
    ORDER BY avg_return DESC
    """,
    conn
)

st.bar_chart(
    return_df.set_index("fund_house")
)
# -----------------------------
# Close Connection
# -----------------------------
conn.close()


