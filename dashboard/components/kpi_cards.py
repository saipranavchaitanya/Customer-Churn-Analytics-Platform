import streamlit as st

def show_kpis(df):
    total = len(df)

    active = len(df[df["customer_status"] == "Active"])

    churn = len(df[df["customer_status"] == "Churned"])

    revenue = df["total_charges"].sum()

    churn_rate = round((churn / total) * 100, 2) if total > 0 else 0

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.metric(
            label="👥 Customers",
            value=f"{total:,}"
        )

    with c2:
        st.metric(
            label="✅ Active",
            value=f"{active:,}"
        )

    with c3:
        st.metric(
            label="❌ Churned",
            value=f"{churn:,}"
        )

    with c4:
        st.metric(
            label="💰 Revenue",
            value=f"₹{revenue:,.0f}"
        )

    with c5:
        st.metric(
            label="📈 Churn Rate",
            value=f"{churn_rate}%"
        )