import psycopg2

conn = psycopg2.connect(host='localhost', port='5432', user='postgres', password='abcd1234')

cursor = conn.cursor()

conn.set_session(autocommit=True)

# cursor.execute("""
#     create TABLE users (
#     user_id serial not null primary key,
#     user_name varchar(255),
#     user_email varchar(255) unique,
#     password varchar(255)
#     )
# """)


def register_user():
    name = input("Enter your name: ")

    while True:
        email = input("Enter your email: ")
        pass1 = input("Enter your password: ")
        pass2 = input("ReEnter your password: ")

        if pass1 == pass2:
            try:
                print("Success!")
                break
            except psycopg2.IntegrityError:
                print("Error: This email already registered!")
        else:
            print("Password not match, please check your password!")

    cursor.execute(f"""
        INSERT INTO users (user_name, email, password)
        VALUES ('{name}', '{email}', '{pass2}')
    """, )

    print("You have successfully created an account.")


# register_user()


cursor.execute("""select * from users order by user_id""")
records = cursor.fetchall()
for record in records:
    print(record)


def delete_account_by_id():
    user_id = int(input("Enter user id to delete: "))
    cursor.execute(f"""
        delete from users
        where user_id = {user_id}
    """)

    print("Delete Success!")


# delete_account_by_id()


def delete_account_by_name():
    user_name = input("Enter user name to delete: ")
    cursor.execute(f"""
        delete from users
        where user_name = {user_name}
    """)

    print("Delete Success!")


# delete_account_by_name()


def delete_account_by_email():
    email = input("Enter email to delete: ")
    cursor.execute(f"""
        delete from users
        where email = {email}
    """)

    print("Delete Success!")


# delete_account_by_email()


def update_account_by_email_and_pass():
    email = input("Enter user email to sign in: ")
    password = input("Enter password: ")

    cursor.execute("""select * from users""")
    all_records = cursor.fetchall()
    n = len(all_records)

    for i in range(n):
        if email == all_records[i][2] and password == all_records[i][3]:
            print("Now you can update your account")
            drict_to_update = int(input("Enter field you want to update: "
                                        "Enter 1 for user name, "
                                        "2 for email, "
                                        "3 for password, "
                                        "and 0 for all: "))
            if drict_to_update == 0:
                user_name_new = input("Enter new user name: ")
                user_email_new = input("Enter new email: ")
                password_new = input("Enter new password: ")
                cursor.execute(f"""update users set user_name = '{user_name_new}' where user_name = '{all_records[i][1]}'""")
                cursor.execute(f"""update users set email = '{user_email_new}' where user_name = '{all_records[i][2]}'""")
                cursor.execute(f"""update users set password = '{password_new}' where password = '{all_records[i][3]}'""")
            if drict_to_update == 1:
                user_name_new = input("Enter new user name: ")
                cursor.execute(f"""update users set user_name = '{user_name_new}' where user_name = '{all_records[i][1]}'""")
            if drict_to_update == 2:
                user_email_new = input("Enter new email: ")
                cursor.execute(f"""update users set email = '{user_email_new}' where user_name = '{all_records[i][2]}'""")
            if drict_to_update == 3:
                password_new = input("Enter new password: ")
                cursor.execute(f"""update users set password = '{password_new}' where password = '{all_records[i][3]}'""")


update_account_by_email_and_pass()


cursor.execute("""select * from users order by user_id""")
records = cursor.fetchall()
for record in records:
    print(record)