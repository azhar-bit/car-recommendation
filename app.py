import pandas as pd
import streamlit as st

# Load dataset
df = pd.read_csv("cars.csv")
df.dropna(inplace=True)

# --- Session State to handle login ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Login to Car Recommender")
    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email")
    if st.button("Login"):
        if name and email:
            st.session_state.logged_in = True
            st.session_state.name = name
            st.session_state.email = email
            st.success("Login successful! 🎉")
        else:
            st.warning("Please fill in all fields.")
    st.stop()

# --- Main Recommender Page ---
st.title("🚗 Car Recommendation System")
st.write(f"Welcome, **{st.session_state.name}**! 👋")

# Sidebar filters
st.sidebar.header("Filter Options")

min_price = st.sidebar.number_input("Minimum Price (in Lakhs)", value=3.0)
max_price = st.sidebar.number_input("Maximum Price (in Lakhs)", value=10.0)
fuel = st.sidebar.selectbox("Fuel Type", options=["", "Petrol", "Diesel", "CNG", "Electric"])

# Filter logic
filtered = df[(df['Present_Price'] >= min_price) & (df['Present_Price'] <= max_price)]

if fuel:
    filtered = filtered[filtered['Fuel_Type'].str.lower() == fuel.lower()]

# Display results
st.subheader("🔍 Recommended Cars")
st.write(filtered[["Car_Name", "Year", "Present_Price", "Fuel_Type", "Transmission", "Kms_Driven"]].reset_index(drop=True))

# Download
st.download_button("📥 Download as CSV", data=filtered.to_csv(index=False), file_name="recommendations.csv")
