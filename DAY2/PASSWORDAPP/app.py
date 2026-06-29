
import streamlit as st
import random
st.title("Password Analyser")
password=st.text_input("Enter your password", type="password")
#st.button("Validate")
if st.button("Validate"):
    upper=lower=digit=special=False
    for ch in password:
        if ch.isupper():
            upper=True
        elif ch.islower():
            lower=True
        elif ch.isdigit():
            digit=True
        else:
            special=True
        
    if len(password)>8 and upper and lower and digit and special:
        st.success("Strong Password . . Thank you! ")
    else:
        st.error("Invalid Password")
        if len(password)<8:
            st.write("Password should be at least 8 characters long")
        if not upper:
            st.write("Password should contain at least one uppercase letter")
        if not lower:
            st.write("Password should contain at least one lowercase letter")
        if not digit:
            st.write("Password should contain at least one digit")
        if not special:
            st.write("Password should contain at least one special character")