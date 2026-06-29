import uuid
from faker import Faker
import random
import pandas as pd

fake = Faker("en_IN")

customers = []


for i in range(500):
    monthly = random.randint(300, 2500)
    tenure = random.randint(1, 72)

    customers.append({
        "customer_code": str(uuid.uuid4())[:20],
        "full_name": fake.name(),
        "gender": random.choice(["Male", "Female"]),
        "age": random.randint(18, 70),
        "phone": fake.phone_number(),
        "email": fake.email(),
        "city": fake.city(),
        "state": fake.state(),
        "contract_type": random.choice([
            "Month-to-month",
            "One Year",
            "Two Year"
        ]),
        "internet_service": random.choice([
            "Fiber",
            "DSL",
            "Cable"
        ]),
        "payment_method": random.choice([
            "Credit Card",
            "Debit Card",
            "UPI",
            "Net Banking"
        ]),
        "tenure_months": tenure,
        "monthly_charges": monthly,
        "total_charges": monthly * tenure,
        "customer_status": random.choice([
            "Active",
            "Churned"
        ])
    })
df = pd.DataFrame(customers)

if __name__ == "__main__":
    print(df.head())
    print(f"\nTotal Customers Generated: {len(df)}")

print(df["customer_code"].head())
def generate_customers():
    return df