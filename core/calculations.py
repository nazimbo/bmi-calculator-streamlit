"""BMI calculation and categorization logic."""

from typing import Tuple
from config.constants import config


class BMICalculator:
    """Handles BMI calculations and categorization.

    This class encapsulates all BMI-related calculations and provides
    methods for calculating BMI values and determining health categories.
    """

    @staticmethod
    def calculate(height_cm: float, weight_kg: float) -> float:
        """Calculate BMI from height and weight.

        Args:
            height_cm: Height in centimeters (must be positive)
            weight_kg: Weight in kilograms (must be positive)

        Returns:
            Calculated BMI value

        Raises:
            ValueError: If height or weight are invalid

        Example:
            >>> BMICalculator.calculate(170, 70)
            24.22
        """
        if height_cm <= 0 or weight_kg <= 0:
            raise ValueError("Height and weight must be positive values")

        if height_cm > config.HEIGHT_MAX_CM or weight_kg > config.WEIGHT_MAX_KG:
            raise ValueError("Height or weight values are unrealistic")

        # BMI formula: weight (kg) / (height (m))^2
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)

        return bmi

    @classmethod
    def get_category(cls, bmi: float) -> Tuple[str, str, str]:
        """Get BMI category, color, and emoji indicator.

        Args:
            bmi: The calculated BMI value

        Returns:
            Tuple of (category_name, color_hex, emoji)

        Raises:
            ValueError: If BMI is negative

        Example:
            >>> BMICalculator.get_category(22.0)
            ('Normal weight', '#2ECC71', '✅')
        """
        if bmi < 0:
            raise ValueError("BMI cannot be negative")

        if bmi < config.BMI_UNDERWEIGHT_THRESHOLD:
            return (
                config.CATEGORY_UNDERWEIGHT,
                config.COLOR_UNDERWEIGHT,
                config.EMOJI_UNDERWEIGHT
            )
        elif bmi < config.BMI_NORMAL_THRESHOLD:
            return (
                config.CATEGORY_NORMAL,
                config.COLOR_NORMAL,
                config.EMOJI_NORMAL
            )
        elif bmi < config.BMI_OVERWEIGHT_THRESHOLD:
            return (
                config.CATEGORY_OVERWEIGHT,
                config.COLOR_OVERWEIGHT,
                config.EMOJI_OVERWEIGHT
            )
        else:
            return (
                config.CATEGORY_OBESE,
                config.COLOR_OBESE,
                config.EMOJI_OBESE
            )

    @classmethod
    def validate_bmi(cls, bmi: float) -> bool:
        """Validate if BMI value is within realistic range.

        Args:
            bmi: The BMI value to validate

        Returns:
            True if BMI is valid, False otherwise

        Example:
            >>> BMICalculator.validate_bmi(25.0)
            True
            >>> BMICalculator.validate_bmi(-5.0)
            False
        """
        return 0 <= bmi <= config.BMI_MAX_REALISTIC
