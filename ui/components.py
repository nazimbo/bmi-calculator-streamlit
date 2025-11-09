"""UI components for BMI Calculator application."""

import streamlit as st
import plotly.graph_objects as go
from typing import Tuple
import logging

from config.constants import config

logger = logging.getLogger(__name__)


class UIComponents:
    """Handles UI rendering and visualization components.

    This class contains all methods for creating and displaying
    UI elements in the BMI Calculator application.
    """

    @staticmethod
    def create_gauge(bmi_value: float) -> go.Figure:
        """Create an interactive gauge chart displaying BMI value.

        The gauge uses color-coded ranges to indicate health categories:
        - Yellow (0-18.5): Underweight
        - Green (18.5-24.9): Normal weight
        - Orange (25-29.9): Overweight
        - Red (30+): Obese

        Args:
            bmi_value: The calculated Body Mass Index value

        Returns:
            A Plotly Figure object configured as an indicator gauge

        Raises:
            ValueError: If bmi_value is negative or unreasonably high

        Example:
            >>> fig = UIComponents.create_gauge(22.5)
            >>> st.plotly_chart(fig, use_container_width=True)
        """
        if bmi_value < 0 or bmi_value > config.BMI_MAX_REALISTIC:
            raise ValueError(f"Invalid BMI value: {bmi_value}")

        try:
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=bmi_value,
                domain={'x': [0, 1], 'y': [0, 1]},
                gauge={
                    'axis': {
                        'range': [None, config.GAUGE_MAX_VALUE],
                        'tickwidth': 1
                    },
                    'bar': {'color': "darkblue"},
                    'steps': [
                        {
                            'range': [0, config.BMI_UNDERWEIGHT_THRESHOLD],
                            'color': config.COLOR_UNDERWEIGHT
                        },
                        {
                            'range': [config.BMI_UNDERWEIGHT_THRESHOLD, config.BMI_NORMAL_THRESHOLD],
                            'color': config.COLOR_NORMAL
                        },
                        {
                            'range': [config.BMI_NORMAL_THRESHOLD, config.BMI_OVERWEIGHT_THRESHOLD],
                            'color': config.COLOR_OVERWEIGHT
                        },
                        {
                            'range': [config.BMI_OVERWEIGHT_THRESHOLD, config.GAUGE_MAX_VALUE],
                            'color': config.COLOR_OBESE
                        },
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': bmi_value
                    }
                }
            ))

            fig.update_layout(
                height=config.CHART_HEIGHT,
                margin=dict(l=10, r=10, t=40, b=10),
                font={'color': "#2E4053", 'family': "Arial"}
            )
            return fig

        except Exception as e:
            logger.error(f"Error creating gauge chart: {e}", exc_info=True)
            raise

    @staticmethod
    def display_results(bmi: float, category: str, emoji: str) -> None:
        """Display BMI results with metrics and category indicator.

        Args:
            bmi: The calculated BMI value
            category: The BMI category name
            emoji: The emoji indicator for the category

        Example:
            >>> UIComponents.display_results(22.5, "Normal weight", "✅")
        """
        st.markdown("### Your Results")

        # Display BMI and category in two columns
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Your BMI", value=f"{bmi:.1f}")
        with col2:
            st.metric(label="Category", value=f"{emoji} {category}")

        # Display category-specific message
        if category == config.CATEGORY_UNDERWEIGHT:
            st.warning(f"⚠️ Your BMI indicates you are **{category}**")
        elif category == config.CATEGORY_NORMAL:
            st.success(f"✅ Your BMI indicates you are at a **{category}**")
        elif category == config.CATEGORY_OVERWEIGHT:
            st.warning(f"⚠️ Your BMI indicates you are **{category}**")
        else:  # Obese
            st.error(f"🚨 Your BMI indicates you are **{category}**")

        logger.info(f"BMI result displayed: {bmi:.2f} - Category: {category}")

    @staticmethod
    def display_bmi_info() -> None:
        """Display BMI information in an expandable section."""
        with st.expander("ℹ️ What is BMI?"):
            st.markdown(f"""
                **Body Mass Index (BMI)** is a simple calculation using your height and weight
                that is used to work out if your weight is healthy.

                ### BMI Categories:
                - **Underweight**: < {config.BMI_UNDERWEIGHT_THRESHOLD}
                - **Normal weight**: {config.BMI_UNDERWEIGHT_THRESHOLD} - {config.BMI_NORMAL_THRESHOLD}
                - **Overweight**: {config.BMI_NORMAL_THRESHOLD + 0.1} - {config.BMI_OVERWEIGHT_THRESHOLD}
                - **Obese**: ≥ {config.BMI_OVERWEIGHT_THRESHOLD + 0.1}

                *Note: BMI is not the only measure of health. Consult with healthcare
                professionals for proper medical advice.*
            """)

    @staticmethod
    def display_health_tips(category: str) -> None:
        """Display health tips based on BMI category.

        Args:
            category: The BMI category name

        Example:
            >>> UIComponents.display_health_tips("Normal weight")
        """
        with st.expander("💡 Health Tips"):
            if category == config.CATEGORY_UNDERWEIGHT:
                st.markdown("""
                    ### Tips for Healthy Weight Gain:
                    - Eat more frequently throughout the day
                    - Choose nutrient-rich foods
                    - Add healthy snacks between meals
                    - Include protein with every meal
                    - Consider strength training exercises
                """)
            elif category == config.CATEGORY_NORMAL:
                st.markdown("""
                    ### Tips to Maintain Healthy Weight:
                    - Keep up your balanced diet
                    - Stay physically active
                    - Get adequate sleep
                    - Stay hydrated
                    - Monitor your weight regularly
                """)
            elif category == config.CATEGORY_OVERWEIGHT:
                st.markdown("""
                    ### Tips for Weight Management:
                    - Increase physical activity
                    - Control portion sizes
                    - Choose whole foods over processed foods
                    - Track your daily calorie intake
                    - Consider consulting a nutritionist
                """)
            else:  # Obese
                st.markdown("""
                    ### Tips for Weight Loss:
                    - Consult with healthcare professionals
                    - Start with moderate exercise
                    - Focus on portion control
                    - Keep a food diary
                    - Set realistic goals
                """)

    @staticmethod
    def display_footer() -> None:
        """Display application footer with disclaimer."""
        st.markdown("---")
        st.info(
            "ℹ️ Remember: BMI is just one measure of health. "
            "Always consult with healthcare professionals for medical advice."
        )
