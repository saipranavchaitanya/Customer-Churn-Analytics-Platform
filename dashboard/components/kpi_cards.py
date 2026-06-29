import streamlit as st

def show_kpis(df):

    total = len(df)

    active = len(df[df["customer_status"]=="Active"])

    churn = len(df[df["customer_status"]=="Churned"])

    revenue = df["total_charges"].sum()

    churn_rate = round((churn/total)*100,2)

    c1,c2,c3,c4,c5 = st.columns(5)

    c1.metric("Customers",total)

    c2.metric("Active",active)

    c3.metric("Churned",churn)

    c4.metric("Revenue",f"₹{revenue:,.0f}")

    c5.metric("Churn Rate",f"{churn_rate}%")