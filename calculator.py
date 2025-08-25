import streamlit as st

# Title of the App
st.title("Simple Calculator 🧮")

# Taking user input
num1 = st.number_input("Enter first number:", step=1.0)
num2 = st.number_input("Enter second number:", step=1.0)

# Operation selection
operation = st.selectbox("Choose operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

# Button to calculate
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.write(f"Result: {num1} + {num2} = {result}")

    elif operation == "Subtraction":
        result = num1 - num2
        st.write(f"Result: {num1} - {num2} = {result}")

    elif operation == "Multiplication":
        result = num1 * num2
        st.write(f"Result: {num1} × {num2} = {result}")

    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.write(f"Result: {num1} ÷ {num2} = {result}")
        else:
            st.error("Error ❌: Division by zero is not allowed!")
