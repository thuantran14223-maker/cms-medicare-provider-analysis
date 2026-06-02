![Dashboard](screenshots/dashboard.png)
# CMS Medicare Provider Analysis

## Project Overview

This project analyzes CMS Medicare Physician & Other Practitioners data (2023) to explore healthcare spending patterns, reimbursement structures, and provider specialty strategies across the United States.

The analysis combines Python, SQL, and Tableau to identify key drivers of Medicare spending and understand how provider specialties differ in service volume, reimbursement, and payment outcomes.

---

## Dashboard

**Dashboard Title**

Medicare Spending Patterns: Volume, Cost, and Provider Strategy

The dashboard examines:

* Top provider specialties by Medicare payment
* Geographic concentration of Medicare spending
* Charge versus Medicare reimbursement gaps
* Service volume versus payment relationships across specialties

**Tableau Public Dashboard**

https://public.tableau.com/app/profile/thuan.tran6584/viz/CMSMedicareProviderAnalysisDashboard/MedicareSpendingPatternsVolumeCostandProviderStrategy?publish=yes

---

## Dataset

**Source:** CMS Medicare Physician & Other Practitioners Data (2023)

**Original Dataset Size:** Approximately 1.2 million records

The original CMS dataset exceeds GitHub file size recommendations. To keep this repository lightweight and reproducible, a sample dataset is included for demonstration purposes.

Data fields include:

* Provider specialty
* State
* Total services
* Submitted charges
* Medicare payments

---

## Business Questions

1. Which provider specialties receive the highest Medicare payments?
2. Which states account for the largest share of Medicare spending?
3. How large is the gap between submitted charges and Medicare reimbursement?
4. Is Medicare spending primarily driven by service volume or reimbursement levels?

---

## Tools & Technologies

* Python (Pandas)
* SQLite
* SQL
* Tableau Public

---

## Key Findings

### 1. High-volume specialties drive total spending

Specialties such as Internal Medicine, Ophthalmology, Nurse Practitioner, and Clinical Laboratory account for a substantial share of Medicare payments due to high utilization.

### 2. Medicare spending is geographically concentrated

California, Florida, Texas, and New York represent the largest Medicare payment totals, reflecting population size and healthcare demand.

### 3. Large charge gaps reflect negotiated pricing

Submitted charges significantly exceed Medicare reimbursement across specialties. These differences reflect reimbursement structures rather than actual provider collections.

### 4. Specialties exhibit distinct payment-volume patterns

Different specialties achieve high Medicare payments through different service-volume patterns.

### 5. Providers follow distinct reimbursement models

The relationship between service volume and Medicare payment varies considerably across specialties, highlighting differences in reimbursement mechanisms and care delivery strategies.

---

## Project Workflow

CMS Medicare Data

→ Python Data Cleaning

→ SQLite Database

→ SQL Analysis

→ CSV Export

→ Tableau Dashboard

→ Business Insights

---

## Repository Structure

```text
cms-medicare-provider-analysis/
│
├── README.md
│
├── data/
│   ├── raw/
│   │   └── tt_cms_medicare_sample_2023.csv
│   │
│   └── processed/
│       ├── top_specialties.csv
│       ├── top_states.csv
│       └── charge_gap.csv
│
├── python/
│   └── load_clean_to_sqlite.py
│   └── create_sample_data.py
│
├── sql/
│   ├── 01_top_specialties.sql
│   ├── 02_top_states.sql
│   └── 03_charge_gap.sql
│
├── tableau/
│   └── tt-cms-medicare-analysis.twbx
│
└── screenshots/
    └── dashboard.png
```

---

## Skills Demonstrated

* SQL querying and aggregation on large healthcare datasets
* Data cleaning and preprocessing using Python (Pandas)
* Healthcare utilization and reimbursement analysis
* Tableau dashboard development and data visualization
* Business storytelling with data
* Public health analytics

---

## Future Improvements

* Add multi-year trend analysis if additional CMS data becomes available
* Expand provider-level analysis (NPI-level insights)
* Develop cost-per-service and reimbursement efficiency metrics
* Explore predictive analytics for healthcare spending trends

---

## Author

**Thuan Tran**

Healthcare Data Analytics Portfolio Project

Buffalo, New York
