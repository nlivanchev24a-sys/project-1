import streamlit as st
st.title("My mini library app")
if books not in st.session_state:
  st.session_state.books = []
  st.header("Add book")
  title = st.text_input("title")
  author = st.text_imput("Author")
  price = st.text_imput("Price", min_value=0.0)
  if st.button("Add book"):
    book = { "title" : title,
            "author" : author,
            "price" : price}
    st.sessipn_state.books.appened(book)
    st.success("The book is added")

if st.button("Show all books"):
  if len(st.session_state.books) == 0:
    st.write("No added books")
  else:
    for book in st.session_state.books:
      st.write("Tite", book["title"])
      st.write("Author", book["author"])
      st.write("Price", book["price"])
      st.write("--------------------")

st.header("Serch by author")
search_author = st.text_input("Enter Author name:")
if st.button("Serch by author"):
  found = False
for book in st.session_state.books:
  if book["author"] == search_author:
    st.write(book)
    found = true
  in found = False:
  st.write("There are no books from this author")
st.header("Search by Title")
search_title = st.text_input("Enter title")
if st.button("Search by Title):
             found = False
for book in st.session_state.books:
  if book["title"] == search_title:
    st.write(book)
    found = true
  in found = False:
  st.write("There are no books from this title")
if st.button ("Show the cheapest book"):
  if len (st.session_state.books) == 0:
    st.write("There's no book")
  else:
    cheapest = st.session-state.books[0]
for book in st.session_state.books:
  if book["price"] < cheapest["price"]:
    cheapest = book
st.write("The cheapest book")
st.write(cheapest)
