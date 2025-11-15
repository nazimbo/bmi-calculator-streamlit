"""Core business logic for BMI calculations."""

from .calculator import calculate_bmi, get_bmi_category
from .constants import (
    MIN_HEIGHT_CM,
    MAX_HEIGHT_CM,
    MIN_WEIGHT_KG,
    MAX_WEIGHT_KG,
    BMI_CATEGORIES,
)

__all__ = [
    "calculate_bmi",
    "get_bmi_category",
    "MIN_HEIGHT_CM",
    "MAX_HEIGHT_CM",
    "MIN_WEIGHT_KG",
    "MAX_WEIGHT_KG",
    "BMI_CATEGORIES",
]
