# loan_calculator.py
import streamlit as st

# Set the title of the app
st.title("Loan Calculator")

# Input fields for loan amount and loan period
loan_amount = st.number_input("Enter the loan amount:", min_value=0.0, value=10000.0, step=1000.0)
loan_years = st.number_input("Enter the number of years:", min_value=1, value=5, step=1)
interest_rate = st.number_input("Enter the annual interest rate (%):", min_value=0.0, value=5.0, step=0.1)

n=1
# Calculate the total amount to be repaid
if st.button("Calculate"):
    # Convert annual interest rate to decimal
    rate = interest_rate / 100

    # Calculate the total amount to be repaid
    total_amount = loan_amount * (1 + rate / n) ** (n * loan_years)

    # Display the result
    st.write(f"The total amount to be repaid is: ₹{total_amount:.2f}")

