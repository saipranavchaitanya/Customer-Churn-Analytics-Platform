import pandas as pd

def validate_customers(df):

    valid_rows = []
    invalid_rows = []

    for _, row in df.iterrows():

        errors = []

        if row["age"] < 18 or row["age"] > 70:
            errors.append("Invalid Age")

        if row["monthly_charges"] <= 0:
            errors.append("Invalid Monthly Charges")

        if pd.isna(row["email"]) or row["email"] == "":
            errors.append("Missing Email")

        if pd.isna(row["customer_code"]) or row["customer_code"] == "":
            errors.append("Missing Customer Code")

        if errors:
            row["error_message"] = ", ".join(errors)
            invalid_rows.append(row)
        else:
            valid_rows.append(row)

    valid_df = pd.DataFrame(valid_rows)
    invalid_df = pd.DataFrame(invalid_rows)

    return valid_df, invalid_df