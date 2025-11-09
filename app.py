"""BMI Calculator - Main Application.

A modern, secure web application for calculating Body Mass Index (BMI)
and providing personalized health insights.
"""

import streamlit as st
import logging
from logging.handlers import RotatingFileHandler
import sys

from config.constants import config
from core.calculations import BMICalculator
from core.validators import InputValidator
from ui.components import UIComponents
from ui.styles import get_custom_css

# Configure logging
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL),
    format=config.LOG_FORMAT,
    handlers=[
        RotatingFileHandler(
            config.LOG_FILE,
            maxBytes=config.LOG_MAX_BYTES,
            backupCount=config.LOG_BACKUP_COUNT
        ),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Main application function."""
    # Page configuration
    st.set_page_config(
        page_title=config.PAGE_TITLE,
        page_icon=config.PAGE_ICON,
        layout=config.PAGE_LAYOUT
    )

    # Apply custom CSS
    st.markdown(get_custom_css(), unsafe_allow_html=True)

    # App header
    st.title(f"{config.PAGE_ICON} Body Mass Index (BMI) Calculator")
    logger.info("BMI Calculator application started")

    st.markdown("---")

    # Create two columns for input
    col1, col2 = st.columns(2)

    with col1:
        height = st.number_input(
            'Height (cm)',
            min_value=config.HEIGHT_MIN_CM,
            max_value=config.HEIGHT_MAX_CM,
            value=config.HEIGHT_DEFAULT_CM,
            step=1,
            help=f"Enter your height in centimeters ({config.HEIGHT_MIN_CM}-{config.HEIGHT_MAX_CM} cm)"
        )

    with col2:
        weight = st.number_input(
            'Weight (kg)',
            min_value=config.WEIGHT_MIN_KG,
            max_value=config.WEIGHT_MAX_KG,
            value=config.WEIGHT_DEFAULT_KG,
            step=1,
            help=f"Enter your weight in kilograms ({config.WEIGHT_MIN_KG}-{config.WEIGHT_MAX_KG} kg)"
        )

    # Validate inputs
    is_valid, error_msg = InputValidator.validate_inputs(height, weight)
    if not is_valid:
        st.error(f"❌ {error_msg}")
        logger.warning(f"Invalid input: {error_msg}")
        st.stop()

    # Calculate BMI with error handling
    try:
        bmi = BMICalculator.calculate(height, weight)
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
        gauge_fig = UIComponents.create_gauge(bmi)
        st.plotly_chart(gauge_fig, use_container_width=True)

    except ValueError as e:
        st.error(f"❌ Invalid BMI value: {e}")
        logger.error(f"ValueError in gauge creation: {e}")
        st.stop()

    except Exception as e:
        st.error("❌ Unable to display BMI gauge. Please try again.")
        logger.error(f"Error displaying gauge: {e}", exc_info=True)
        st.stop()

    # Get BMI category
    try:
        category, color, emoji = BMICalculator.get_category(bmi)
    except ValueError as e:
        st.error(f"❌ {str(e)}")
        logger.error(f"ValueError in category determination: {e}")
        st.stop()

    # Display results
    UIComponents.display_results(bmi, category, emoji)

    # Display BMI information
    UIComponents.display_bmi_info()

    # Display health tips
    UIComponents.display_health_tips(category)

    # Footer
    UIComponents.display_footer()

    logger.info("BMI Calculator session completed")


if __name__ == "__main__":
    main()
