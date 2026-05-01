import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="US Car Listings Analysis",
    page_icon="🚗",
    layout="wide"
)

# -------------------------------
# HEADER & BUSINESS CONTEXT
# -------------------------------
st.title("🚗 US Second-Hand Car Listings — Market Analysis")
st.markdown("""
This dashboard explores a dataset of **used car listings in the United States**.  
Use the filters on the left to explore how **price, mileage, condition and vehicle type**  
interact across the market — and what patterns emerge for buyers and sellers.
""")
st.divider()

# -------------------------------
# LOAD DATA
# -------------------------------
car_data = pd.read_csv('vehicles_us.csv')

# -------------------------------
# SIDEBAR FILTERS
# -------------------------------
st.sidebar.header("🔍 Filters")

selected_condition = st.sidebar.selectbox(
    "Vehicle condition",
    options=["All"] + sorted(car_data["condition"].dropna().unique().tolist())
)

selected_type = st.sidebar.selectbox(
    "Vehicle type",
    options=["All"] + sorted(car_data["type"].dropna().unique().tolist())
)

year_min = int(car_data["model_year"].dropna().min())
year_max = int(car_data["model_year"].dropna().max())
selected_years = st.sidebar.slider(
    "Model year range",
    year_min, year_max,
    (2005, year_max)
)

max_odometer = int(car_data["odometer"].max())
selected_odometer = st.sidebar.slider(
    "Max odometer (km)",
    0, max_odometer, 150000
)

st.sidebar.divider()
st.sidebar.header("📊 Charts")
build_histogram = st.sidebar.checkbox("Odometer distribution")
build_scatter    = st.sidebar.checkbox("Price vs odometer")
build_bar        = st.sidebar.checkbox("Listings by vehicle type")
build_box        = st.sidebar.checkbox("Price by condition")

# -------------------------------
# APPLY FILTERS
# -------------------------------
filtered = car_data.copy()

if selected_condition != "All":
    filtered = filtered[filtered["condition"] == selected_condition]

if selected_type != "All":
    filtered = filtered[filtered["type"] == selected_type]

filtered = filtered[
    (filtered["model_year"] >= selected_years[0]) &
    (filtered["model_year"] <= selected_years[1])
]

filtered = filtered[filtered["odometer"] <= selected_odometer]

# -------------------------------
# KPI METRICS
# -------------------------------
st.subheader("📈 Key Metrics")
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total listings", f"{len(filtered):,}")
col2.metric("Average price", f"${filtered['price'].mean():,.0f}")
col3.metric("Average odometer", f"{filtered['odometer'].mean():,.0f} km")
col4.metric("Most common condition",
            filtered["condition"].mode()[0] if len(filtered) > 0 else "N/A")

st.divider()

# -------------------------------
# DATA TABLE
# -------------------------------
with st.expander("📋 View filtered data"):
    st.dataframe(filtered, use_container_width=True)

# -------------------------------
# CHARTS
# -------------------------------
if build_histogram:
    st.subheader("Odometer Distribution")
    st.markdown("*How many kilometres have most listed cars been driven?*")
    fig = go.Figure(data=[go.Histogram(
        x=filtered["odometer"],
        marker_color="#2E74B5",
        opacity=0.8
    )])
    fig.update_layout(
        xaxis_title="Odometer (km)",
        yaxis_title="Number of listings",
        title="Distribution of Odometer Readings"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Most listings cluster between 50,000 and 150,000 km — typical for second-hand markets.")

if build_scatter:
    st.subheader("Price vs Odometer")
    st.markdown("*Does higher mileage always mean a lower price?*")
    fig = px.scatter(
        filtered,
        x="odometer",
        y="price",
        color="condition",
        opacity=0.5,
        labels={
            "odometer": "Odometer (km)",
            "price": "Price (USD)",
            "condition": "Condition"
        },
        title="Price vs Odometer by Condition"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Higher mileage generally correlates with lower prices, but condition plays a significant role.")

if build_bar:
    st.subheader("Listings by Vehicle Type")
    st.markdown("*Which vehicle types dominate the second-hand market?*")
    type_counts = filtered["type"].value_counts().reset_index()
    type_counts.columns = ["type", "count"]
    fig = px.bar(
        type_counts,
        x="type",
        y="count",
        color="count",
        color_continuous_scale="Blues",
        labels={"type": "Vehicle type", "count": "Number of listings"},
        title="Number of Listings by Vehicle Type"
    )
    fig.update_layout(coloraxis_showscale=False)
    st.plotly_chart(fig, use_container_width=True)
    st.caption("SUVs and sedans are the most common vehicle types in the dataset.")

if build_box:
    st.subheader("Price Distribution by Condition")
    st.markdown("*How much does vehicle condition affect the asking price?*")
    fig = px.box(
        filtered,
        x="condition",
        y="price",
        color="condition",
        labels={"condition": "Condition", "price": "Price (USD)"},
        title="Price Range by Vehicle Condition"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.caption("'New' and 'like new' vehicles command significantly higher prices with less variability.")

# -------------------------------
# FOOTER
# -------------------------------
st.divider()
st.markdown("""
<small>Dataset: US vehicle listings | 
Built with Python, Streamlit & Plotly | 
[GitHub](https://github.com/Lorena885/Analisis_de_Anuncios_de_Coches)</small>
""", unsafe_allow_html=True)