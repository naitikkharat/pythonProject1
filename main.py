import streamlit as st

st.title("Login Page")


allowed_accounts = {
    "fs23ai024": "12345",
    "fs23ai13": "6789",
    "fs23ai005": "01234"
}

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):

    if username in allowed_accounts and password == allowed_accounts[username]:
        st.success("Login successful!")
        st.snow()
    else:
        st.error("Invalid username or password")
