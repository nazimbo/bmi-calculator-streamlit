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
├── app.py                    # Main application with BMI logic
├── requirements.txt          # Direct dependencies
├── requirements-lock.txt     # Pinned dependency versions
├── requirements-dev.txt      # Development dependencies
├── pytest.ini               # Pytest configuration
├── .gitignore               # Comprehensive gitignore patterns
├── README.md                # This file
├── TESTING.md               # Testing documentation
├── SECURITY.md              # Security documentation
└── tests/                   # Test suite
    ├── __init__.py
    └── test_bmi_calculator.py  # Comprehensive unit tests
```

## Code Quality

### Testing
- **Unit tests**: 50+ test cases
- **Coverage**: 80%+ code coverage requirement
- **Test categories**: Normal cases, boundary tests, edge cases, error handling, integration tests
- **Continuous testing**: Run tests before every commit

### Type Safety
```python
def calculate_bmi(height_cm: float, weight_kg: float) -> float:
    """Calculate BMI from height and weight."""
    # Full type hints on all functions
```

### Error Handling
```python
try:
    bmi = calculate_bmi(height, weight)
except ValueError as e:
    st.error(f"❌ {str(e)}")
    logger.error(f"ValueError: {e}")
```

### Logging
- All calculations logged
- Error tracking with full context
- Rotating log files (10MB max, 5 backups)
- Logs excluded from version control

### BMI Categories

The application classifies weight into the following categories:
- Underweight: BMI < 18.5 (Yellow)
- Normal weight: BMI 18.5-24.9 (Green)
- Overweight: BMI 25-29.9 (Orange)
- Obese: BMI ≥ 30 (Red)

## Recent Improvements (v1.1.0)

### Critical Security Fixes
- ✅ **Fixed XSS vulnerability**: Replaced all `unsafe_allow_html=True` with Streamlit native components
- ✅ **Added error handling**: Comprehensive try-except blocks throughout application
- ✅ **Input validation**: Validates height/weight for realistic ranges
- ✅ **Dependency security**: Separated direct dependencies from lock file

### Quality Improvements
- ✅ **Testing infrastructure**: 50+ tests with 80%+ coverage requirement
- ✅ **Type hints**: Added type annotations to all functions
- ✅ **Logging**: Full audit trail with rotating log files
- ✅ **Documentation**: Added TESTING.md and SECURITY.md
- ✅ **Comprehensive .gitignore**: Prevents committing sensitive files

### Code Organization
- ✅ **Extracted functions**: `calculate_bmi()` and `get_bmi_category()` for testability
- ✅ **Better separation**: Requirements split into production and development
- ✅ **Developer tools**: pytest, coverage, safety, bandit ready

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