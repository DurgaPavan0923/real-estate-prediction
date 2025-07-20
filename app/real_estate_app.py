import streamlit as st

# Layout Section (from M1)
st.title("🏠 Real Estate Price Prediction")
st.markdown("Enter the property details below to estimate the house price per unit area:")

# M2 - Input fields for model
st.subheader("📋 Property Details")

# Input widgets
transaction_year = st.selectbox("Transaction Year", [2012, 2013], index=1)
house_age = st.slider("House Age (Years)", min_value=0, max_value=50, value=10)
distance_to_mrt = st.number_input("Distance to MRT (meters)", min_value=0.0, value=500.0, step=10.0)
num_stores = st.slider("Number of Nearby Stores", min_value=0, max_value=20, value=5)
latitude = st.number_input("Latitude", min_value=0.0, max_value=90.0, value=24.96)
longitude = st.number_input("Longitude", min_value=0.0, max_value=180.0, value=121.54)
