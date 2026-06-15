import streamlit as st
import pandas as pd

# --- PAGE SETUP ---
st.set_page_config(page_title="Personal Monthly Budget", layout="wide")

# --- HEADER ---
st.title("Personal Monthly Budget | KPI Summary Dashboard")
st.subheader("Gregory | Southfield, MI · June 2026")

# --- INCOME & EXPENSE SUMMARY ---
income = 3710.76
expenses = 2840.55
surplus = income - expenses
annual_surplus = surplus * 12
savings_goal = 500.00
savings_rate = (surplus / income) * 100
expense_ratio = (expenses / income) * 100
surplus_vs_goal = surplus - savings_goal

# --- KPI METRICS ---
st.markdown("### KPI Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Monthly Income", f"${income:,.2f}")
col2.metric("Total Monthly Expenses", f"${expenses:,.2f}")
col3.metric("Monthly Net Surplus", f"${surplus:,.2f}", "✔ Surplus")
col4.metric("Savings Rate %", f"{savings_rate:.1f}%", "✔ Strong")

col5, col6, col7 = st.columns(3)
col5.metric("Expense Ratio %", f"{expense_ratio:.1f}%", "⚠ Watch")
col6.metric("Surplus vs Savings Goal", f"${surplus_vs_goal:,.2f}", "✔ On Track")
col7.metric("Annual Net Surplus", f"${annual_surplus:,.2f}")

# --- EXPENSE BREAKDOWN ---
st.markdown("### Expense Breakdown")
data = {
    "Category": ["Housing", "Utilities", "Food", "Transportation", "Healthcare", "Personal & Lifestyle", "Savings & Investments", "Debt Payments", "Other"],
    "Monthly ($)": [257.39, 517.39, 377.66, 149.70, 0.00, 55.96, 1482.45, 0.00, 0.00]
}
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

# --- KPI SUMMARY ---
st.markdown("### KPI Summary")
st.write(f"**Break-Even Date:** Day 23 of the month ⚠ Mid")
st.write(f"**Largest Expense Category:** Savings & Investments (${max(df['Monthly ($)']):,.2f})")

# --- TREND CHART ---
st.markdown("### Monthly Trend Data (12-Month Rolling View)")
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
income_trend = [income]*12
expense_trend = [expenses]*12
surplus_trend = [surplus]*12

trend_df = pd.DataFrame({
    "Month": months,
    "Income": income_trend,
    "Expenses": expense_trend,
    "Surplus": surplus_trend
})
st.line_chart(trend_df.set_index("Month"))

# --- FOOTER ---
st.caption("© 2026 Gregory | Southfield, MI")

