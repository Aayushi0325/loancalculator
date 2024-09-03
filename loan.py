# loan_calculator.py
import streamlit as st

# Set the title of the app
st.title("Loan Calculator")

# Input fields for loan amount, loan period, interest rate, and compounding frequency
loan_amount = st.number_input("Enter the loan amount (₹):", min_value=0.0, value=10000.0, step=1000.0)
loan_years = st.number_input("Enter the number of years:", min_value=1, value=5, step=1)
interest_rate = st.number_input("Enter the annual interest rate (%):", min_value=0.0, value=5.0, step=0.1)
compounding_frequency = st.selectbox("Select compounding frequency:", ["Annually", "Semi-Annually", "Quarterly", "Monthly", "Daily"])

# Mapping frequency to n (number of times interest is compounded per year)
frequency_mapping = {
    "Annually": 1,
    "Semi-Annually": 2,
    "Quarterly": 4,
    "Monthly": 12,
    "Daily": 365
}

# Get the number of times interest is compounded per year based on user's selection
n = frequency_mapping[compounding_frequency]

# Calculate the total amount to be repaid using the compound interest formula
if st.button("Calculate"):
    # Convert annual interest rate to decimal
    rate = interest_rate / 100

    # Calculate the total amount using the compound interest formula
    total_amount = loan_amount * (1 + rate / n) ** (n * loan_years)

    # Display the result
    st.write(f"The total amount to be repaid is: ₹{total_amount:.2f}")
