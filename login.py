import psycopg2
import streamlit as st

conn = psycopg2.connect(host='localhost', port='5432', user='postgres', password='abcd1234')

cursor = conn.cursor()

conn.set_session(autocommit=True)


def login_form():
    cursor.execute("""select * from users""")
    records = cursor.fetchall()

    email_input = st.text_input("Enter your email: ", key='email_input')
    password_input = st.text_input("Enter your password: ", key='password')

    login_status = False

    if st.button("Login"):
        for i in range(len(records)):
            if email_input == records[i][2] and password_input == records[i][4]:
                login_status = True

    if login_status:
        st.success('Login Successfully')

    js_code = """<style>a{font-size:14px}</style><a href="http://localhost:8503" target="_self">Forget Password?</a>"""
    st.markdown(js_code, unsafe_allow_html=True)

    js_code = """<style>a {font-size:14px}</style><a href="http://localhost:8501" target="_self"> Sign Up </a>"""
    st.markdown(js_code, unsafe_allow_html=True)

    return login_status


login_form()
