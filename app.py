import pickle
import pandas as pd
import streamlit as st

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('preprocessor.pkl', 'rb') as f:
    preprocessor = pickle.load(f)

st.title("Student Math Score Predictor")

gender = st.selectbox("Gender", ["female", "male"])
race_ethnicity = st.selectbox(
    "Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"]
)
parental_level_of_education = st.selectbox(
    "Parental Level of Education",
    [
        "some high school",
        "high school",
        "some college",
        "associate's degree",
        "bachelor's degree",
        "master's degree",
    ],
)
lunch = st.selectbox("Lunch", ["standard", "free/reduced"])
test_preparation_course = st.selectbox("Test Preparation", ["none", "completed"])
reading_score = st.number_input(
    "Reading Score", min_value=0, max_value=100, value=70
)
writing_score = st.number_input(
    "Writing Score", min_value=0, max_value=100, value=70
)

if st.button("Predict"):
    data = pd.DataFrame([{
        'gender': gender,
        'race_ethnicity': race_ethnicity,
        'parental_level_of_education': parental_level_of_education,
        'lunch': lunch,
        'test_preparation_course': test_preparation_course,
        'reading_score': reading_score,
        'writing_score': writing_score,
    }])

    transformed = preprocessor.transform(data)
    pred = model.predict(transformed)[0]

    st.success(f"Predicted Math Score: {pred:.2f}")