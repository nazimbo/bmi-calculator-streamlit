# BMI Calculator

A modern, secure, and well-tested web application built with Streamlit that calculates Body Mass Index (BMI) and provides personalized health insights.

## Features

### Core Functionality
- Interactive BMI gauge visualization
- Real-time BMI calculation with error handling
- Color-coded weight categories with visual indicators
- Personalized health tips based on BMI category
- Comprehensive input validation
- Professional UI/UX with native Streamlit components

### Security & Quality
- ✅ **XSS Protection**: No unsafe HTML rendering
- ✅ **Error Handling**: Comprehensive try-except blocks with logging
- ✅ **Input Validation**: Validates all user inputs for realistic ranges
- ✅ **Logging**: Full audit trail with rotating log files
- ✅ **Type Safety**: Type hints on all functions
- ✅ **Testing**: 80%+ code coverage with pytest
- ✅ **Security Scanning**: Safety and Bandit ready

## Requirements

- Python 3.9+
- Streamlit >= 1.41.0
- Plotly >= 5.24.0
- Pandas >= 2.2.0

## Installation

### For Users

1. Clone the repository:
```bash
git clone <repository-url>
cd bmi-calculator-streamlit
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install production dependencies:
```bash
pip install -r requirements.txt
```

### For Developers

Install development dependencies (includes testing and linting tools):
```bash
pip install -r requirements-dev.txt
```

## Usage

### Running the Application

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Open your browser to `http://localhost:8501`

3. Enter your measurements:
   - Height: 100-300 cm
   - Weight: 10-500 kg

4. View your results:
   - Interactive BMI gauge
   - Weight category with visual indicator
   - Personalized health tips

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=. --cov-report=html

# View coverage report
open htmlcov/index.html
```

See [TESTING.md](TESTING.md) for detailed testing documentation.

### Security Checks

```bash
# Check for dependency vulnerabilities
safety check --file requirements-lock.txt

# Static security analysis
bandit -r app.py
```

See [SECURITY.md](SECURITY.md) for security documentation.

## Project Structure

```
bmi-calculator-streamlit/
├── app.py                       # Main application entry point
├── config/                      # Configuration module
│   ├── __init__.py
│   └── constants.py            # All configuration constants
├── core/                        # Core business logic
│   ├── __init__.py
│   ├── calculations.py         # BMI calculation logic
│   └── validators.py           # Input validation logic
├── ui/                          # UI components
│   ├── __init__.py
│   ├── components.py           # Reusable UI components
│   └── styles.py               # CSS styles
├── tests/                       # Test suite
│   ├── __init__.py
│   └── test_bmi_calculator.py  # Comprehensive unit tests
├── requirements.txt             # Direct dependencies
├── requirements-lock.txt        # Pinned dependency versions
├── requirements-dev.txt         # Development dependencies
├── pyproject.toml              # Project configuration (pytest, ruff, black, mypy)
├── .pre-commit-config.yaml     # Pre-commit hooks configuration
├── .gitignore                  # Comprehensive gitignore patterns
├── README.md                   # This file
├── TESTING.md                  # Testing documentation
└── SECURITY.md                 # Security documentation
```

## Code Quality

### Modular Architecture
The application follows clean architecture principles with clear separation of concerns:

- **config/**: Configuration and constants (no hardcoded values)
- **core/**: Business logic (calculations, validators)
- **ui/**: Presentation layer (components, styles)
- **tests/**: Comprehensive test suite

This modular structure provides:
- ✅ Better testability and maintainability
- ✅ Clear separation of concerns
- ✅ Easy to extend and modify
- ✅ Reusable components

### Testing
- **Unit tests**: 70+ test cases covering all modules
- **Coverage**: 80%+ code coverage requirement (enforced)
- **Test categories**: Normal cases, boundary tests, edge cases, error handling, integration tests
- **Continuous testing**: Pre-commit hooks run tests automatically

```bash
# Run tests with coverage
pytest --cov=. --cov-report=html
```

### Code Quality Tools
```bash
# Format code with Black
black .

# Lint with Ruff
ruff check . --fix

# Type check with mypy
mypy app.py core/ ui/ config/

# Security check
bandit -r app.py core/ ui/ config/
safety check --file requirements-lock.txt
```

### Pre-commit Hooks
Automated checks run before every commit:
- Code formatting (Black)
- Linting (Ruff)
- Type checking (mypy)
- Security scanning (Bandit, Safety)
- Tests (pytest)

```bash
# Install pre-commit hooks
pre-commit install

# Run manually
pre-commit run --all-files
```

### Type Safety
All functions have complete type annotations:
```python
def calculate_bmi(height_cm: float, weight_kg: float) -> float:
    """Calculate BMI from height and weight."""
    # Full type hints enforced by mypy
```

### Error Handling
Comprehensive error handling with logging:
```python
try:
    bmi = BMICalculator.calculate(height, weight)
    logger.info(f"BMI calculated: {bmi:.2f}")
except ValueError as e:
    st.error(f"❌ {str(e)}")
    logger.error(f"ValueError: {e}")
```

### Configuration Management
All constants centralized in config module:
```python
from config.constants import config

# No hardcoded values
height_min = config.HEIGHT_MIN_CM
bmi_threshold = config.BMI_UNDERWEIGHT_THRESHOLD
```

### Logging
- All calculations logged with context
- Error tracking with full stack traces
- Rotating log files (10MB max, 5 backups)
- Logs excluded from version control

### BMI Categories

The application classifies weight into the following categories:
- Underweight: BMI < 18.5 (Yellow)
- Normal weight: BMI 18.5-24.9 (Green)
- Overweight: BMI 25-29.9 (Orange)
- Obese: BMI ≥ 30 (Red)

## Recent Improvements (v1.2.0)

### Critical Security Fixes (v1.1.0)
- ✅ **Fixed XSS vulnerability**: Replaced all `unsafe_allow_html=True` with Streamlit native components
- ✅ **Added error handling**: Comprehensive try-except blocks throughout application
- ✅ **Input validation**: Validates height/weight for realistic ranges
- ✅ **Dependency security**: Separated direct dependencies from lock file

### High Severity Fixes (v1.2.0)
- ✅ **Modular architecture**: Refactored monolithic app.py into config/, core/, ui/ modules
- ✅ **Configuration management**: Eliminated all hardcoded values with centralized config
- ✅ **Code quality tools**: Added ruff, black, mypy with pyproject.toml configuration
- ✅ **Pre-commit hooks**: Automated code quality checks before every commit
- ✅ **Enhanced validation**: Separate InputValidator class with comprehensive checks

### Quality Improvements
- ✅ **Testing infrastructure**: 70+ tests with 80%+ coverage requirement (enforced)
- ✅ **Type hints**: Complete type annotations enforced by mypy
- ✅ **Logging**: Full audit trail with rotating log files
- ✅ **Documentation**: Added TESTING.md and SECURITY.md
- ✅ **Comprehensive .gitignore**: Prevents committing sensitive files

### Code Organization
- ✅ **Separation of concerns**: config/, core/, ui/ modules with clear responsibilities
- ✅ **Reusable components**: UIComponents class for all UI rendering
- ✅ **Business logic isolation**: BMICalculator class for all calculations
- ✅ **Configuration centralization**: All constants in one place
- ✅ **Developer tools**: Complete toolchain (pytest, ruff, black, mypy, bandit, safety, pre-commit)

## Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Write** tests for your changes
4. **Run** the test suite: `pytest --cov=.`
5. **Ensure** coverage stays above 80%
6. **Run** security checks: `safety check` and `bandit -r app.py`
7. **Commit** your changes with clear messages
8. **Push** to your branch
9. **Open** a Pull Request

See [TESTING.md](TESTING.md) for testing guidelines and [SECURITY.md](SECURITY.md) for security best practices.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Screenshots

(Add screenshots of your application here to showcase the interface and features)