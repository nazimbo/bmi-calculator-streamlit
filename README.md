# BMI Calculator

A simple web application built with Streamlit that calculates Body Mass Index (BMI) and provides weight category classification.

## Features

- Calculate BMI using height and weight inputs
- Input validation with minimum and maximum values
- Real-time BMI calculation
- Automatic weight category classification
- Clean and intuitive user interface

## Requirements

- Python 3.7+
- Streamlit

## Installation

1. Create a virtual environment:
```bash
python3 -m venv bmi_env
source bmi_env/bin/activate  # On Windows, use: bmi_env\Scripts\activate
```

2. Install the required package:
```bash
pip install streamlit
```

## Usage

1. Save the code in a file named `app.py`

2. Run the Streamlit application:
```bash
streamlit run app.py
```

3. The application will open in your default web browser. If it doesn't, navigate to the URL shown in the terminal (typically http://localhost:8501)

4. Enter your height in centimeters (100-250 cm)

5. Enter your weight in kilograms (10-150 kg)

6. Your BMI and weight category will be displayed automatically

## BMI Categories

The application classifies weight into the following categories:
- Underweight: BMI < 18.5
- Normal weight: BMI 18.5-24.9
- Overweight: BMI 25-29.9
- Obese: BMI ≥ 30

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).