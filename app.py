import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("airline_price_model.pkl")

st.title("✈️ Airline Fare Prediction")
st.write("Enter flight details to estimate ticket price")

# -------------------------
# Encoding dictionaries
# -------------------------

airline_dict = {
    "AirAsia": 0,
    "Air India": 1,
    "GO FIRST": 2,
    "Indigo": 3,
    "SpiceJet": 4,
    "Vistara": 5
}

city_dict = {
    "Delhi": 0,
    "Mumbai": 1,
    "Bangalore": 2,
    "Kolkata": 3,
    "Hyderabad": 4,
    "Chennai": 5
}

departure_time_dict = {
    "Early Morning": 0,
    "Morning": 1,
    "Afternoon": 2,
    "Evening": 3,
    "Night": 4,
    "Late Night": 5
}

arrival_time_dict = departure_time_dict

stops_dict = {
    "one": 0,
    "two": 1,
    "zero": 2
}

class_dict = {
    "Business": 0,
    "Economy": 1
}

# -------------------------
# User Inputs
# -------------------------

airline = st.selectbox("Airline", airline_dict.keys())

source_city = st.selectbox("Source City", city_dict.keys())

departure_time = st.selectbox("Departure Time", departure_time_dict.keys())

stops = st.selectbox("Stops", stops_dict.keys())

arrival_time = st.selectbox("Arrival Time", arrival_time_dict.keys())

destination_city = st.selectbox("Destination City", city_dict.keys())

class_type = st.selectbox("Class", class_dict.keys())

duration = st.number_input("Duration (in hours)", min_value=0.0)

days_left = st.number_input("Days Left Before Departure", min_value=0)

# -------------------------
# Convert to encoded values
# -------------------------

airline = airline_dict[airline]
source_city = city_dict[source_city]
departure_time = departure_time_dict[departure_time]
stops = stops_dict[stops]
arrival_time = arrival_time_dict[arrival_time]
destination_city = city_dict[destination_city]
class_type = class_dict[class_type]

# -------------------------
# Prediction
# -------------------------

if st.button("Predict Price"):

    input_data = np.array([[
        airline,
        source_city,
        departure_time,
        stops,
        arrival_time,
        destination_city,
        class_type,
        duration,
        days_left
    ]])

    prediction = model.predict(input_data)

    st.success(f"Estimated Flight Price: ₹ {int(prediction[0])}")