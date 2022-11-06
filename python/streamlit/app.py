import streamlit as st
import random

st.set_page_config(page_title="Password App", page_icon="🔒")
st.markdown("<h1 style='text-align: center; margin-bottom: 40px; color: #F0FF42;'>Generate Secure Password</h1>", unsafe_allow_html=True)
pw_length = st.slider(min_value=10, max_value=100, label="Password Length")
pw_keys = "abcdefghijklmnABCoZ!@#$%^xyz012345678MpqrsDLEF0AZ!@#$%^BCODtKuvJwI}{G[]Hxyz01234567890AZ!@#$%^BCODEFGHNIJKLMNOPQRSTUVWXYZ!@#$%^%^&*()?"
pw = ""
for x in range(0, pw_length):
    pw_char = random.choice(pw_keys)
    pw = pw + pw_char
#using st.code allows user to copy password by clicking on clipboard icon    
st.code(f" {pw} ")
st.markdown("<br><hr>", unsafe_allow_html=True)
#workaround to center generate button
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3:
    center_button = st.button("Generate")