from etl.load_customers import load_customers

print("=" * 50)
print("CUSTOMER CHURN ETL PIPELINE")
print("=" * 50)

print("Step 1 : Generating Customers...")

records = load_customers()

print(f"Step 2 : {records} Customers Loaded")

print("Pipeline Completed Successfully!")