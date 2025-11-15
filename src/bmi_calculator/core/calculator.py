"""Core BMI calculation functions.

This module contains the business logic for BMI calculations,
extracted from the UI layer for better testability and reusability.
"""

from typing import Tuple

from .constants import (
    MIN_HEIGHT_CM,
    MAX_HEIGHT_CM,
    MIN_WEIGHT_KG,
    MAX_WEIGHT_KG,
    BMI_CATEGORIES,
    BMICategory,
)


def calculate_bmi(height_cm: float, weight_kg: float) -> float:
    """Calculate BMI from height and weight.

    Args:
        height_cm: Height in centimeters
        weight_kg: Weight in kilograms

    Returns:
        Calculated BMI value

    Raises:
        ValueError: If height or weight are invalid or outside realistic ranges
    """
    # Validate positive values
    if height_cm <= 0 or weight_kg <= 0:
        raise ValueError("Height and weight must be positive values")

    # Validate realistic ranges (aligned with UI constraints)
    if not (MIN_HEIGHT_CM <= height_cm <= MAX_HEIGHT_CM):
        raise ValueError(
            f"Height must be between {MIN_HEIGHT_CM}-{MAX_HEIGHT_CM} cm. "
            f"Received: {height_cm} cm"
        )

    if not (MIN_WEIGHT_KG <= weight_kg <= MAX_WEIGHT_KG):
        raise ValueError(
            f"Weight must be between {MIN_WEIGHT_KG}-{MAX_WEIGHT_KG} kg. "
            f"Received: {weight_kg} kg"
        )

    # Calculate BMI: weight (kg) / height (m)^2
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)

    return bmi


def get_bmi_category(bmi: float) -> BMICategory:
    """Get BMI category with all associated properties.

    Args:
        bmi: The BMI value

    Returns:
        BMICategory object with name, color, emoji, and description

    Raises:
        ValueError: If BMI is negative
    """
    if bmi < 0:
        raise ValueError(f"BMI cannot be negative. Received: {bmi}")

    # Find the appropriate category
    for category in BMI_CATEGORIES:
        if bmi < category.threshold:
            return category

    # Fallback to last category (should never reach here due to inf threshold)
    return BMI_CATEGORIES[-1]


def get_bmi_category_legacy(bmi: float) -> Tuple[str, str, str]:
    """Get BMI category as tuple (for backward compatibility).

    This function maintains backward compatibility with the old API.
    New code should use get_bmi_category() instead.

    Args:
        bmi: The BMI value

    Returns:
        Tuple of (category_name, color, emoji)

    Raises:
        ValueError: If BMI is negative
    """
    category = get_bmi_category(bmi)
    return (category.name, category.color, category.emoji)
