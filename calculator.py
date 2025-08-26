# calculator.py
import streamlit as st
import math

# Memory variable
memory = 0

st.title("Advanced Calculator")

# User inputs
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)
operation = st.selectbox("Choose Operation", 
                         ["Addition", "Subtraction", "Multiplication", "Division", 
                          "Power", "Square Root", "Percentage", "Memory Recall", "Clear Memory"])

# Button to calculate
if st.button("Calculate"):
    result = None
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero!"
    elif operation == "Power":
        result = num1 ** num2
    elif operation == "Square Root":
        result = math.sqrt(num1)
    elif operation == "Percentage":
        result = (num1 * num2) / 100
    elif operation == "Memory Recall":
        result = memory
    elif operation == "Clear Memory":
        memory = 0
        result = "Memory Cleared!"

    # Store result in memory if not Memory Recall/Clear Memory
    if operation not in ["Memory Recall", "Clear Memory"]:
        memory = result

    st.write("Result:", result)
