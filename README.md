# 🚀 Customer Churn Analytics Platform

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-red?logo=streamlit)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase-green?logo=postgresql)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automated-success?logo=githubactions)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

</p>

An **End-to-End Customer Churn Analytics Platform** built using **Python, PostgreSQL (Supabase), Streamlit, SQLAlchemy, Plotly, and GitHub Actions**.

This project demonstrates a complete **Data Engineering + Data Analytics** workflow—from synthetic customer data generation to ETL automation, cloud database integration, and interactive business dashboards.

---

# 🌐 Live Demo

## 🚀 Streamlit Dashboard

**Live Application**

👉 **https://customer-churn-analytics-project.streamlit.app/**

---

## 📂 GitHub Repository

👉 **https://github.com/saipranavchaitanya/Customer-Churn-Analytics-Platform**

---

# 📌 Project Overview

Customer churn is one of the most important business metrics for telecom and subscription-based companies.

This platform automates the complete analytics workflow by:

* Generating realistic customer data using Faker
* Cleaning and transforming customer information
* Validating records before loading
* Loading data into PostgreSQL (Supabase)
* Monitoring ETL execution
* Visualizing business KPIs
* Running the ETL pipeline automatically every day using GitHub Actions

---

# 🏗 Project Architecture

```
GitHub Actions (Daily Scheduler)
          │
          ▼
Python Data Generator (Faker)
          │
          ▼
Transformation Layer
          │
          ▼
Validation Layer
          │
          ▼
PostgreSQL (Supabase)
          │
          ▼
Streamlit Dashboard
          │
 ├── Home Dashboard
 ├── Customer Dashboard
 ├── Churn Dashboard
 ├── ETL Monitor
 ├── Pipeline Logs
 └── Error Logs
```

---

# 📂 Project Structure

```
Customer-Churn-Analytics-Platform/
│
├── config/
│   └── database.py
│
├── generator/
│   └── generate_customers.py
│
├── transformation/
│   └── transform_customers.py
│
├── validation/
│   └── validate_customers.py
│
├── etl/
│   └── load_customers.py
│
├── etl_logging/
│   └── etl_logger.py
│
├── dashboard/
│   ├── Home.py
│   ├── db.py
│   ├── pages/
│   ├── charts/
│   └── components/
│
├── run_pipeline.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Tech Stack

### Programming

* Python

### Database

* PostgreSQL (Supabase)

### Data Processing

* Pandas
* NumPy
* Faker

### ETL

* SQLAlchemy

### Dashboard

* Streamlit
* Plotly

### Automation

* GitHub Actions

### Version Control

* Git
* GitHub

---

# ✨ Features

## Automated ETL Pipeline

* Customer Data Generation
* Data Cleaning
* Data Transformation
* Data Validation
* PostgreSQL Loading
* ETL Logging
* Error Logging

---

## Customer Dashboard

* Total Customers
* Active Customers
* Churn Customers
* Monthly Revenue
* Customer Distribution
* Contract Analysis
* Internet Service Analysis

---

## Churn Dashboard

* Churn Rate
* Churn by Contract
* Churn by Internet Service
* Churn by Gender
* Churn by State

---

## ETL Monitor

* Pipeline Status
* Records Loaded
* Execution Time
* Daily Pipeline History

---

## Pipeline Logs

* Successful Runs
* Failed Runs
* Records Loaded
* Execution Time

---

## Error Logs

* Validation Errors
* Invalid Records
* Data Quality Monitoring

---

# 📊 Dashboard Pages

* 🏠 Home Dashboard
* 👥 Customer Dashboard
* 📉 Churn Dashboard
* ⚙️ ETL Monitor
* 📄 Pipeline Logs
* ❌ Error Logs

---

# 📈 Visualizations

* KPI Cards
* Pie Charts
* Bar Charts
* Line Charts
* State-wise Analysis
* Interactive Filters

---

# 🔄 ETL Workflow

1. Generate Customer Data
2. Transform Data
3. Validate Data
4. Load into PostgreSQL
5. Store ETL Logs
6. Update Streamlit Dashboard

---

# ☁️ Cloud Components

* GitHub Repository
* GitHub Actions
* PostgreSQL (Supabase)
* Streamlit Community Cloud

---

# 🤖 Automation

The ETL pipeline executes automatically every day using **GitHub Actions**.

```
Schedule

Every Day
```

Pipeline Flow

```
Generate Customer Data
          │
          ▼
Transform Data
          │
          ▼
Validate Data
          │
          ▼
Load into PostgreSQL
          │
          ▼
Refresh Dashboard
```

---

# 📦 Database Tables

### customers

Stores customer information.

### etl_logs

Stores ETL execution details.

### validation_errors

Stores invalid records detected during validation.

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/saipranavchaitanya/Customer-Churn-Analytics-Platform.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run ETL Pipeline

```bash
python run_pipeline.py
```

Run Dashboard

```bash
streamlit run dashboard/Home.py
```

---

# 🔐 Environment Variables

Create a `.env` file

```
DB_HOST=your_host
DB_PORT=5432
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=your_password
```

---

# 📸 Dashboard Screenshots

Replace these images with screenshots from your deployed application.

### 🏠 Home Dashboard

![Home Dashboard](images/home_dashboard.png)

### 👥 Customer Dashboard

![Customer Dashboard](images/customer_dashboard.png)

### 📉 Churn Dashboard

![Churn Dashboard](images/churn_dashboard.png)

### ⚙️ ETL Monitor

![ETL Monitor](images/etl_monitor.png)

---

# 🎯 Skills Demonstrated

* Python
* SQL
* PostgreSQL
* SQLAlchemy
* ETL Development
* Data Validation
* Data Cleaning
* Data Transformation
* Streamlit
* Plotly
* GitHub Actions
* Git
* GitHub
* Data Engineering
* Business Intelligence

---

# 📚 Future Enhancements

* Machine Learning Churn Prediction
* Email Notifications
* Apache Airflow Integration
* Docker Deployment
* Kubernetes Deployment
* Azure Data Factory Integration
* AWS Deployment
* Power BI Integration
* Real-Time Data Streaming

---

# 👨‍💻 Author

## **A.N.S. Pranav Chaitanya**

**B.Tech – Computer Science Engineering**

**Data Analyst | BI Developer | Data Engineering Enthusiast**

### 🌐 GitHub

https://github.com/saipranavchaitanya

### 🚀 Live Application

https://customer-churn-analytics-project.streamlit.app/

### 💼 LinkedIn

Add your LinkedIn profile here.

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
