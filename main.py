import streamlit as st

st.title('BMI Calculator')

# Input fields for height and weight
height = st.number_input('Enter your height in centimeters:', min_value=100, max_value=250)
weight = st.number_input('Enter your weight in kilograms:', min_value=10, max_value=150)

# Calculate BMI
bmi = weight / (height / 100) ** 2

# Display BMI result and weight category
st.header('Your BMI:')
st.write(bmi)

if bmi < 18.5:
    st.write('Your weight is categorized as "Underweight".')
elif bmi < 25:
    st.write('Your weight is categorized as "Normal weight".')
elif bmi < 30:
    st.write('Your weight is categorized as "Overweight".')
else:
    st.write('Your weight is categorized as "Obese".')
