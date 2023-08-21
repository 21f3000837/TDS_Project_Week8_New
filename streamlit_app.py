import streamlit as st

def main():
    st.title("Find the Largest Number")

    st.write("Enter three numbers to find the largest among them:")

    number1 = st.number_input("Enter the first number:")
    number2 = st.number_input("Enter the second number:")
    number3 = st.number_input("Enter the third number:")

    largest_number = max(number1, number2, number3)

    st.write(f"The largest number is: {largest_number}")

main()

