"""UI components for the BMI Calculator.

This module contains reusable UI components like charts and visualizations.
"""

import plotly.graph_objects as go

from ..core.constants import GAUGE_MAX_BMI, GAUGE_HEIGHT_PX, GAUGE_MARGIN, BMI_CATEGORIES
from ..utils.logger import get_logger

logger = get_logger(__name__)


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
        # Build color steps from BMI_CATEGORIES
        steps = []
        prev_threshold = 0.0
        for category in BMI_CATEGORIES:
            # Use min to cap at GAUGE_MAX_BMI for display
            upper = min(category.threshold, GAUGE_MAX_BMI)
            if upper > prev_threshold:
                steps.append({"range": [prev_threshold, upper], "color": category.color})
                prev_threshold = upper
            if upper >= GAUGE_MAX_BMI:
                break

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=bmi_value,
                domain={"x": [0, 1], "y": [0, 1]},
                gauge={
                    "axis": {"range": [None, GAUGE_MAX_BMI], "tickwidth": 1},
                    "bar": {"color": "darkblue"},
                    "steps": steps,
                    "threshold": {
                        "line": {"color": "red", "width": 4},
                        "thickness": 0.75,
                        "value": bmi_value,
                    },
                },
            )
        )

        fig.update_layout(
            height=GAUGE_HEIGHT_PX,
            margin=GAUGE_MARGIN,
            font={"color": "#2E4053", "family": "Arial"},
        )

        return fig

    except Exception as e:
        logger.error(f"Error creating gauge chart: {e}", exc_info=True)
        raise
