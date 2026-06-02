# CMS Medicare Provider Analysis

## 📊 Overview
This project analyzes the **CMS Medicare Physician & Other Practitioners dataset (2023)** to explore healthcare utilization, spending patterns, and reimbursement differences across provider specialties and geographic regions.

The analysis focuses on identifying key drivers of Medicare spending and uncovering insights into how healthcare services are delivered and reimbursed in the United States.

---

## 📁 Dataset
- Source: CMS Medicare Provider Utilization and Payment Data (2023)
- Size: ~1.2 million records
- Data includes:
  - Provider specialty
  - State
  - Total services
  - Submitted charges
  - Medicare payments

---

## 🛠 Tools & Technologies
- **SQL (SQLite)** – data querying and aggregation  
- **Python (Pandas)** – data cleaning and preprocessing  
- **Tableau Public** – data visualization and dashboarding  

---

## ❓ Business Questions
This project aims to answer the following:

1. Which provider specialties drive the highest Medicare spending?
2. Which states have the highest healthcare utilization and payments?
3. How do submitted charges compare to actual Medicare payments?
4. What drives healthcare spending: service volume or cost per service?

---

## 🔍 Key Findings

- **Spending Concentration**  
  Medicare spending is highly concentrated among a small number of specialties, including Ophthalmology, Internal Medicine, and Clinical Laboratory.

- **Geographic Variation**  
  States such as California, Florida, Texas, and New York account for the largest share of Medicare utilization and payments.

- **Charge vs Payment Gap**  
  There is a significant gap between submitted charges and actual Medicare payments, particularly for procedural specialties such as Ambulatory Surgical Centers and Diagnostic Radiology.

- **Two Drivers of Healthcare Spending**  
  A key insight from the analysis is that Medicare spending is driven by:
  - High-volume services (e.g., Clinical Laboratory, Internal Medicine)
  - High-cost procedures (e.g., Ophthalmology, Radiology)

---

## 📊 Dashboard

The Tableau dashboard visualizes:
- Top specialties by Medicare spending  
- Top states by utilization and payment  
- Charge vs payment differences  
- Service volume vs payment (scatter plot)

👉 (Add your Tableau Public link here)

---

## 🗂 Project Structure

cms-medicare-provider-analysis/
|
|-- data/
|   |-- raw/
|       |-- Medicare_Physician_Other_Practitioners_by_Provider_2023.csv
|       |-- MUP_PHY_RY25_20250312_DD_Prvdr_508.pdf
|       |-- MUP_PHY_RY25_202350312_Methodology_508.pdf
|   |-- processed/
|
|-- outputs/
|   |-- top_specialties.csv
|   |-- state_summary.csv
|   |-- charge_payment_gap.csv
|
|-- python/
|   |-- load_to_sqlite.py
|   |-- clean_data.py
|
|-- sql/
|   |-- test_connection.sql
|   |-- query_1_top specialties.sql
|   |-- query_2_top states.sql
|   |-- query_3_charge_gap.sql
|
|-- tableau/
|   |-- tt-cms-medicare-analysis.twbx
|
|-- screenshots/
|   |-- dashboard.png
|
|-- README.md
|
|-- tt_cms_medicare.db
---

## 🧠 Skills Demonstrated

- SQL data aggregation and analysis on large datasets (1M+ rows)
- Data cleaning and preprocessing using Python (Pandas)
- Healthcare data interpretation (Medicare utilization & reimbursement)
- Data visualization and dashboard design in Tableau
- Business insight generation and storytelling

---

## 🚀 Future Improvements

- Add time-series analysis if multi-year data is available  
- Incorporate provider-level analysis (NPI-level insights)  
- Perform outlier detection and cost-per-service normalization  
- Build predictive models for healthcare spending trends  

---

## 📌 Author

**Thuan Tran**  
Health Data Analyst (aspiring)  
📍 Buffalo, NY  

---

## ⭐ Notes

This project is part of a data analytics portfolio focused on healthcare data and real-world datasets in the United States.