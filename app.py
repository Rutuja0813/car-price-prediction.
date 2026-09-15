
# this ui part of car price prediction

import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('car_price_model.pkl', 'rb') as file:
    model = pickle.load(file)

# title and description
st.set_page_config(page_title="Car Price Prediction", page_icon="🚗", layout="wide")
st.title("Car Price Prediction App")
st.markdown("""
This app predicts the price of a car based on various features.
Please enter the details below and click on 'Predict Price' to see the estimate.
""")

# input section
st.sidebar.header("Input Features")

import streamlit as st

st.title("Car Price Prediction App")
st.write("This app predicts the price of a car based on various features.")

# Input field
import numpy as np
import streamlit as st
import pickle

# Load the trained model

with open("car_price_model.pkl", "rb") as file:
    model = pickle.load(file)



# Page configuration
st.set_page_config(page_title="Car Price Prediction", page_icon="🚗", layout="centered")

st.title("Car Price Prediction App")
st.markdown("""
This app predicts the price of a car based on various features.
Please enter the details below and click on 'Predict Price' to see the estimated price.
""")

# Input section
st.subheader("Enter Car Details")
col1, col2 = st.columns(2)

with col1:
    brand = st.selectbox("Car Brand",
                         ["audi", "bmw", "chevrolet", "honda", "hyundai", "jaguar",
                          "mazda", "mercedes", "mitsubishi", "nissan", "porsche",
                          "subaru", "toyota", "volkswagen", "volvo"])
    fueltype = st.selectbox("Fuel Type", ["gas", "diesel"])
    aspiration = st.selectbox("Aspiration", ["std", "turbo"])
    doornumber = st.selectbox("Number of Doors", ["two", "four"])
    carbody = st.selectbox("Car Body Type", ["sedan", "hatchback", "convertible", "wagon", "hardtop"])

with col2:
    drivewheel = st.selectbox("Drive Wheel", ["fwd", "rwd", "4wd"])
    enginesize = st.number_input("Engine Size (cc)", min_value=50, max_value=600, value=150)
    horsepower = st.number_input("Horsepower (HP)", min_value=40, max_value=400, value=100)
    citympg = st.number_input("City Mileage (km/l)", min_value=5, max_value=40, value=15)
    highwaympg = st.number_input("Highway Mileage (km/l)", min_value=5, max_value=50, value=20)

st.markdown("---")

if st.button("🚗 Predict Car Price"):
    # Sample input array (This will depend on your feature structure)
    # For demonstration, let's assume your model expects [enginesize, horsepower, citympg, highwaympg]
    input_data = np.array([[enginesize, horsepower, citympg, highwaympg]])

    # Predict price
    predicted_price = model.predict(input_data)[0]

    # Display result
    st.success(f"💰 Estimated Car Price: ${predicted_price:,.2f}")

    st.balloons()



