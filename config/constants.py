"""Configuration constants for BMI Calculator application."""

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class BMIConfig:
    """BMI Calculator configuration constants.

    This class contains all configuration values used throughout the application.
    Using a frozen dataclass ensures these values cannot be modified at runtime.
    """

    # Input validation ranges
    HEIGHT_MIN_CM: int = 100
    HEIGHT_MAX_CM: int = 300
    HEIGHT_DEFAULT_CM: int = 170

    WEIGHT_MIN_KG: int = 10
    WEIGHT_MAX_KG: int = 500
    WEIGHT_DEFAULT_KG: int = 70

    # BMI thresholds (WHO standard)
    BMI_UNDERWEIGHT_THRESHOLD: float = 18.5
    BMI_NORMAL_THRESHOLD: float = 24.9
    BMI_OVERWEIGHT_THRESHOLD: float = 29.9
    BMI_MAX_REALISTIC: float = 100.0

    # UI Configuration
    GAUGE_MAX_VALUE: int = 40
    CHART_HEIGHT: int = 300
    PAGE_LAYOUT: str = "centered"
    PAGE_TITLE: str = "BMI Calculator"
    PAGE_ICON: str = "⚕️"

    # Color scheme for BMI categories
    COLOR_UNDERWEIGHT: str = "#FFC300"  # Yellow
    COLOR_NORMAL: str = "#2ECC71"       # Green
    COLOR_OVERWEIGHT: str = "#FF5733"   # Orange
    COLOR_OBESE: str = "#C70039"        # Red

    # Emoji indicators
    EMOJI_UNDERWEIGHT: str = "⚠️"
    EMOJI_NORMAL: str = "✅"
    EMOJI_OVERWEIGHT: str = "⚠️"
    EMOJI_OBESE: str = "🚨"

    # Logging configuration
    LOG_FILE: str = "bmi_calculator.log"
    LOG_MAX_BYTES: int = 10485760  # 10MB
    LOG_BACKUP_COUNT: int = 5
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    LOG_LEVEL: str = "INFO"

    # Category names
    CATEGORY_UNDERWEIGHT: str = "Underweight"
    CATEGORY_NORMAL: str = "Normal weight"
    CATEGORY_OVERWEIGHT: str = "Overweight"
    CATEGORY_OBESE: str = "Obese"

    @property
    def colors(self) -> Dict[str, str]:
        """Get all colors as a dictionary."""
        return {
            'underweight': self.COLOR_UNDERWEIGHT,
            'normal': self.COLOR_NORMAL,
            'overweight': self.COLOR_OVERWEIGHT,
            'obese': self.COLOR_OBESE
        }

    @property
    def emojis(self) -> Dict[str, str]:
        """Get all emojis as a dictionary."""
        return {
            'underweight': self.EMOJI_UNDERWEIGHT,
            'normal': self.EMOJI_NORMAL,
            'overweight': self.EMOJI_OVERWEIGHT,
            'obese': self.EMOJI_OBESE
        }

    @property
    def categories(self) -> Dict[str, str]:
        """Get all category names as a dictionary."""
        return {
            'underweight': self.CATEGORY_UNDERWEIGHT,
            'normal': self.CATEGORY_NORMAL,
            'overweight': self.CATEGORY_OVERWEIGHT,
            'obese': self.CATEGORY_OBESE
        }


# Create a singleton instance
config = BMIConfig()
