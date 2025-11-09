# Testing Guide

This document describes how to run and write tests for the BMI Calculator application.

## Test Infrastructure

The project uses **pytest** as the testing framework with the following features:
- Unit tests for core calculation functions
- Integration tests for complete workflows
- Code coverage reporting
- Edge case and boundary testing

## Installation

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

This will install:
- pytest (test framework)
- pytest-cov (coverage reporting)
- pytest-mock (mocking utilities)

## Running Tests

### Run all tests
```bash
pytest
```

### Run with verbose output
```bash
pytest -v
```

### Run specific test file
```bash
pytest tests/test_bmi_calculator.py
```

### Run specific test class
```bash
pytest tests/test_bmi_calculator.py::TestCalculateBMI
```

### Run specific test
```bash
pytest tests/test_bmi_calculator.py::TestCalculateBMI::test_normal_bmi_calculation
```

### Run with coverage report
```bash
pytest --cov=. --cov-report=html
```

This generates an HTML coverage report in `htmlcov/index.html`.

### Run with coverage in terminal
```bash
pytest --cov=. --cov-report=term-missing
```

## Test Coverage Goals

- **Minimum coverage**: 80%
- **Target coverage**: 90%+
- The pytest configuration will fail if coverage drops below 80%

## Test Structure

```
tests/
├── __init__.py
├── test_bmi_calculator.py    # Unit and integration tests
└── conftest.py               # Pytest fixtures (if needed)
```

## Writing New Tests

### Test Naming Convention
- Test files: `test_*.py`
- Test classes: `Test*`
- Test functions: `test_*`

### Example Test
```python
def test_bmi_calculation():
    """Test BMI calculation with normal values."""
    bmi = calculate_bmi(170, 70)
    assert pytest.approx(bmi, 0.01) == 24.22
```

### Testing Guidelines

1. **Test one thing at a time**: Each test should verify one specific behavior
2. **Use descriptive names**: Test names should clearly describe what they test
3. **Include docstrings**: Explain what the test verifies
4. **Test edge cases**: Include boundary values and error conditions
5. **Use fixtures**: Share setup code across tests using pytest fixtures
6. **Mock external dependencies**: Don't test external services

## Current Test Coverage

### Tested Functions
- `calculate_bmi()` - BMI calculation logic
- `get_bmi_category()` - Category determination

### Test Categories
1. **Normal cases**: Standard valid inputs
2. **Boundary cases**: Values at category boundaries (18.5, 24.9, 29.9)
3. **Edge cases**: Minimum/maximum valid values
4. **Error cases**: Invalid inputs that should raise exceptions
5. **Integration**: Full workflow from input to result

## Continuous Integration

When setting up CI/CD, tests should run automatically on:
- Every push to feature branches
- Every pull request
- Before deployment to production

Example GitHub Actions workflow:
```yaml
- name: Run tests
  run: |
    pip install -r requirements-dev.txt
    pytest --cov=. --cov-report=xml
```

## Test Data

### Valid Test Cases
- Height range: 100-300 cm
- Weight range: 10-500 kg
- BMI categories: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), Obese (≥30)

### Invalid Test Cases
- Zero or negative values
- Unrealistic values (height >300cm, weight >500kg)
- Negative BMI values

## Debugging Failed Tests

### Run with detailed output
```bash
pytest -vv --tb=long
```

### Run with Python debugger
```bash
pytest --pdb
```

This drops into the debugger when a test fails.

### Show print statements
```bash
pytest -s
```

## Future Testing Enhancements

- [ ] UI testing with Selenium or Playwright
- [ ] Performance testing for large-scale usage
- [ ] Visual regression testing for UI changes
- [ ] Mutation testing to verify test quality
- [ ] Property-based testing with Hypothesis
