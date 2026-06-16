import streamlit as st
import pandas as pd

# 1. Base App Settings
st.set_page_config(page_title="Personal Monthly Budget", layout="wide")

# 2. Secure API & Link Retrieval 
# Pulls your Stripe Secret Key out of sight from the front-end client
stripe_key = st.secrets["STRIPE_API_KEY"]

# Replace this with your actual Stripe Payment Link URL from your dashboard
#STRIPE_PAYMENT_LINK = "https://buy.stripe.com/your_actual_link_here"
STRIPE_PAYMENT_LINK = "https://buy.stripe.com/test_dRm3cx4YKcNs6yG2tP7Zu00"
# 3. Router logic: Check the URL parameters for access validation
if st.query_params.get("payment") == "success":
    
    # =========================================================================
    # --- SUCCESS STATE: USER PAID -> SHOW FULL DASHBOARD ---
    # =========================================================================
    st.success("🎉 Access Granted! Welcome to your Workspace.")
    
    # Optional logout option allowing users to reset parameters manually
    if st.button("Log Out / Re-lock Dashboard"):
        st.query_params.clear()
        st.rerun()
        
    st.title("Personal Monthly Budget | KPI Summary Dashboard")
    st.subheader("Gregory | Southfield, MI • June 2026")
    
    st.markdown("### KPI Metrics")
    
    # Core Dashboard Math & Variables
    income = 3710.76
    expenses = 2840.55
    surplus = income - expenses
    savings_goal = 500.00
    
    savings_ratio = (surplus / income) * 100
    expense_ratio = (expenses / income) * 100
    surplus_vs_goal = surplus - savings_goal
    annual_surplus = surplus * 12
    
    # Layout Structure: Metric Columns
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Total Monthly Income", value=f"${income:,.2f}")
    with col2:
        st.metric(label="Total Monthly Expenses", value=f"${expenses:,.2f}")
    with col3:
        st.metric(label="Monthly Net Surplus", value=f"${surplus:,.2f}", delta="↑ Surplus", delta_color="normal")
    with col4:
        st.metric(label="Savings Rate %", value=f"{savings_ratio:.1f}%", delta="↑ Strong", delta_color="normal")
        
    col5, col6, col7 = st.columns(3)
    with col5:
        st.metric(label="Expense Ratio %", value=f"{expense_ratio:.1f}%", delta="↓ Watch", delta_color="inverse")
    with col6:
        st.metric(label="Surplus vs Savings Goal", value=f"${surplus_vs_goal:,.2f}", delta="↑ On Track", delta_color="normal")
    with col7:
        st.metric(label="Annual Net Surplus", value=f"${annual_surplus:,.2f}")
        
    st.markdown("---")
    st.markdown("### Expense Breakdown")
    
    # Dataframe Table Layout
    expense_data = {
        "Category": ["Housing", "Utilities", "Food", "Transportation", "Healthcare", "Personal & Lifestyle"],
        "Monthly ($)": [257.39, 517.39, 377.66, 149.70, 0.00, 0.00]
    }
    df = pd.DataFrame(expense_data)
    st.dataframe(df, use_container_width=True, hide_index=True)

else:
    # =========================================================================
    # --- LOCKED STATE: RENDER FRONT PAGE SPLASH SCREEN ---
    # =========================================================================
    st.write("") # Spacer
    st.markdown("<h1 style='text-align: center;'>🔒 Unlock Dynamic Budget Tracker</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Gain full access to the interactive budget dashboard for a one-time unlock.</p>", unsafe_allow_html=True)
    
    # Clean Pricing Card Component
    st.info("💳 **Price:** $2.99 USD")
    
    # Full Width Purchase Link Button Redirecting securely to Stripe
    st.link_button(
        "Buy Now & Unlock", 
        STRIPE_PAYMENT_LINK, 
        type="primary", 
        use_container_width=True
    )
