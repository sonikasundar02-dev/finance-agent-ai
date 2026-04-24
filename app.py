import streamlit as st
from agents import aero_agent, emission_agent, financial_agent

st.set_page_config(page_title="Sky-Bound Flight Deck", layout="wide")

st.title("🛩️ Sky-Bound Flight Deck")

# INPUTS
distance = st.number_input("Flight Distance (km)", value=1200)
payload = st.number_input("Payload (kg)", value=5000)
wind_type = st.selectbox("Wind Type", ["headwind", "tailwind", "none"])
wind_speed = st.slider("Wind Speed (knots)", 0, 50, 10)
fuel_price = st.number_input("Fuel Price ($/litre)", value=1.2)
carbon_price = st.number_input("Carbon Tax ($/unit)", value=0.05)

if st.button("Run Analysis"):

    # AGENT 1
    fuel_burn, impact = aero_agent(distance, payload, wind_type, wind_speed)

    # AGENT 2
    emissions, carbon_cost = emission_agent(fuel_burn, carbon_price)

    # AGENT 3
    decision, reason, savings, total_cost = financial_agent(
        fuel_burn, fuel_price, carbon_cost, wind_type
    )

    # DASHBOARD OUTPUT
    st.subheader("✈️ Aero Report")
    st.write(f"Fuel Burn: {fuel_burn:.2f} litres")
    st.write(f"Impact: {impact:.2f}%")

    st.subheader("🌍 Emissions Report")
    st.write(f"CO2: {emissions:.2f} kg")
    st.write(f"Carbon Cost: ${carbon_cost:.2f}")

    st.subheader("📊 Financial Decision")
    st.write(f"Decision: {decision}")
    st.write(f"Reason: {reason}")
    st.write(f"Total Cost: ${total_cost:.2f}")
    st.write(f"Estimated Savings: ${savings:.2f}")
