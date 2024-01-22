import re
import psycopg2
import streamlit as st

conn = psycopg2.connect(host='localhost', port='5432', user='postgres', password='abcd1234')

cursor = conn.cursor()

conn.set_session(autocommit=True)


def forget_password():
    name = st.text_input("Enter your account name")
    user_email = st.text_input("Enter your account email")
    phone_number = st.text_input("Enter your account phone number")
    cursor.execute("""select * from users""")
    records = cursor.fetchall()

    get_pass = False
    n = len(records)
    index = -1

    is_email = False
    email_validate_pattern = r"^\S+@\S+\.\S+$"
    if re.match(email_validate_pattern, user_email):
        is_email = True

    is_phone_number = False
    phone_validate_pattern = "^\\0?[0-9][0-9]{7,14}"
    if re.match(phone_validate_pattern, phone_number):
        is_phone_number = True

    if st.button("Get Password"):
        if is_email and is_phone_number:
            for i in range(n):
                if name == records[i][1] and user_email == records[i][2] and int(phone_number) == records[i][3]:
                    get_pass = True
                    index = i

    if get_pass and index != -1:
        st.text(f"Your password is: {records[index][4]}")
    elif name != '' and user_email != '' and phone_number != '':
        st.error("Your info doesnt exist, please check again")

    js_code = """<style>a {font-size:14px}</style><a href="http://localhost:8502" target="_self"> Sign In </a>"""
    st.markdown(js_code, unsafe_allow_html=True)


forget_password()
