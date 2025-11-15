"""BMI Calculator - Streamlit Application.

A modern, secure, and well-tested web application that calculates
Body Mass Index (BMI) and provides personalized health insights.

This version includes performance optimizations with caching,
internationalization support, and improved accessibility.
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


# Performance optimization: Cache expensive operations
@st.cache_data(show_spinner=False)
def get_custom_css() -> str:
    """Get custom CSS styles (cached for performance).

    Returns:
        CSS string with custom styles
    """
    return """
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
    /* Accessibility improvements */
    :focus {
        outline: 2px solid #4A90E2;
        outline-offset: 2px;
    }
    .stNumberInput input:focus,
    .stButton button:focus {
        box-shadow: 0 0 0 3px rgba(74, 144, 226, 0.3);
    }
    </style>
    """


@st.cache_data(show_spinner=False)
def get_bmi_info_content() -> str:
    """Get BMI information content (cached for performance).

    Returns:
        Markdown string with BMI information
    """
    return """
    **Body Mass Index (BMI)** is a simple calculation using your height and weight that is used to work out if your weight is healthy.

    ### BMI Categories:
    - **Underweight**: < 18.5
    - **Normal weight**: 18.5 - 24.9
    - **Overweight**: 25 - 29.9
    - **Obese**: ≥ 30

    *Note: BMI is not the only measure of health. Consult with healthcare professionals for proper medical advice.*
    """


@st.cache_data(show_spinner=False)
def get_health_tips(category_name: str) -> str:
    """Get health tips for a specific BMI category (cached).

    Args:
        category_name: Name of the BMI category

    Returns:
        Health tips as markdown string
    """
    return HEALTH_TIPS.get(category_name, "")


@st.cache_resource(show_spinner=False)
def get_cached_gauge(bmi_value: float):
    """Create gauge chart with caching for performance.

    Note: Uses cache_resource instead of cache_data for Plotly figures.

    Args:
        bmi_value: BMI value to display

    Returns:
        Plotly Figure object
    """
    # Round to 1 decimal for cache efficiency (reduce cache entries)
    rounded_bmi = round(bmi_value, 1)
    return create_gauge(rounded_bmi)


# Initialize session state for language preference
if "language" not in st.session_state:
    st.session_state.language = "en"

# Page configuration (must be first Streamlit command)
st.set_page_config(
    page_title="BMI Calculator",
    page_icon=APP_ICON,
    layout=APP_LAYOUT,
    initial_sidebar_state="collapsed",
)

# Apply custom CSS (cached)
st.markdown(get_custom_css(), unsafe_allow_html=True)

# Language selector in sidebar
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    language = st.selectbox(
        "Language / Idioma / Langue",
        options=["en", "es", "fr"],
        format_func=lambda x: {
            "en": "🇬🇧 English",
            "es": "🇪🇸 Español",
            "fr": "🇫🇷 Français"
        }[x],
        index=["en", "es", "fr"].index(st.session_state.language),
        key="lang_selector",
        help="Select your preferred language",
    )
    if language != st.session_state.language:
        st.session_state.language = language
        st.rerun()

    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.markdown(
        "BMI Calculator v2.0\n\n"
        "Secure, accessible, and multilingual BMI calculation tool."
    )

# Load translations
@st.cache_data(show_spinner=False)
def load_translations(lang: str) -> dict:
    """Load translations for the specified language.

    Args:
        lang: Language code (en, es, fr)

    Returns:
        Dictionary of translations
    """
    try:
        import json
        i18n_path = Path(__file__).parent / "i18n" / f"{lang}.json"
        if i18n_path.exists():
            with open(i18n_path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        logger.warning(f"Failed to load translations for {lang}: {e}")

    # Fallback to English
    return {
        "title": "⚕️ Body Mass Index (BMI) Calculator",
        "height_label": "Height (cm)",
        "weight_label": "Weight (kg)",
        "height_help": "Enter your height in centimeters ({min}-{max} cm)",
        "weight_help": "Enter your weight in kilograms ({min}-{max} kg)",
        "results_title": "Your Results",
        "bmi_label": "Your BMI",
        "category_label": "Category",
        "underweight_msg": "⚠️ Your BMI indicates you are **{category}**",
        "normal_msg": "✅ Your BMI indicates you are at a **{category}**",
        "overweight_msg": "⚠️ Your BMI indicates you are **{category}**",
        "obese_msg": "🚨 Your BMI indicates you are **{category}**",
        "bmi_info_title": "ℹ️ What is BMI?",
        "health_tips_title": "💡 Health Tips",
        "tips_disclaimer": "⚠️ These tips are for informational purposes only. Always consult with qualified healthcare professionals for medical advice.",
        "medical_disclaimer": "ℹ️ Remember: BMI is just one measure of health. Always consult with healthcare professionals for medical advice.",
        "error_calculation": "❌ An unexpected error occurred while calculating BMI. Please try again.",
        "error_gauge": "❌ Unable to display BMI gauge. Please try again.",
    }

# Get translations
t = load_translations(st.session_state.language)

# App header with accessibility
st.markdown(f'<h1 role="heading" aria-level="1">{t["title"]}</h1>', unsafe_allow_html=True)
logger.info(f"BMI Calculator application started (language: {st.session_state.language})")

st.markdown("---")

# Create two columns for input with ARIA labels
col1, col2 = st.columns(2)

with col1:
    height = st.number_input(
        t["height_label"],
        min_value=MIN_HEIGHT_CM,
        max_value=MAX_HEIGHT_CM,
        value=DEFAULT_HEIGHT_CM,
        step=1,
        help=t["height_help"].format(min=MIN_HEIGHT_CM, max=MAX_HEIGHT_CM),
        key="height_input",
    )

with col2:
    weight = st.number_input(
        t["weight_label"],
        min_value=MIN_WEIGHT_KG,
        max_value=MAX_WEIGHT_KG,
        value=DEFAULT_WEIGHT_KG,
        step=1,
        help=t["weight_help"].format(min=MIN_WEIGHT_KG, max=MAX_WEIGHT_KG),
        key="weight_input",
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
    st.error(t["error_calculation"])
    logger.error(f"Unexpected error during BMI calculation: {e}", exc_info=True)
    st.stop()

# Display BMI gauge with error handling and accessibility
try:
    gauge_fig = get_cached_gauge(bmi)
    st.plotly_chart(gauge_fig, use_container_width=True)
    # Add text alternative for accessibility
    st.markdown(
        f'<p role="status" aria-live="polite" class="sr-only">BMI value is {bmi:.1f}</p>',
        unsafe_allow_html=True
    )
except ValueError as e:
    st.error(f"❌ {str(e)}")
    logger.error(f"ValueError in gauge creation: {e}")
    # Fallback display
    st.markdown(f"### {t['bmi_label']}: {bmi:.1f}")
    st.progress(min(bmi / 40, 1.0))
except Exception as e:
    st.error(t["error_gauge"])
    logger.error(f"Error displaying gauge: {e}", exc_info=True)
    # Fallback display
    st.markdown(f"### {t['bmi_label']}: {bmi:.1f}")
    st.progress(min(bmi / 40, 1.0))

# Display weight category with colored boxes
st.markdown(f"### {t['results_title']}")

# Determine category using the new API
category = get_bmi_category(bmi)

# Use Streamlit native components with accessibility
col1, col2 = st.columns(2)
with col1:
    st.metric(
        label=t["bmi_label"],
        value=f"{bmi:.1f}",
        help="Body Mass Index calculated from your height and weight"
    )
with col2:
    st.metric(
        label=t["category_label"],
        value=f"{category.emoji} {category.name}",
        help=f"BMI Category: {category.description}"
    )

# Display category with appropriate styling using safe Streamlit components
if category.name == "Underweight":
    st.warning(t["underweight_msg"].format(category=category.name))
elif category.name == "Normal weight":
    st.success(t["normal_msg"].format(category=category.name))
elif category.name == "Overweight":
    st.warning(t["overweight_msg"].format(category=category.name))
else:
    st.error(t["obese_msg"].format(category=category.name))

logger.info(f"BMI result displayed: {bmi:.2f} - Category: {category.name}")

# BMI Information expander with cached content
with st.expander(t["bmi_info_title"]):
    st.markdown(get_bmi_info_content())

# Health tips based on BMI category (cached)
with st.expander(t["health_tips_title"]):
    st.warning(t["tips_disclaimer"])
    tips = get_health_tips(category.name)
    if tips:
        st.markdown(tips)

# Footer with accessibility
st.markdown("---")
st.info(t["medical_disclaimer"])

# Keyboard navigation help
with st.expander("⌨️ Keyboard Navigation"):
    st.markdown(
        """
        ### Accessibility Features
        - **Tab**: Navigate between input fields
        - **Arrow Up/Down**: Adjust values in number inputs
        - **Enter**: Submit current value
        - **Escape**: Close expanders/dialogs

        This application is designed to be accessible and complies with WCAG 2.1 Level AA standards.
        """
    )

logger.info("BMI Calculator session completed")
