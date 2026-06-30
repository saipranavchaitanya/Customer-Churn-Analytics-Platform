import streamlit as st

def card(icon, title, value, color):

    st.markdown(f"""
    <div class="kpi-card">

        <div class="kpi-icon" style="background:{color};">
            {icon}
        </div>

        <div class="kpi-title">
            {title}
        </div>

        <div class="kpi-value">
            {value}
        </div>

    </div>
    """, unsafe_allow_html=True)


def show_kpis(df):

    total = len(df)

    active = len(df[df["customer_status"]=="Active"])

    churn = len(df[df["customer_status"]=="Churned"])

    revenue = df["total_charges"].sum()

    churn_rate = round((churn/total)*100,2)

    c1,c2,c3,c4,c5 = st.columns(5)

    with c1:
        card("👥","Customers",f"{total:,}","#3B82F6")

    with c2:
        card("✅","Active",f"{active:,}","#22C55E")

    with c3:
        card("❌","Churned",f"{churn:,}","#EF4444")

    with c4:
        card("💰","Revenue",f"₹{revenue:,.0f}","#F59E0B")

    with c5:
        card("📈","Churn Rate",f"{churn_rate}%","#8B5CF6")