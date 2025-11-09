import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import logging
from logging.handlers import RotatingFileHandler
import sys

# Configure logging
log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(
    level=logging.INFO,
    format=log_format,
    handlers=[
        RotatingFileHandler('bmi_calculator.log', maxBytes=10485760, backupCount=5),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


# Core BMI calculation functions (extracted for testability)
def calculate_bmi(height_cm: float, weight_kg: float) -> float:
    """Calculate BMI from height and weight.

    Args:
        height_cm: Height in centimeters
        weight_kg: Weight in kilograms

    Returns:
        Calculated BMI value

    Raises:
        ValueError: If height or weight are invalid
    """
    if height_cm <= 0 or weight_kg <= 0:
        raise ValueError("Height and weight must be positive values")
    if height_cm > 300 or weight_kg > 500:
        raise ValueError("Height or weight values are unrealistic")

    return weight_kg / (height_cm / 100) ** 2


def get_bmi_category(bmi: float) -> tuple:
    """Get BMI category, color, and emoji.

    Args:
        bmi: The BMI value

    Returns:
        Tuple of (category_name, color, emoji)
    """
    if bmi < 0:
        raise ValueError("BMI cannot be negative")

    if bmi < 18.5:
        return ("Underweight", "#FFC300", "⚠️")
    elif bmi < 24.9:
        return ("Normal weight", "#2ECC71", "✅")
    elif bmi < 29.9:
        return ("Overweight", "#FF5733", "⚠️")
    else:
        return ("Obese", "#C70039", "🚨")


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
st.title("⚕️ Body Mass Index (BMI) Calculator")
logger.info("BMI Calculator application started")

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

# Calculate BMI with error handling
try:
    bmi = calculate_bmi(height, weight)
    logger.info(f"BMI calculated: {bmi:.2f} for height={height}cm, weight={weight}kg")
except ValueError as e:
    st.error(f"❌ {str(e)}")
    logger.error(f"ValueError during BMI calculation: {e}")
    st.stop()
except Exception as e:
    st.error("❌ An unexpected error occurred while calculating BMI. Please try again.")
    logger.error(f"Unexpected error during BMI calculation: {e}", exc_info=True)
    st.stop()

# Create BMI gauge
def create_gauge(bmi_value: float) -> go.Figure:
    """Create an interactive gauge chart displaying BMI value.

    Args:
        bmi_value: The calculated Body Mass Index value

    Returns:
        A Plotly Figure object configured as an indicator gauge

    Raises:
        ValueError: If bmi_value is negative or unreasonably high
    """
    if bmi_value < 0 or bmi_value > 100:
        raise ValueError(f"Invalid BMI value: {bmi_value}")

    try:
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
    except Exception as e:
        logger.error(f"Error creating gauge chart: {e}", exc_info=True)
        raise

# Display BMI gauge with error handling
try:
    st.plotly_chart(create_gauge(bmi), use_container_width=True)
except ValueError as e:
    st.error(f"❌ Invalid BMI value: {e}")
    logger.error(f"ValueError in gauge creation: {e}")
    st.stop()
except Exception as e:
    st.error("❌ Unable to display BMI gauge. Please try again.")
    logger.error(f"Error displaying gauge: {e}", exc_info=True)
    st.stop()

# Display weight category with colored boxes
st.markdown("### Your Results")

# Determine category and color using the centralized function
category, color, emoji = get_bmi_category(bmi)

# Use Streamlit native components instead of unsafe HTML
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Your BMI", value=f"{bmi:.1f}")
with col2:
    st.metric(label="Category", value=f"{emoji} {category}")

# Display category with appropriate styling using safe Streamlit components
if category == "Underweight":
    st.warning(f"⚠️ Your BMI indicates you are **{category}**")
elif category == "Normal weight":
    st.success(f"✅ Your BMI indicates you are at a **{category}**")
elif category == "Overweight":
    st.warning(f"⚠️ Your BMI indicates you are **{category}**")
else:
    st.error(f"🚨 Your BMI indicates you are **{category}**")

logger.info(f"BMI result displayed: {bmi:.2f} - Category: {category}")

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
st.info("ℹ️ Remember: BMI is just one measure of health. Always consult with healthcare professionals for medical advice.")
logger.info("BMI Calculator session completed")