import streamlit as st
from health_engine import analyze_health

st.set_page_config(
    page_title="Personal AI Health Solutions",
    page_icon="❤️",
    layout="centered",
)

st.title("Personal AI Health Assistant")
st.subheader("Data → AI → Insight → Action")

st.write(
    "Enter a few daily wellness values to demonstrate how a personal AI health "
    "assistant can turn data into simple, personalized actions."
)

st.warning(
    "Educational prototype only. This app provides general wellness insights "
    "and is not a medical diagnostic tool."
)

st.header("1. Collect Personal Data")

sleep_hours = st.number_input(
    "Sleep (hours)",
    min_value=0.0,
    max_value=24.0,
    value=7.0,
    step=0.5,
)

steps = st.number_input(
    "Daily steps",
    min_value=0,
    max_value=100000,
    value=6000,
    step=500,
)

heart_rate = st.number_input(
    "Resting heart rate (bpm)",
    min_value=20,
    max_value=220,
    value=72,
    step=1,
)

water_liters = st.number_input(
    "Water intake (liters)",
    min_value=0.0,
    max_value=10.0,
    value=2.0,
    step=0.1,
)

goal = st.text_input(
    "Personal goal",
    value="Maintain a healthy daily routine",
)

if st.button("Analyze My Data", type="primary"):
    data = {
        "sleep_hours": sleep_hours,
        "steps": steps,
        "heart_rate": heart_rate,
        "water_liters": water_liters,
        "goal": goal,
    }

    insights, actions = analyze_health(data)

    st.header("2. AI-Style Analysis & Insights")

    for insight in insights:
        st.write("•", insight)

    st.header("3. Personalized Actions")

    for action in actions:
        st.write("→", action)

    st.success("Analysis complete.")

st.divider()
st.caption(
    "Prototype for academic demonstration. Always consult a qualified healthcare "
    "professional for medical concerns."
)
