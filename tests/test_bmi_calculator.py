"""Unit tests for BMI Calculator functions."""

import pytest
import sys
from pathlib import Path

# Add parent directory to path to import app module
sys.path.insert(0, str(Path(__file__).parent.parent))

from app import calculate_bmi, get_bmi_category


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
        with pytest.raises(ValueError, match="Height or weight values are unrealistic"):
            calculate_bmi(350, 70)

    def test_unrealistic_weight_raises_error(self):
        """Test that unrealistic weight values raise ValueError."""
        with pytest.raises(ValueError, match="Height or weight values are unrealistic"):
            calculate_bmi(170, 600)

    def test_minimum_valid_values(self):
        """Test BMI calculation with minimum valid values."""
        bmi = calculate_bmi(100, 10)
        assert bmi == 10.0

    def test_maximum_valid_values(self):
        """Test BMI calculation with maximum valid values."""
        bmi = calculate_bmi(300, 500)
        assert pytest.approx(bmi, 0.01) == 55.56


class TestGetBMICategory:
    """Test cases for get_bmi_category function."""

    def test_underweight_category(self):
        """Test underweight category (BMI < 18.5)."""
        category, color, emoji = get_bmi_category(17.0)
        assert category == "Underweight"
        assert color == "#FFC300"
        assert emoji == "⚠️"

    def test_underweight_boundary(self):
        """Test underweight boundary (BMI = 18.4)."""
        category, color, emoji = get_bmi_category(18.4)
        assert category == "Underweight"

    def test_normal_weight_category(self):
        """Test normal weight category (18.5 <= BMI < 24.9)."""
        category, color, emoji = get_bmi_category(22.0)
        assert category == "Normal weight"
        assert color == "#2ECC71"
        assert emoji == "✅"

    def test_normal_weight_lower_boundary(self):
        """Test normal weight lower boundary (BMI = 18.5)."""
        category, color, emoji = get_bmi_category(18.5)
        assert category == "Normal weight"

    def test_normal_weight_upper_boundary(self):
        """Test normal weight upper boundary (BMI = 24.8)."""
        category, color, emoji = get_bmi_category(24.8)
        assert category == "Normal weight"

    def test_overweight_category(self):
        """Test overweight category (25 <= BMI < 29.9)."""
        category, color, emoji = get_bmi_category(27.0)
        assert category == "Overweight"
        assert color == "#FF5733"
        assert emoji == "⚠️"

    def test_overweight_lower_boundary(self):
        """Test overweight lower boundary (BMI = 25.0)."""
        category, color, emoji = get_bmi_category(25.0)
        assert category == "Overweight"

    def test_overweight_upper_boundary(self):
        """Test overweight upper boundary (BMI = 29.8)."""
        category, color, emoji = get_bmi_category(29.8)
        assert category == "Overweight"

    def test_obese_category(self):
        """Test obese category (BMI >= 30)."""
        category, color, emoji = get_bmi_category(35.0)
        assert category == "Obese"
        assert color == "#C70039"
        assert emoji == "🚨"

    def test_obese_boundary(self):
        """Test obese boundary (BMI = 30.0)."""
        category, color, emoji = get_bmi_category(30.0)
        assert category == "Obese"

    def test_very_high_bmi(self):
        """Test very high BMI value."""
        category, color, emoji = get_bmi_category(50.0)
        assert category == "Obese"

    def test_negative_bmi_raises_error(self):
        """Test that negative BMI raises ValueError."""
        with pytest.raises(ValueError, match="BMI cannot be negative"):
            get_bmi_category(-5.0)


class TestIntegration:
    """Integration tests combining calculate_bmi and get_bmi_category."""

    def test_full_underweight_flow(self):
        """Test full flow for underweight person."""
        bmi = calculate_bmi(180, 55)
        category, color, emoji = get_bmi_category(bmi)
        assert category == "Underweight"
        assert pytest.approx(bmi, 0.01) == 16.98

    def test_full_normal_weight_flow(self):
        """Test full flow for normal weight person."""
        bmi = calculate_bmi(170, 70)
        category, color, emoji = get_bmi_category(bmi)
        assert category == "Normal weight"
        assert pytest.approx(bmi, 0.01) == 24.22

    def test_full_overweight_flow(self):
        """Test full flow for overweight person."""
        bmi = calculate_bmi(165, 75)
        category, color, emoji = get_bmi_category(bmi)
        assert category == "Overweight"
        assert pytest.approx(bmi, 0.01) == 27.55

    def test_full_obese_flow(self):
        """Test full flow for obese person."""
        bmi = calculate_bmi(160, 85)
        category, color, emoji = get_bmi_category(bmi)
        assert category == "Obese"
        assert pytest.approx(bmi, 0.01) == 33.20


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_very_short_person(self):
        """Test BMI for very short person (100cm)."""
        bmi = calculate_bmi(100, 30)
        assert bmi == 30.0

    def test_very_tall_person(self):
        """Test BMI for very tall person (250cm)."""
        bmi = calculate_bmi(250, 100)
        assert bmi == 16.0

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
        category, _, _ = get_bmi_category(18.5)
        assert category == "Normal weight"

    def test_bmi_boundary_24_9(self):
        """Test exact BMI boundary at 24.9."""
        bmi = calculate_bmi(170, 71.961)
        assert pytest.approx(bmi, 0.01) == 24.9
        category, _, _ = get_bmi_category(24.9)
        assert category == "Normal weight"

    def test_bmi_boundary_29_9(self):
        """Test exact BMI boundary at 29.9."""
        bmi = calculate_bmi(170, 86.411)
        assert pytest.approx(bmi, 0.01) == 29.9
        category, _, _ = get_bmi_category(29.9)
        assert category == "Overweight"
