"""CSS styles for BMI Calculator application."""


def get_custom_css() -> str:
    """Get custom CSS for styling the application.

    Returns:
        String containing CSS styles

    Example:
        >>> css = get_custom_css()
        >>> st.markdown(css, unsafe_allow_html=True)
    """
    return """
        <style>
        .main {
            padding: 2rem;
        }
        .stAlert {
            padding: 1rem;
            margin: 1rem 0;
            border-radius: 0.5rem;
        }
        div[data-testid="stExpander"] {
            border: none;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            padding: 1rem;
            border-radius: 0.5rem;
        }
        </style>
    """
