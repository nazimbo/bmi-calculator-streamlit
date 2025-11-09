"""Input validation logic for BMI Calculator."""

from typing import Tuple
from config.constants import config


class InputValidator:
    """Validates user inputs for BMI calculation.

    This class provides validation methods to ensure user inputs
    are within acceptable ranges for BMI calculations.
    """

    @staticmethod
    def validate_height(height_cm: float) -> Tuple[bool, str]:
        """Validate height input.

        Args:
            height_cm: Height value in centimeters

        Returns:
            Tuple of (is_valid, error_message)
            If valid, error_message is empty string

        Example:
            >>> InputValidator.validate_height(170)
            (True, '')
            >>> InputValidator.validate_height(50)
            (False, 'Height is too low...')
        """
        if height_cm <= 0:
            return False, "Height must be a positive value."

        if height_cm < config.HEIGHT_MIN_CM:
            return (
                False,
                f"Height seems too low. Please enter a value between "
                f"{config.HEIGHT_MIN_CM} and {config.HEIGHT_MAX_CM} cm."
            )

        if height_cm > config.HEIGHT_MAX_CM:
            return (
                False,
                f"Height exceeds realistic human range. Maximum allowed: "
                f"{config.HEIGHT_MAX_CM} cm."
            )

        return True, ""

    @staticmethod
    def validate_weight(weight_kg: float) -> Tuple[bool, str]:
        """Validate weight input.

        Args:
            weight_kg: Weight value in kilograms

        Returns:
            Tuple of (is_valid, error_message)
            If valid, error_message is empty string

        Example:
            >>> InputValidator.validate_weight(70)
            (True, '')
            >>> InputValidator.validate_weight(5)
            (False, 'Weight is too low...')
        """
        if weight_kg <= 0:
            return False, "Weight must be a positive value."

        if weight_kg < config.WEIGHT_MIN_KG:
            return (
                False,
                f"Weight seems too low. Please enter a value between "
                f"{config.WEIGHT_MIN_KG} and {config.WEIGHT_MAX_KG} kg."
            )

        if weight_kg > config.WEIGHT_MAX_KG:
            return (
                False,
                f"Weight exceeds realistic range. Maximum allowed: "
                f"{config.WEIGHT_MAX_KG} kg."
            )

        return True, ""

    @classmethod
    def validate_inputs(cls, height_cm: float, weight_kg: float) -> Tuple[bool, str]:
        """Validate both height and weight inputs.

        Args:
            height_cm: Height value in centimeters
            weight_kg: Weight value in kilograms

        Returns:
            Tuple of (is_valid, error_message)
            If valid, error_message is empty string

        Example:
            >>> InputValidator.validate_inputs(170, 70)
            (True, '')
        """
        # Validate height first
        is_valid, error_msg = cls.validate_height(height_cm)
        if not is_valid:
            return False, error_msg

        # Then validate weight
        is_valid, error_msg = cls.validate_weight(weight_kg)
        if not is_valid:
            return False, error_msg

        return True, ""
