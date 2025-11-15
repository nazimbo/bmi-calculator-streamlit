"""BMI Calculator - Streamlit Application.

A modern, secure, and well-tested web application that calculates
Body Mass Index (BMI) and provides personalized health insights.
"""

import sys
from pathlib import Path

import streamlit as st

# Add src directory to path for imports
src_path = Path(__file__).parent / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from bmi_calculator.core import (
    calculate_bmi,
    get_bmi_category,
    MIN_HEIGHT_CM,
    MAX_HEIGHT_CM,
    MIN_WEIGHT_KG,
    MAX_WEIGHT_KG,
)
from bmi_calculator.core.constants import (
    DEFAULT_HEIGHT_CM,
    DEFAULT_WEIGHT_KG,
    APP_TITLE,
    APP_ICON,
    APP_LAYOUT,
    HEALTH_TIPS,
    MEDICAL_DISCLAIMER,
)
from bmi_calculator.ui import create_gauge
from bmi_calculator.utils import get_logger

# Get logger (configured only once)
logger = get_logger(__name__)

# Page configuration
st.set_page_config(page_title="BMI Calculator", page_icon=APP_ICON, layout=APP_LAYOUT)

# Custom CSS
st.markdown(
    """
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
""",
    unsafe_allow_html=True,
)

# App header
st.title(APP_TITLE)
logger.info("BMI Calculator application started")

st.markdown("---")

# Create two columns for input
col1, col2 = st.columns(2)

with col1:
    height = st.number_input(
        "Height (cm)",
        min_value=MIN_HEIGHT_CM,
        max_value=MAX_HEIGHT_CM,
        value=DEFAULT_HEIGHT_CM,
        step=1,
        help=f"Enter your height in centimeters ({MIN_HEIGHT_CM}-{MAX_HEIGHT_CM} cm)",
    )

with col2:
    weight = st.number_input(
        "Weight (kg)",
        min_value=MIN_WEIGHT_KG,
        max_value=MAX_WEIGHT_KG,
        value=DEFAULT_WEIGHT_KG,
        step=1,
        help=f"Enter your weight in kilograms ({MIN_WEIGHT_KG}-{MAX_WEIGHT_KG} kg)",
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

# Display BMI gauge with error handling
try:
    st.plotly_chart(create_gauge(bmi), use_container_width=True)
except ValueError as e:
    st.error(f"❌ Invalid BMI value: {e}")
    logger.error(f"ValueError in gauge creation: {e}")
    # Fallback display
    st.markdown(f"### Your BMI: {bmi:.1f}")
    st.progress(min(bmi / 40, 1.0))
except Exception as e:
    st.error("❌ Unable to display BMI gauge. Please try again.")
    logger.error(f"Error displaying gauge: {e}", exc_info=True)
    # Fallback display
    st.markdown(f"### Your BMI: {bmi:.1f}")
    st.progress(min(bmi / 40, 1.0))

# Display weight category with colored boxes
st.markdown("### Your Results")

# Determine category using the new API
category = get_bmi_category(bmi)

# Use Streamlit native components
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Your BMI", value=f"{bmi:.1f}")
with col2:
    st.metric(label="Category", value=f"{category.emoji} {category.name}")

# Display category with appropriate styling using safe Streamlit components
if category.name == "Underweight":
    st.warning(f"⚠️ Your BMI indicates you are **{category.name}**")
elif category.name == "Normal weight":
    st.success(f"✅ Your BMI indicates you are at a **{category.name}**")
elif category.name == "Overweight":
    st.warning(f"⚠️ Your BMI indicates you are **{category.name}**")
else:
    st.error(f"🚨 Your BMI indicates you are **{category.name}**")

logger.info(f"BMI result displayed: {bmi:.2f} - Category: {category.name}")

# BMI Information expander
with st.expander("ℹ️ What is BMI?"):
    st.markdown(
        """
        **Body Mass Index (BMI)** is a simple calculation using your height and weight that is used to work out if your weight is healthy.

        ### BMI Categories:
        - **Underweight**: < 18.5
        - **Normal weight**: 18.5 - 24.9
        - **Overweight**: 25 - 29.9
        - **Obese**: ≥ 30

        *Note: BMI is not the only measure of health. Consult with healthcare professionals for proper medical advice.*
    """
    )

# Health tips based on BMI category
with st.expander("💡 Health Tips"):
    st.warning(
        "⚠️ These tips are for informational purposes only. "
        "Always consult with qualified healthcare professionals for medical advice."
    )
    tips = HEALTH_TIPS.get(category.name, "")
    if tips:
        st.markdown(tips)

# Footer
st.markdown("---")
st.info(MEDICAL_DISCLAIMER)
logger.info("BMI Calculator session completed")
