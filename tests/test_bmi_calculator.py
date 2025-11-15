"""Unit tests for BMI Calculator functions."""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from bmi_calculator.core import (
    calculate_bmi,
    get_bmi_category,
    MIN_HEIGHT_CM,
    MAX_HEIGHT_CM,
    MIN_WEIGHT_KG,
    MAX_WEIGHT_KG,
)
from bmi_calculator.core.calculator import get_bmi_category_legacy
from bmi_calculator.ui import create_gauge


class TestCalculateBMI:
    """Test cases for calculate_bmi function."""

    def test_normal_bmi_calculation(self):
        """Test BMI calculation with normal values."""
        # Height: 170cm, Weight: 70kg
        # Expected BMI: 70 / (1.7)^2 = 24.22
        bmi = calculate_bmi(170, 70)
        assert pytest.approx(bmi, 0.01) == 24.22

    def test_underweight_bmi_calculation(self):
        """Test BMI calculation resulting in underweight category."""
        # Height: 180cm, Weight: 55kg
        # Expected BMI: 55 / (1.8)^2 = 16.98
        bmi = calculate_bmi(180, 55)
        assert pytest.approx(bmi, 0.01) == 16.98

    def test_overweight_bmi_calculation(self):
        """Test BMI calculation resulting in overweight category."""
        # Height: 165cm, Weight: 75kg
        # Expected BMI: 75 / (1.65)^2 = 27.55
        bmi = calculate_bmi(165, 75)
        assert pytest.approx(bmi, 0.01) == 27.55

    def test_obese_bmi_calculation(self):
        """Test BMI calculation resulting in obese category."""
        # Height: 160cm, Weight: 85kg
        # Expected BMI: 85 / (1.6)^2 = 33.20
        bmi = calculate_bmi(160, 85)
        assert pytest.approx(bmi, 0.01) == 33.20

    def test_zero_height_raises_error(self):
        """Test that zero height raises ValueError."""
        with pytest.raises(ValueError, match="Height and weight must be positive values"):
            calculate_bmi(0, 70)

    def test_negative_height_raises_error(self):
        """Test that negative height raises ValueError."""
        with pytest.raises(ValueError, match="Height and weight must be positive values"):
            calculate_bmi(-170, 70)

    def test_zero_weight_raises_error(self):
        """Test that zero weight raises ValueError."""
        with pytest.raises(ValueError, match="Height and weight must be positive values"):
            calculate_bmi(170, 0)

    def test_negative_weight_raises_error(self):
        """Test that negative weight raises ValueError."""
        with pytest.raises(ValueError, match="Height and weight must be positive values"):
            calculate_bmi(170, -70)

    def test_unrealistic_height_raises_error(self):
        """Test that unrealistic height values raise ValueError."""
        with pytest.raises(ValueError, match="Height must be between"):
            calculate_bmi(350, 70)

    def test_unrealistic_weight_raises_error(self):
        """Test that unrealistic weight values raise ValueError."""
        with pytest.raises(ValueError, match="Weight must be between"):
            calculate_bmi(170, 600)

    def test_minimum_valid_values(self):
        """Test BMI calculation with minimum valid values."""
        bmi = calculate_bmi(MIN_HEIGHT_CM, MIN_WEIGHT_KG)
        assert bmi == 10.0

    def test_maximum_valid_values(self):
        """Test BMI calculation with maximum valid values."""
        bmi = calculate_bmi(MAX_HEIGHT_CM, MAX_WEIGHT_KG)
        assert pytest.approx(bmi, 0.01) == 22.22

    def test_height_below_minimum(self):
        """Test that height below minimum raises error."""
        with pytest.raises(ValueError, match="Height must be between"):
            calculate_bmi(MIN_HEIGHT_CM - 1, 70)

    def test_height_above_maximum(self):
        """Test that height above maximum raises error."""
        with pytest.raises(ValueError, match="Height must be between"):
            calculate_bmi(MAX_HEIGHT_CM + 1, 70)

    def test_weight_below_minimum(self):
        """Test that weight below minimum raises error."""
        with pytest.raises(ValueError, match="Weight must be between"):
            calculate_bmi(170, MIN_WEIGHT_KG - 1)

    def test_weight_above_maximum(self):
        """Test that weight above maximum raises error."""
        with pytest.raises(ValueError, match="Weight must be between"):
            calculate_bmi(170, MAX_WEIGHT_KG + 1)


class TestGetBMICategory:
    """Test cases for get_bmi_category function."""

    def test_underweight_category(self):
        """Test underweight category (BMI < 18.5)."""
        category = get_bmi_category(17.0)
        assert category.name == "Underweight"
        assert category.color == "#FFC300"
        assert category.emoji == "⚠️"

    def test_underweight_boundary(self):
        """Test underweight boundary (BMI = 18.4)."""
        category = get_bmi_category(18.4)
        assert category.name == "Underweight"

    def test_normal_weight_category(self):
        """Test normal weight category (18.5 <= BMI < 24.9)."""
        category = get_bmi_category(22.0)
        assert category.name == "Normal weight"
        assert category.color == "#2ECC71"
        assert category.emoji == "✅"

    def test_normal_weight_lower_boundary(self):
        """Test normal weight lower boundary (BMI = 18.5)."""
        category = get_bmi_category(18.5)
        assert category.name == "Normal weight"

    def test_normal_weight_upper_boundary(self):
        """Test normal weight upper boundary (BMI = 24.8)."""
        category = get_bmi_category(24.8)
        assert category.name == "Normal weight"

    def test_overweight_category(self):
        """Test overweight category (25 <= BMI < 29.9)."""
        category = get_bmi_category(27.0)
        assert category.name == "Overweight"
        assert category.color == "#FF5733"
        assert category.emoji == "⚠️"

    def test_overweight_lower_boundary(self):
        """Test overweight lower boundary (BMI = 25.0)."""
        category = get_bmi_category(25.0)
        assert category.name == "Overweight"

    def test_overweight_upper_boundary(self):
        """Test overweight upper boundary (BMI = 29.8)."""
        category = get_bmi_category(29.8)
        assert category.name == "Overweight"

    def test_obese_category(self):
        """Test obese category (BMI >= 30)."""
        category = get_bmi_category(35.0)
        assert category.name == "Obese"
        assert category.color == "#C70039"
        assert category.emoji == "🚨"

    def test_obese_boundary(self):
        """Test obese boundary (BMI = 30.0)."""
        category = get_bmi_category(30.0)
        assert category.name == "Obese"

    def test_very_high_bmi(self):
        """Test very high BMI value."""
        category = get_bmi_category(50.0)
        assert category.name == "Obese"

    def test_negative_bmi_raises_error(self):
        """Test that negative BMI raises ValueError."""
        with pytest.raises(ValueError, match="BMI cannot be negative"):
            get_bmi_category(-5.0)


class TestGetBMICategoryLegacy:
    """Test backward compatibility of legacy tuple API."""

    def test_legacy_api_returns_tuple(self):
        """Test that legacy API returns tuple."""
        result = get_bmi_category_legacy(22.0)
        assert isinstance(result, tuple)
        assert len(result) == 3

    def test_legacy_api_underweight(self):
        """Test legacy API for underweight."""
        name, color, emoji = get_bmi_category_legacy(17.0)
        assert name == "Underweight"
        assert color == "#FFC300"
        assert emoji == "⚠️"

    def test_legacy_api_normal(self):
        """Test legacy API for normal weight."""
        name, color, emoji = get_bmi_category_legacy(22.0)
        assert name == "Normal weight"
        assert color == "#2ECC71"
        assert emoji == "✅"


class TestCreateGauge:
    """Test cases for create_gauge function."""

    def test_gauge_creation_normal_bmi(self):
        """Test gauge creation with normal BMI value."""
        fig = create_gauge(22.0)
        assert fig is not None
        assert fig.data[0].value == 22.0

    def test_gauge_creation_low_bmi(self):
        """Test gauge creation with low BMI value."""
        fig = create_gauge(15.0)
        assert fig is not None
        assert fig.data[0].value == 15.0

    def test_gauge_creation_high_bmi(self):
        """Test gauge creation with high BMI value."""
        fig = create_gauge(35.0)
        assert fig is not None
        assert fig.data[0].value == 35.0

    def test_gauge_rejects_negative_bmi(self):
        """Test that negative BMI raises ValueError."""
        with pytest.raises(ValueError, match="Invalid BMI value"):
            create_gauge(-5.0)

    def test_gauge_rejects_unrealistic_bmi(self):
        """Test that unrealistic BMI raises ValueError."""
        with pytest.raises(ValueError, match="Invalid BMI value"):
            create_gauge(150.0)

    def test_gauge_has_correct_structure(self):
        """Test gauge has correct Plotly structure."""
        fig = create_gauge(25.0)
        assert len(fig.data) == 1
        assert fig.data[0].type == "indicator"
        assert fig.data[0].mode == "gauge+number"

    def test_gauge_has_color_ranges(self):
        """Test gauge has BMI category color ranges."""
        fig = create_gauge(25.0)
        steps = fig.data[0].gauge.steps
        assert len(steps) == 4  # 4 BMI categories
        # Verify colors match BMI categories
        assert steps[0].color == "#FFC300"  # Underweight
        assert steps[1].color == "#2ECC71"  # Normal
        assert steps[2].color == "#FF5733"  # Overweight
        assert steps[3].color == "#C70039"  # Obese

    def test_gauge_boundary_values(self):
        """Test gauge with BMI boundary values."""
        # Test at 0 (minimum valid)
        fig = create_gauge(0.1)
        assert fig.data[0].value == 0.1

        # Test at 100 (maximum valid)
        fig = create_gauge(100.0)
        assert fig.data[0].value == 100.0

    def test_gauge_exact_boundary(self):
        """Test gauge at exact boundary (100)."""
        fig = create_gauge(100.0)
        assert fig.data[0].value == 100.0

    def test_gauge_just_above_boundary(self):
        """Test gauge just above boundary raises error."""
        with pytest.raises(ValueError, match="Invalid BMI value"):
            create_gauge(100.1)


class TestIntegration:
    """Integration tests combining calculate_bmi and get_bmi_category."""

    def test_full_underweight_flow(self):
        """Test full flow for underweight person."""
        bmi = calculate_bmi(180, 55)
        category = get_bmi_category(bmi)
        assert category.name == "Underweight"
        assert pytest.approx(bmi, 0.01) == 16.98

    def test_full_normal_weight_flow(self):
        """Test full flow for normal weight person."""
        bmi = calculate_bmi(170, 70)
        category = get_bmi_category(bmi)
        assert category.name == "Normal weight"
        assert pytest.approx(bmi, 0.01) == 24.22

    def test_full_overweight_flow(self):
        """Test full flow for overweight person."""
        bmi = calculate_bmi(165, 75)
        category = get_bmi_category(bmi)
        assert category.name == "Overweight"
        assert pytest.approx(bmi, 0.01) == 27.55

    def test_full_obese_flow(self):
        """Test full flow for obese person."""
        bmi = calculate_bmi(160, 85)
        category = get_bmi_category(bmi)
        assert category.name == "Obese"
        assert pytest.approx(bmi, 0.01) == 33.20

    def test_full_flow_with_visualization(self):
        """Test complete flow including gauge creation."""
        bmi = calculate_bmi(170, 70)
        category = get_bmi_category(bmi)
        gauge = create_gauge(bmi)

        assert category.name == "Normal weight"
        assert gauge.data[0].value == pytest.approx(bmi, 0.01)


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_very_short_person(self):
        """Test BMI for very short person (100cm)."""
        bmi = calculate_bmi(100, 30)
        assert bmi == 30.0

    def test_very_tall_person(self):
        """Test BMI for very tall person (300cm)."""
        bmi = calculate_bmi(300, 100)
        assert pytest.approx(bmi, 0.01) == 11.11

    def test_decimal_inputs(self):
        """Test BMI calculation with decimal inputs."""
        bmi = calculate_bmi(175.5, 72.3)
        assert pytest.approx(bmi, 0.01) == 23.47

    def test_bmi_boundary_18_5(self):
        """Test exact BMI boundary at 18.5."""
        # Find weight for 170cm to get exactly 18.5 BMI
        # BMI = weight / (1.7)^2
        # 18.5 = weight / 2.89
        # weight = 53.465
        bmi = calculate_bmi(170, 53.465)
        assert pytest.approx(bmi, 0.01) == 18.5
        category = get_bmi_category(18.5)
        assert category.name == "Normal weight"

    def test_bmi_boundary_24_9(self):
        """Test BMI at 24.9 (upper boundary of normal weight)."""
        bmi = calculate_bmi(170, 71.961)
        assert pytest.approx(bmi, 0.01) == 24.9
        # 24.9 is >= 24.9 threshold, so it's Overweight
        category = get_bmi_category(24.9)
        assert category.name == "Overweight"

    def test_bmi_boundary_29_9(self):
        """Test BMI at 29.9 (upper boundary of overweight)."""
        bmi = calculate_bmi(170, 86.411)
        assert pytest.approx(bmi, 0.01) == 29.9
        # 29.9 is >= 29.9 threshold, so it's Obese
        category = get_bmi_category(29.9)
        assert category.name == "Obese"
