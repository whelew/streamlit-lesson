# Create a function named calculator_body()
# Within it, create 3 columns using the st.columns() function
# Note, in the video, this column function was still in beta
    
import streamlit as st

def calculator_body():
    st.write("---") #Puts a straight line to divide app
    col1, col2, col3 = st.columns(3)
    with col1:
        num1 = st.number_input(label = 'Enter the first integer', step = 1)
    with col2:
        num2 = st.number_input(label = 'Enter the second integer', step = 2)
    with col3:
        operator = st.selectbox(label = 'Select operator',
                           options = ['Add', 'Subtract', 'Multiply', 'Divide'])
        if st.button('Click here to calculate!'):
            if num2 == 0 and operator == 'Divide':
                st.error('Division by zero error. Enter a non-zero integer.')
            else:
                calculator_function(num1, num2, operator)

def calculator_function(num1, num2, operator):
    if operator == 'Add': result = num1 + num2
    elif operator == 'Subtract': result = num1 - num2
    elif operator == 'Multiply': result = num1 * num2
    elif operator == 'Divide': result = num1 / num2
    st.success(f'The result is **{result}**')
    


