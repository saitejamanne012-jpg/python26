import streamlit as st
st.title("welcome to streamlit")
num1=st.number_input("Enter number 1",step=1)
num2=st.number_input("Enter number 2",step=2) 

sum=num1+num2
if st.button("addition"):          
  st.write("sum is:",sum)