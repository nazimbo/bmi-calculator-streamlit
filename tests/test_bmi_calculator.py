"""Unit tests for BMI Calculator functions using the new modular structure."""

import pytest
from core.calculations import BMICalculator
from core.validators import InputValidator
from config.constants import config


class TestBMICalculator:
    """Test cases for BMICalculator class."""

    def test_normal_bmi_calculation(self):
        """Test BMI calculation with normal values."""
        # Height: 170cm, Weight: 70kg
        # Expected BMI: 70 / (1.7)^2 = 24.22
        bmi = BMICalculator.calculate(170, 70)
        assert pytest.approx(bmi, 0.01) == 24.22

    def test_underweight_bmi_calculation(self):
        """Test BMI calculation resulting in underweight category."""
        # Height: 180cm, Weight: 55kg
        # Expected BMI: 55 / (1.8)^2 = 16.98
        bmi = BMICalculator.calculate(180, 55)
        assert pytest.approx(bmi, 0.01) == 16.98

    def test_overweight_bmi_calculation(self):
        """Test BMI calculation resulting in overweight category."""
        # Height: 165cm, Weight: 75kg
        # Expected BMI: 75 / (1.65)^2 = 27.55
        bmi = BMICalculator.calculate(165, 75)
        assert pytest.approx(bmi, 0.01) == 27.55

    def test_obese_bmi_calculation(self):
        """Test BMI calculation resulting in obese category."""
        # Height: 160cm, Weight: 85kg
        # Expected BMI: 85 / (1.6)^2 = 33.20
        bmi = BMICalculator.calculate(160, 85)
        assert pytest.approx(bmi, 0.01) == 33.20

    def test_zero_height_raises_error(self):
        """Test that zero height raises ValueError."""
        with pytest.raises(ValueError, match="Height and weight must be positive values"):
            BMICalculator.calculate(0, 70)

    def test_negative_height_raises_error(self):
        """Test that negative height raises ValueError."""
        with pytest.raises(ValueError, match="Height and weight must be positive values"):
            BMICalculator.calculate(-170, 70)

    def test_zero_weight_raises_error(self):
        """Test that zero weight raises ValueError."""
        with pytest.raises(ValueError, match="Height and weight must be positive values"):
            BMICalculator.calculate(170, 0)

    def test_negative_weight_raises_error(self):
        """Test that negative weight raises ValueError."""
        with pytest.raises(ValueError, match="Height and weight must be positive values"):
            BMICalculator.calculate(170, -70)

    def test_unrealistic_height_raises_error(self):
        """Test that unrealistic height values raise ValueError."""
        with pytest.raises(ValueError, match="Height or weight values are unrealistic"):
            BMICalculator.calculate(350, 70)

    def test_unrealistic_weight_raises_error(self):
        """Test that unrealistic weight values raise ValueError."""
        with pytest.raises(ValueError, match="Height or weight values are unrealistic"):
            BMICalculator.calculate(170, 600)

    def test_minimum_valid_values(self):
        """Test BMI calculation with minimum valid values."""
        bmi = BMICalculator.calculate(config.HEIGHT_MIN_CM, config.WEIGHT_MIN_KG)
        assert bmi == 10.0

    def test_maximum_valid_values(self):
        """Test BMI calculation with maximum valid values."""
        bmi = BMICalculator.calculate(config.HEIGHT_MAX_CM, config.WEIGHT_MAX_KG)
        assert pytest.approx(bmi, 0.01) == 55.56


class TestGetBMICategory:
    """Test cases for BMICalculator.get_category method."""

    def test_underweight_category(self):
        """Test underweight category (BMI < 18.5)."""
        category, color, emoji = BMICalculator.get_category(17.0)
        assert category == config.CATEGORY_UNDERWEIGHT
        assert color == config.COLOR_UNDERWEIGHT
        assert emoji == config.EMOJI_UNDERWEIGHT

    def test_underweight_boundary(self):
        """Test underweight boundary (BMI = 18.4)."""
        category, color, emoji = BMICalculator.get_category(18.4)
        assert category == config.CATEGORY_UNDERWEIGHT

    def test_normal_weight_category(self):
        """Test normal weight category (18.5 <= BMI < 24.9)."""
        category, color, emoji = BMICalculator.get_category(22.0)
        assert category == config.CATEGORY_NORMAL
        assert color == config.COLOR_NORMAL
        assert emoji == config.EMOJI_NORMAL

    def test_normal_weight_lower_boundary(self):
        """Test normal weight lower boundary (BMI = 18.5)."""
        category, color, emoji = BMICalculator.get_category(18.5)
        assert category == config.CATEGORY_NORMAL

    def test_normal_weight_upper_boundary(self):
        """Test normal weight upper boundary (BMI = 24.8)."""
        category, color, emoji = BMICalculator.get_category(24.8)
        assert category == config.CATEGORY_NORMAL

    def test_overweight_category(self):
        """Test overweight category (25 <= BMI < 29.9)."""
        category, color, emoji = BMICalculator.get_category(27.0)
        assert category == config.CATEGORY_OVERWEIGHT
        assert color == config.COLOR_OVERWEIGHT
        assert emoji == config.EMOJI_OVERWEIGHT

    def test_overweight_lower_boundary(self):
        """Test overweight lower boundary (BMI = 25.0)."""
        category, color, emoji = BMICalculator.get_category(25.0)
        assert category == config.CATEGORY_OVERWEIGHT

    def test_overweight_upper_boundary(self):
        """Test overweight upper boundary (BMI = 29.8)."""
        category, color, emoji = BMICalculator.get_category(29.8)
        assert category == config.CATEGORY_OVERWEIGHT

    def test_obese_category(self):
        """Test obese category (BMI >= 30)."""
        category, color, emoji = BMICalculator.get_category(35.0)
        assert category == config.CATEGORY_OBESE
        assert color == config.COLOR_OBESE
        assert emoji == config.EMOJI_OBESE

    def test_obese_boundary(self):
        """Test obese boundary (BMI = 30.0)."""
        category, color, emoji = BMICalculator.get_category(30.0)
        assert category == config.CATEGORY_OBESE

    def test_very_high_bmi(self):
        """Test very high BMI value."""
        category, color, emoji = BMICalculator.get_category(50.0)
        assert category == config.CATEGORY_OBESE

    def test_negative_bmi_raises_error(self):
        """Test that negative BMI raises ValueError."""
        with pytest.raises(ValueError, match="BMI cannot be negative"):
            BMICalculator.get_category(-5.0)


class TestInputValidator:
    """Test cases for InputValidator class."""

    def test_valid_height(self):
        """Test validation of valid height."""
        is_valid, error_msg = InputValidator.validate_height(170)
        assert is_valid is True
        assert error_msg == ""

    def test_height_too_low(self):
        """Test validation of height below minimum."""
        is_valid, error_msg = InputValidator.validate_height(50)
        assert is_valid is False
        assert "too low" in error_msg.lower()

    def test_height_too_high(self):
        """Test validation of height above maximum."""
        is_valid, error_msg = InputValidator.validate_height(350)
        assert is_valid is False
        assert "exceeds" in error_msg.lower()

    def test_negative_height(self):
        """Test validation of negative height."""
        is_valid, error_msg = InputValidator.validate_height(-10)
        assert is_valid is False
        assert "positive" in error_msg.lower()

    def test_valid_weight(self):
        """Test validation of valid weight."""
        is_valid, error_msg = InputValidator.validate_weight(70)
        assert is_valid is True
        assert error_msg == ""

    def test_weight_too_low(self):
        """Test validation of weight below minimum."""
        is_valid, error_msg = InputValidator.validate_weight(5)
        assert is_valid is False
        assert "too low" in error_msg.lower()

    def test_weight_too_high(self):
        """Test validation of weight above maximum."""
        is_valid, error_msg = InputValidator.validate_weight(600)
        assert is_valid is False
        assert "exceeds" in error_msg.lower()

    def test_negative_weight(self):
        """Test validation of negative weight."""
        is_valid, error_msg = InputValidator.validate_weight(-10)
        assert is_valid is False
        assert "positive" in error_msg.lower()

    def test_validate_both_inputs_valid(self):
        """Test validation of both valid inputs."""
        is_valid, error_msg = InputValidator.validate_inputs(170, 70)
        assert is_valid is True
        assert error_msg == ""

    def test_validate_both_inputs_invalid_height(self):
        """Test validation with invalid height."""
        is_valid, error_msg = InputValidator.validate_inputs(50, 70)
        assert is_valid is False
        assert "height" in error_msg.lower()

    def test_validate_both_inputs_invalid_weight(self):
        """Test validation with invalid weight."""
        is_valid, error_msg = InputValidator.validate_inputs(170, 5)
        assert is_valid is False
        assert "weight" in error_msg.lower()


class TestIntegration:
    """Integration tests combining multiple components."""

    def test_full_underweight_flow(self):
        """Test full flow for underweight person."""
        # Validate inputs
        is_valid, _ = InputValidator.validate_inputs(180, 55)
        assert is_valid is True

        # Calculate BMI
        bmi = BMICalculator.calculate(180, 55)
        assert pytest.approx(bmi, 0.01) == 16.98

        # Get category
        category, color, emoji = BMICalculator.get_category(bmi)
        assert category == config.CATEGORY_UNDERWEIGHT

    def test_full_normal_weight_flow(self):
        """Test full flow for normal weight person."""
        is_valid, _ = InputValidator.validate_inputs(170, 70)
        assert is_valid is True

        bmi = BMICalculator.calculate(170, 70)
        assert pytest.approx(bmi, 0.01) == 24.22

        category, color, emoji = BMICalculator.get_category(bmi)
        assert category == config.CATEGORY_NORMAL

    def test_full_overweight_flow(self):
        """Test full flow for overweight person."""
        is_valid, _ = InputValidator.validate_inputs(165, 75)
        assert is_valid is True

        bmi = BMICalculator.calculate(165, 75)
        assert pytest.approx(bmi, 0.01) == 27.55

        category, color, emoji = BMICalculator.get_category(bmi)
        assert category == config.CATEGORY_OVERWEIGHT

    def test_full_obese_flow(self):
        """Test full flow for obese person."""
        is_valid, _ = InputValidator.validate_inputs(160, 85)
        assert is_valid is True

        bmi = BMICalculator.calculate(160, 85)
        assert pytest.approx(bmi, 0.01) == 33.20

        category, color, emoji = BMICalculator.get_category(bmi)
        assert category == config.CATEGORY_OBESE


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_bmi_boundary_18_5(self):
        """Test exact BMI boundary at 18.5."""
        # Find weight for 170cm to get exactly 18.5 BMI
        # BMI = weight / (1.7)^2
        # 18.5 = weight / 2.89
        # weight = 53.465
        bmi = BMICalculator.calculate(170, 53.465)
        assert pytest.approx(bmi, 0.01) == 18.5
        category, _, _ = BMICalculator.get_category(18.5)
        assert category == config.CATEGORY_NORMAL

    def test_bmi_boundary_24_9(self):
        """Test exact BMI boundary at 24.9."""
        bmi = BMICalculator.calculate(170, 71.961)
        assert pytest.approx(bmi, 0.01) == 24.9
        category, _, _ = BMICalculator.get_category(24.9)
        assert category == config.CATEGORY_NORMAL

    def test_bmi_boundary_29_9(self):
        """Test exact BMI boundary at 29.9."""
        bmi = BMICalculator.calculate(170, 86.411)
        assert pytest.approx(bmi, 0.01) == 29.9
        category, _, _ = BMICalculator.get_category(29.9)
        assert category == config.CATEGORY_OVERWEIGHT

    def test_decimal_inputs(self):
        """Test BMI calculation with decimal inputs."""
        bmi = BMICalculator.calculate(175.5, 72.3)
        assert pytest.approx(bmi, 0.01) == 23.47

    def test_bmi_validator_valid_range(self):
        """Test BMI validator with valid BMI."""
        assert BMICalculator.validate_bmi(25.0) is True
        assert BMICalculator.validate_bmi(0.1) is True
        assert BMICalculator.validate_bmi(99.9) is True

    def test_bmi_validator_invalid_range(self):
        """Test BMI validator with invalid BMI."""
        assert BMICalculator.validate_bmi(-0.1) is False
        assert BMICalculator.validate_bmi(101) is False
