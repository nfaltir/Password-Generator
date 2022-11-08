import streamlit as st
import secrets
import string

st.set_page_config(page_title="Password App", page_icon="🔒", layout="wide")
st.markdown("<h1 style='text-align: center; margin-bottom: 30px; color: #FF9F29;'>Generate Secure Password</h1>", unsafe_allow_html=True)

pw_length = st.slider(min_value=10, max_value=100, label="Password Length")

symbols_char = string.punctuation
num_values = string.digits
lower_char = string.ascii_lowercase
upper_char = string.ascii_uppercase

#bind all vars
pw_keys = lower_char + upper_char + num_values + symbols_char
pw = ''.join(secrets.choice(pw_keys) for i in range(pw_length)) 

#using st.code allows user to copy password by clicking on clipboard icon    
st.code(pw)
st.markdown("<br><hr>", unsafe_allow_html=True)
#workaround to center generate button









