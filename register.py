import psycopg2
import streamlit as st
import re

conn = psycopg2.connect(host='localhost', port='5432', user='postgres', password='abcd1234')

cursor = conn.cursor()

conn.set_session(autocommit=True)


def register_user():
    name = st.text_input("Enter your name: ", key="name")
    user_email = st.text_input("Enter your email: ", key="user_email")
    phone_number = st.text_input("Enter your phone number: ", key="phone_number")
    pass1 = st.text_input("Enter your password: ", type="password", key="pass1")
    pass2 = st.text_input("ReEnter your password: ", type="password", key="pass2")

    cursor.execute("""select * from users""")
    records = cursor.fetchall()

    is_email = False
    email_validate_pattern = r"^\S+@\S+\.\S+$"
    if re.match(email_validate_pattern, user_email):
        is_email = True

    is_phone_number = False
    phone_validate_pattern = "^\\0?[0-9][0-9]{7,14}"
    if re.match(phone_validate_pattern, phone_number):
        is_phone_number = True

    if st.button("Xác nhận"):
        if pass1 == pass2:
            n = len(records)
            duplicate_email = False
            duplicate_phone = False
            if n > 0:
                for i in range(n):
                    if user_email == records[i][2]:
                        duplicate_email = True
                    if int(phone_number) == records[i][3]:
                        duplicate_phone = True
            if not duplicate_email and not duplicate_phone and is_email and is_phone_number:
                cursor.execute(f""" INSERT INTO users (user_name, user_email, phone_number, password)
                                    VALUES ('{name}', '{user_email}', '{phone_number}', '{pass2}')
                                    """, )
                st.success("Register Successfully")
            elif duplicate_email or duplicate_phone:
                st.error("This account already have, please check again! (email or phone number)")
            elif not is_email:
                st.error("Please enter a email valid!")
            elif not is_phone_number:
                st.error("Please enter a phone number valid!")
        else:
            st.error("Password not match, please check again!")

    st.markdown("""<a href="http://localhost:8502/" target="_self" style="font-size:16px;">Sign In</a>""", unsafe_allow_html=True)


register_user()
