# 🚗 US Second-Hand Car Listings — Market Analysis Dashboard

An interactive web application built with Streamlit and Plotly to explore 
and analyse a dataset of used car listings across the United States — 
helping buyers, sellers and analysts understand pricing patterns, 
mileage trends and market composition.

---

## 📌 Business Problem

The second-hand car market is highly fragmented — prices vary significantly 
depending on mileage, condition, vehicle type and model year. 
Without a clear way to explore these variables together, it's difficult 
to make informed buying or selling decisions.

This dashboard makes that exploration fast and visual.

---

## 🎯 Objective

Build an interactive tool that allows users to:
- Filter listings by condition, type, model year and odometer
- Visualise key market patterns through dynamic charts
- Extract actionable insights from raw listing data

---

## 🚀 Live App

👉 [Open the dashboard](https://proyecto-sprint7-0nrf.onrender.com)

---

## 📊 Features

| Feature | Description |
|---|---|
| KPI Metrics | Total listings, average price, average odometer, most common condition |
| Sidebar Filters | Condition, vehicle type, model year range, max odometer |
| Odometer Distribution | Histogram showing mileage spread across listings |
| Price vs Odometer | Scatter plot coloured by condition |
| Listings by Type | Bar chart showing market share by vehicle type |
| Price by Condition | Box plot showing price ranges per condition level |
| Data Table | Collapsible filtered dataset view |

---

## 🔧 Tools & Libraries

| Category | Tools |
|---|---|
| Language | Python 3.14 |
| Web framework | Streamlit |
| Visualisation | Plotly Express, Plotly Graph Objects |
| Data manipulation | Pandas |
| Deployment | Render |

---


## 🧪 Key Insights

- Most listings cluster between **50,000 and 150,000 km** — 
  typical for the second-hand market
- Higher mileage generally correlates with lower prices, 
  but **condition plays a significant role** in final value
- **SUVs and sedans** dominate the listing volume
- **"New" and "like new"** vehicles command significantly 
  higher prices with less price variability

---

## 🚀 How to Run Locally

1. Clone this repository:
```bash
git clone https://github.com/Lorena885/Analisis_de_Anuncios_de_Coches.git
cd Analisis_de_Anuncios_de_Coches
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```
