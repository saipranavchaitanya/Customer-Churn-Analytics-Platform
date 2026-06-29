import pandas as pd

def transform_customers(df):

    # Full Name
    df["full_name"] = df["full_name"].str.title().str.strip()

    # Email
    df["email"] = df["email"].str.lower().str.strip()

    # Customer Status
    df["customer_status"] = df["customer_status"].str.title()

    # Contract Type
    df["contract_type"] = df["contract_type"].str.title()

    # Internet Service
    df["internet_service"] = df["internet_service"].str.title()

    # Payment Method
    df["payment_method"] = df["payment_method"].str.title()

    # Monthly Charges
    df["monthly_charges"] = df["monthly_charges"].round(2)

    # Total Charges
    df["total_charges"] = df["total_charges"].round(2)

    # Tenure Group
    def tenure_group(x):
        if x <= 12:
            return "0-12 Months"
        elif x <= 24:
            return "13-24 Months"
        elif x <= 48:
            return "25-48 Months"
        else:
            return "49-72 Months"

    df["tenure_group"] = df["tenure_months"].apply(tenure_group)

    # Churn Flag
    df["churn_flag"] = df["customer_status"].apply(
        lambda x: 1 if x == "Churned" else 0
    )

    return df