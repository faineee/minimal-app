import streamlit as st
from joblib import load
import numpy as np

try:
    st.write("Attempting to import joblib...")
    # Create a dummy file if it doesn't exist
    dummy_data = np.array([1])
    try:
        model = load('dummy.joblib')
        st.write("Loaded existing dummy.joblib")
    except FileNotFoundError:
        np.save('dummy.joblib', dummy_data)
        model = load('dummy.joblib')
        st.write("Created and loaded dummy.joblib")

    st.write("joblib imported successfully!")
    st.write(f"Dummy data: {model}") # Display the content to confirm loading
except Exception as e:
    st.error(f"Error importing joblib: {e}")
    st.exception(e) # Show the full traceback for debugging
