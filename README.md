# Telecom Customer Churn Analysis

An end-to-end Business Analysis project investigating why customers leave a telecom company — and which customers are most at risk.

---

## Dashboard Preview

![Telecom Churn Dashboard](TelecomChurnProject\dashboard_preview.png)

---

## Business Problem

A telecom company is losing customers and doesn't know why. This project answers three key questions:

- How many customers are churning, and what is the churn rate?
- What are the main reasons customers are leaving?
- Which contract types and cities have the highest churn?

---

## Tools Used

| Tool | Purpose |
|---|---|
| SQL (DB Browser for SQLite) | Extract and query the data |
| Python (Pandas) | Clean and prepare the data |
| Tableau Public | Build the interactive dashboard |

---

## Project Structure

```
TelecomChurnProject/
├── data/
│   └── telecom_customer_churn.csv        ← Raw dataset (7,043 customers)
├── scripts/
│   └── clean_data.py                     ← Python data cleaning script
├── output/
│   ├── 1_churn_overview.csv              ← Overall churn rate
│   ├── 2_churn_by_contract.csv           ← Churn breakdown by contract type
│   ├── 3_churn_reasons.csv               ← Top reasons customers left
│   ├── 4_revenue_lost.csv                ← Revenue impact of churn
│   └── 5_churn_by_city.csv               ← Cities with the highest churn
├── Telecom_Churn_Analysis.twbx           ← Tableau dashboard file
├── dashboard_preview.png                 ← Dashboard screenshot
└── README.md
```

---

## Dataset

- **Source:** Maven Analytics — Telecom Customer Churn
- **Size:** 7,043 customers, 38 columns
- **Location:** California, USA

---

## Data Issues Found & Fixed

| Problem | Rows Affected | Fix Applied |
|---|---|---|
| Missing Churn Reason | 5,174 | Filled with "Not Churned" |
| Missing Internet Type | 1,526 | Filled with "No Internet" |
| Missing Offer | 3,877 | Filled with "No Offer" |
| Negative Monthly Charges | 120 | Removed from dataset |

---

## SQL Queries

Five queries were written to extract key business insights:

1. **Churn Overview** — Overall churn rate across all customers
2. **Churn by Contract** — Breakdown of churn by contract type
3. **Churn Reasons** — Top reasons customers left ranked by volume
4. **Revenue Lost** — Total and average revenue by customer status
5. **Churn by City** — Top 10 cities with the highest churn

---

## Key Findings

- **26.5%** of customers churned — roughly 1 in 4 customers
- **Month-to-Month** contract customers churn at a significantly higher rate than yearly contracts
- The **top 2 churn reasons** are both competitor-related — customers are being poached, not leaving due to poor service
- **San Diego** and **Los Angeles** have the highest number of churned customers

---

## Dashboard

The Tableau dashboard includes 5 interactive charts:

- Churn Overview — total customers by status
- Churn by Contract Type — stacked bar chart
- Top Churn Reasons — horizontal bar chart
- Revenue Lost — revenue comparison by status
- Cities with Highest Churn — horizontal bar chart

---

## How to Open the Dashboard

1. Download and install [Tableau Public](https://public.tableau.com) for free
2. Open `Telecom_Churn_Analysis.twbx`
3. All data is packaged inside the file — no additional setup needed

---

## Author

**Chase Brangham**  
[GitHub Profile](https://github.com/ChaseBrangham)
