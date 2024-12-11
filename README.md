# BMI Calculator

A modern, interactive web application built with Streamlit that calculates Body Mass Index (BMI) and provides personalized health insights.

## Features

- Interactive BMI gauge visualization
- Real-time BMI calculation
- Color-coded weight categories
- Personalized health tips
- Information about BMI
- Responsive design
- Input validation
- Professional UI/UX

## Requirements

- Python 3.7+
- Streamlit
- Plotly
- Pandas

## Installation

1. Create a virtual environment:
```bash
python3 -m venv bmi_env
source bmi_env/bin/activate  # On Windows, use: bmi_env\Scripts\activate
```

2. Install the required packages:
```bash
pip install streamlit plotly pandas
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

6. View your BMI on the interactive gauge chart

7. Check your weight category and personalized health tips

## Features Breakdown

### Visual Elements
- Interactive gauge chart showing BMI
- Color-coded weight categories
- Professional styling with custom CSS
- Responsive two-column layout
- Expandable information sections

### Functionality
- Real-time BMI calculation
- Input validation
- Personalized health tips based on BMI category
- Detailed BMI information
- Mobile-responsive design

### BMI Categories

The application classifies weight into the following categories:
- Underweight: BMI < 18.5 (Yellow)
- Normal weight: BMI 18.5-24.9 (Green)
- Overweight: BMI 25-29.9 (Orange)
- Obese: BMI ≥ 30 (Red)

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Screenshots

(Add screenshots of your application here to showcase the interface and features)