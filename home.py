import psycopg2
import streamlit as st
from testapipython import response

conn = psycopg2.connect(host='localhost', port='5432', user='postgres', password='abcd1234')

cursor = conn.cursor()

conn.set_session(autocommit=True)

cursor.execute("""select * from sach""")
datas = cursor.fetchall()

style = open('style.css', 'r')
st.markdown(f"""<style>{style.read()}</style>""", unsafe_allow_html=True)

js_code = open('sach.js', 'r')
st.markdown(js_code.read(), unsafe_allow_html=True)


def remove_duplicate_list(x):
    return list(dict.fromkeys(x))


authors = []
books_name = []
book_imgs = []

for data in datas:
    books_name.append(data[1])
    authors.append(data[2])
    book_imgs.append(data[4])

authors = remove_duplicate_list(authors)
books_name = remove_duplicate_list(books_name)
book_imgs = remove_duplicate_list(book_imgs)

author_html = []

for i in range(len(authors)):
    author_html.append(f"""<a class="author" href="#">{authors[i]}</a>""")

wrap_author = f"""  <div class="authors">
                        {''.join(author_html)}     
                    </div>"""
st.markdown("""<h1>Các Tác Giả</h1>""", unsafe_allow_html=True)
st.markdown(wrap_author, unsafe_allow_html=True)

st.markdown("""""", unsafe_allow_html=True)
st.markdown("""<h1>Sách Mới</h1>""", unsafe_allow_html=True)


def render_book(i):
    return (f"""<div class="book_display">
    <a class="book_container" href="http://localhost:3000/sach/{i + 1}" target="_self">
        <img class="book_img book_img_{i + 1}" src="{book_imgs[i]}" alt="pics{i+1}" >
        <p class="book_name">{books_name[i]}</p>
        <a href="#" class="buy_now">
            <span>Mua Ngay</span>
        </a>
    </a>
    </div>""")


books_html = []


def render_all_books():
    for i in range(len(books_name)):
        books_html.append(render_book(i))
  