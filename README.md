# BMI Calculator v2.0

A modern, secure, accessible, and multilingual web application built with Streamlit that calculates Body Mass Index (BMI) and provides personalized health insights.

## ✨ What's New in v2.0

### 🚀 **Performance Optimizations**
- **Caching**: Intelligent caching with `@st.cache_data` and `@st.cache_resource`
- **Faster Load Times**: CSS, translations, and gauge charts are cached
- **Reduced Server Load**: Optimized for high-traffic scenarios

### 🌍 **Internationalization (i18n)**
- **Multi-language Support**: English, Spanish, French
- **Easy Language Switching**: Sidebar language selector
- **Extensible**: JSON-based translations for easy additions

### ♿ **Accessibility (WCAG 2.1 Level AA)**
- **Screen Reader Support**: ARIA labels and semantic HTML
- **Keyboard Navigation**: Full keyboard accessibility
- **Focus Indicators**: Clear visual focus states
- **Alternative Text**: Screen reader descriptions for visualizations

### 🐳 **Production-Ready Deployment**
- **Docker Support**: Multi-stage Dockerfile for optimal image size
- **Docker Compose**: One-command deployment
- **Comprehensive Docs**: Deployment guides for AWS, GCP, Azure, and Streamlit Cloud
- **Health Checks**: Built-in health monitoring
- **Security**: Non-root user, minimal attack surface

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
- ✅ **Logging**: Full audit trail with rotating log files (singleton pattern)
- ✅ **Type Safety**: Type hints on all functions
- ✅ **Testing**: 90%+ code coverage with pytest (52 tests)
- ✅ **Security Scanning**: Safety and Bandit integrated in CI/CD
- ✅ **Modular Architecture**: Separation of concerns (core, UI, utils)

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

### Running with Docker

**Quick Start:**

```bash
# Using Docker
docker build -t bmi-calculator .
docker run -p 8501:8501 bmi-calculator

# Using Docker Compose (recommended)
docker-compose up -d
```

Open `http://localhost:8501` in your browser.

**Stop the application:**

```bash
docker-compose down
```

See [DEPLOYMENT.md](DEPLOYMENT.md) for comprehensive deployment guides including AWS, GCP, Azure, and Streamlit Cloud.

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
├── app.py                       # Main Streamlit application (UI layer)
├── src/                         # Application source code
│   └── bmi_calculator/
│       ├── core/                # Business logic
│       │   ├── calculator.py    # BMI calculations
│       │   └── constants.py     # Configuration & constants
│       ├── ui/                  # UI components
│       │   └── components.py    # Reusable UI components (gauge)
│       └── utils/               # Utilities
│           └── logger.py        # Logging configuration
├── i18n/                        # Internationalization
│   ├── en.json                  # English translations
│   ├── es.json                  # Spanish translations
│   └── fr.json                  # French translations
├── tests/                       # Test suite
│   └── test_bmi_calculator.py   # Comprehensive unit tests (52 tests)
├── .github/                     # CI/CD
│   └── workflows/
│       └── ci.yml               # GitHub Actions pipeline
├── .streamlit/                  # Streamlit configuration
│   └── config.toml              # Production configuration
├── Dockerfile                   # Multi-stage Docker build
├── docker-compose.yml           # Docker Compose configuration
├── .dockerignore                # Docker build exclusions
├── requirements.txt             # Direct dependencies
├── requirements-lock.txt        # Pinned dependency versions
├── requirements-dev.txt         # Development dependencies
├── pytest.ini                   # Pytest configuration
├── README.md                    # This file
├── TESTING.md                   # Testing documentation
├── SECURITY.md                  # Security documentation
└── DEPLOYMENT.md                # Comprehensive deployment guide
```

## Code Quality

### Testing
- **Unit tests**: 52 comprehensive test cases
- **Coverage**: 90% code coverage (exceeds 80% target)
- **Test categories**: Normal cases, boundary tests, edge cases, error handling, integration tests
- **Continuous testing**: Automated via GitHub Actions CI/CD
- **Test modules**: Core logic, UI components, accessibility features

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

## Version History

### v2.0.0 (Latest) - Comprehensive Enhancements

#### 🚀 **Performance & Scalability**
- ✅ **Intelligent Caching**: `@st.cache_data` and `@st.cache_resource` for optimal performance
- ✅ **Singleton Logger**: Fixed memory leaks from handler accumulation
- ✅ **Optimized Reruns**: Reduced server resource usage for high-traffic scenarios

#### 🌍 **Internationalization**
- ✅ **Multi-language Support**: English, Spanish, French
- ✅ **JSON-based Translations**: Easy to extend with new languages
- ✅ **User Preference**: Language selector in sidebar

#### ♿ **Accessibility (WCAG 2.1 Level AA)**
- ✅ **Screen Reader Support**: Full ARIA labels and semantic HTML
- ✅ **Keyboard Navigation**: Complete keyboard accessibility
- ✅ **Focus Management**: Clear visual focus indicators
- ✅ **Alternative Text**: Screen reader descriptions for all visualizations

#### 🐳 **Production Deployment**
- ✅ **Docker Support**: Multi-stage Dockerfile with non-root user
- ✅ **Docker Compose**: One-command deployment
- ✅ **Health Checks**: Built-in health monitoring
- ✅ **Deployment Guides**: Comprehensive docs for AWS, GCP, Azure, Streamlit Cloud

#### 🏗️ **Architecture**
- ✅ **Modular Structure**: Separation of core, UI, and utils
- ✅ **Constants Module**: All configuration centralized
- ✅ **Backward Compatibility**: Legacy API maintained

#### 📊 **Testing & CI/CD**
- ✅ **52 Comprehensive Tests**: 90% code coverage
- ✅ **GitHub Actions**: Automated testing, security scanning, linting
- ✅ **Multi-Python Support**: Tested on Python 3.9-3.12

### v1.1.0 - Security & Quality Hardening

#### Critical Fixes
- ✅ Fixed XSS vulnerability with native Streamlit components
- ✅ Added comprehensive error handling
- ✅ Implemented realistic input validation
- ✅ Separated dependency management (direct vs lock files)

#### Quality Improvements
- ✅ 50+ tests with 80%+ coverage
- ✅ Type hints on all functions
- ✅ Rotating log files with audit trail
- ✅ Added TESTING.md and SECURITY.md

#### Code Organization
- ✅ Extracted testable functions
- ✅ Split production and development dependencies

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