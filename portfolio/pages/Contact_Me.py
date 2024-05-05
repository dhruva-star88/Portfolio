import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    email = st.text_input("Your Email Address")
    raw_message = st.text_area("Your Message")
    # This is the synatx for email to write with subject
    message = f"""\
Subject: New Email from {email}\

{raw_message}
From: {email}
"""
    button = st.form_submit_button("Submit")
    print(button)

    if button:
        print(button)
        print("Pressed")
        send_email(message)
        st.info("Your email has been sent Successfully")
