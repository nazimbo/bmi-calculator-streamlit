"""Configuration constants for BMI Calculator.

This module contains all configuration values, validation constants,
and BMI category definitions to avoid hardcoding throughout the application.
"""

from dataclasses import dataclass
from typing import List


# Input validation constants
MIN_HEIGHT_CM = 100
MAX_HEIGHT_CM = 300
MIN_WEIGHT_KG = 10
MAX_WEIGHT_KG = 200  # Realistic maximum for general population

# Default UI values
DEFAULT_HEIGHT_CM = 170
DEFAULT_WEIGHT_KG = 70

# Logging configuration
LOG_FILE_NAME = "bmi_calculator.log"
LOG_FILE_MAX_BYTES = 10 * 1024 * 1024  # 10MB
LOG_FILE_BACKUP_COUNT = 5
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Gauge visualization constants
GAUGE_MAX_BMI = 40
GAUGE_HEIGHT_PX = 300
GAUGE_MARGIN = {"l": 10, "r": 10, "t": 40, "b": 10}


@dataclass
class BMICategory:
    """Data class representing a BMI category with its properties."""

    name: str
    threshold: float  # Upper threshold for this category
    color: str  # Hex color code
    emoji: str  # Visual indicator
    description: str  # Longer description


# BMI Categories based on WHO standards
BMI_CATEGORIES: List[BMICategory] = [
    BMICategory(
        name="Underweight",
        threshold=18.5,
        color="#FFC300",
        emoji="⚠️",
        description="Below normal weight range",
    ),
    BMICategory(
        name="Normal weight",
        threshold=24.9,
        color="#2ECC71",
        emoji="✅",
        description="Healthy weight range",
    ),
    BMICategory(
        name="Overweight",
        threshold=29.9,
        color="#FF5733",
        emoji="⚠️",
        description="Above normal weight range",
    ),
    BMICategory(
        name="Obese",
        threshold=float("inf"),
        color="#C70039",
        emoji="🚨",
        description="Significantly above normal weight range",
    ),
]

# Health tips by category
HEALTH_TIPS = {
    "Underweight": """
### Tips for Healthy Weight Gain:
- Eat more frequently throughout the day
- Choose nutrient-rich foods
- Add healthy snacks between meals
- Include protein with every meal
- Consider strength training exercises
""",
    "Normal weight": """
### Tips to Maintain Healthy Weight:
- Keep up your balanced diet
- Stay physically active
- Get adequate sleep
- Stay hydrated
- Monitor your weight regularly
""",
    "Overweight": """
### Tips for Weight Management:
- Increase physical activity
- Control portion sizes
- Choose whole foods over processed foods
- Track your daily calorie intake
- Consider consulting a nutritionist
""",
    "Obese": """
### Tips for Weight Loss:
- Consult with healthcare professionals
- Start with moderate exercise
- Focus on portion control
- Keep a food diary
- Set realistic goals
""",
}

# Medical disclaimer
MEDICAL_DISCLAIMER = (
    "ℹ️ Remember: BMI is just one measure of health. "
    "Always consult with healthcare professionals for medical advice."
)

# App metadata
APP_TITLE = "⚕️ Body Mass Index (BMI) Calculator"
APP_ICON = "⚕️"
APP_LAYOUT = "centered"
