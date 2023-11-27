import streamlit as st
import pandas as pd
import joblib

# Custom styles
st.markdown(
    """
    <style>
        .sidebar-content {
            background-color: pink;
            padding: 10px;
        }
        .main-content {
            background-color: lightblue;
            padding: 10px;
            text-align: center;
        }
        .selected-features th {
            background-color: pink !important;
            color: white !important;
        }
        .selected-features td {
            background-color: lightblue !important;
            color: black !important;
        }
        .stSlider {
            margin-bottom: 20px;
        }
        /* Modify select box styles */
        .SelectBox {
            font-size: 18px !important;
            color: blue !important;
        }
        /* Modify select option styles */
        .SelectBox option {
            font-size: 18px !important;
            color: red !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

class SessionState:
    def __init__(self):
        self.predicted = False

# Create a session state
session_state = SessionState()

def load_model():
    # Load the pre-trained pipeline (LC_pipe) using joblib
    pipeline = joblib.load("LC_pipe.joblib")

    # Load your pre-trained machine learning model
    model = joblib.load("rf_model.joblib")

    return pipeline, model

def main():
    # Load the machine learning model and pipeline
    pipeline, model = load_model()

    # Large title at the beginning
    st.title("To know the price of your car")

    # Sidebar inputs
    age = st.selectbox("Select the age of your car:", ['', 0, 1, 2, 3], key="Age", help="Select the age of your car")
    hp_kW = st.slider("Select the horsepower (hp_kW) of your car:", 10., 168., step=1., key="hp_kW", help="Select the horsepower (hp_kW) of your car")
    make_model = st.selectbox("Select the model of your car", ['', 'Audi A1', 'Audi A2', 'Audi A3', 'Opel Astra', 'Opel Corsa', 'Opel Insignia', 'Renault Clio', 'Renault Duster', 'Renault Espace'], key="Make Model", help="Select the model of your car")
    gears = st.selectbox("Select the gears of your car", ['', 7, 6, 5, 8], key="Gears", help="Select the gears of your car")
    km = st.slider("Select the kilometers driven by your car", 0, 350000, step=100, key="km", help="Select the kilometers driven by your car")

    # Check if any feature is set to a default value, and prompt the user to select values
    if age == '' or hp_kW == 66. or make_model == '' or gears == '' or km == 0:
        st.warning("Please select values for all features.")
    elif session_state.predicted:
        st.info("Prediction has already been made. Press 'Try Another Prediction' to make a new prediction.")
    else:
        # Display selected features in a table with modified colors
        selected_features = pd.DataFrame({
            'Feature': ['Age', 'Horsepower', 'Make Model', 'Gears', 'Kilometers'],
            'Selected Value': [age, hp_kW, make_model, gears, km]
        })

        # Display the styled table
        st.subheader("Selected Features:")
        st.table(selected_features.style.set_table_styles([
            {'selector': 'th', 'props': [('background-color', 'pink'), ('color', 'white')]},
            {'selector': 'td', 'props': [('background-color', 'lightblue'), ('color', 'black')]}
        ]))

        # Prepare input features for prediction
        input_data = pd.DataFrame({
            'age': [age],
            'hp_kW': [hp_kW],
            'make_model': [make_model],
            'Gears': [gears],
            'km': [km]
        })

        # Use the pipeline for preprocessing
        input_data_preprocessed = pipeline.transform(input_data)

        # Button to trigger prediction
        if st.button("Predict", key="Predict"):
            # MakeHere's the continuation of the code:


            # Make predictions using the loaded model
            prediction = model.predict(input_data_preprocessed)

            # Display the predicted price or relevant information
            st.write(f"Predicted Car Price: {prediction[0]}")

            # Set session state to True after the first prediction
            session_state.predicted = True

        # Button to reset the form and try another prediction
        if st.button("Try Another Prediction", key="Try Another Prediction"):
            # Reset session state
            session_state.predicted = False

if __name__ == "__main__":
    main()