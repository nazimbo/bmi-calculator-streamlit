import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚕️",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stAlert {
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0.5rem;
    }
    div[data-testid="stExpander"] {
        border: none;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        padding: 1rem;
        border-radius: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# App header
st.markdown("""
    <h1 style='text-align: center; color: #2E4053;'>
        Body Mass Index (BMI) Calculator 
        <span style='font-size: 2rem;'>⚕️</span>
    </h1>
""", unsafe_allow_html=True)

st.markdown("---")

# Create two columns for input
col1, col2 = st.columns(2)

with col1:
    height = st.number_input(
        'Height (cm)',
        min_value=100,
        max_value=250,
        value=170,
        step=1,
        help="Enter your height in centimeters"
    )

with col2:
    weight = st.number_input(
        'Weight (kg)',
        min_value=10,
        max_value=150,
        value=70,
        step=1,
        help="Enter your weight in kilograms"
    )

# Calculate BMI
bmi = weight / (height / 100) ** 2

# Create BMI gauge
def create_gauge(bmi_value):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=bmi_value,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [None, 40], 'tickwidth': 1},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 18.5], 'color': "#FFC300"},    # Underweight
                {'range': [18.5, 24.9], 'color': "#2ECC71"}, # Normal
                {'range': [24.9, 29.9], 'color': "#FF5733"}, # Overweight
                {'range': [29.9, 40], 'color': "#C70039"},   # Obese
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': bmi_value
            }
        }
    ))
    
    fig.update_layout(
        height=300,
        margin=dict(l=10, r=10, t=40, b=10),
        font={'color': "#2E4053", 'family': "Arial"}
    )
    return fig

# Display BMI gauge
st.plotly_chart(create_gauge(bmi), use_container_width=True)

# Display weight category with colored boxes
st.markdown("### Your Results")

if bmi < 18.5:
    category = "Underweight"
    color = "#FFC300"
elif bmi < 24.9:
    category = "Normal weight"
    color = "#2ECC71"
elif bmi < 29.9:
    category = "Overweight"
    color = "#FF5733"
else:
    category = "Obese"
    color = "#C70039"

st.markdown(f"""
    <div style='
        background-color: {color};
        padding: 1rem;
        border-radius: 0.5rem;
        color: white;
        text-align: center;
        margin: 1rem 0;
        font-weight: bold;
    '>
        Your BMI is: {bmi:.1f}<br>
        Category: {category}
    </div>
""", unsafe_allow_html=True)

# BMI Information expander
with st.expander("ℹ️ What is BMI?"):
    st.markdown("""
        **Body Mass Index (BMI)** is a simple calculation using your height and weight that is used to work out if your weight is healthy.

        ### BMI Categories:
        - **Underweight**: < 18.5
        - **Normal weight**: 18.5 - 24.9
        - **Overweight**: 25 - 29.9
        - **Obese**: ≥ 30

        *Note: BMI is not the only measure of health. Consult with healthcare professionals for proper medical advice.*
    """)

# Health tips based on BMI category
with st.expander("💡 Health Tips"):
    if bmi < 18.5:
        st.markdown("""
            ### Tips for Healthy Weight Gain:
            - Eat more frequently throughout the day
            - Choose nutrient-rich foods
            - Add healthy snacks between meals
            - Include protein with every meal
            - Consider strength training exercises
        """)
    elif bmi < 24.9:
        st.markdown("""
            ### Tips to Maintain Healthy Weight:
            - Keep up your balanced diet
            - Stay physically active
            - Get adequate sleep
            - Stay hydrated
            - Monitor your weight regularly
        """)
    elif bmi < 29.9:
        st.markdown("""
            ### Tips for Weight Management:
            - Increase physical activity
            - Control portion sizes
            - Choose whole foods over processed foods
            - Track your daily calorie intake
            - Consider consulting a nutritionist
        """)
    else:
        st.markdown("""
            ### Tips for Weight Loss:
            - Consult with healthcare professionals
            - Start with moderate exercise
            - Focus on portion control
            - Keep a food diary
            - Set realistic goals
        """)

# Footer
st.markdown("---")
st.markdown("""
    <p style='text-align: center; color: #666;'>
        Remember: BMI is just one measure of health. Always consult with healthcare professionals for medical advice.
    </p>
""", unsafe_allow_html=True)