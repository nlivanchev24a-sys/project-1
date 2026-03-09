import streamlit as st

st.title("My mini library app")

# Инициализация на списъка с книги
if "books" not in st.session_state:
    st.session_state.books = []

st.header("Add book")
title = st.text_input("Title")
author = st.text_input("Author")
price = st.number_input("Price", min_value=0.0, step=0.1)

if st.button("Add book"):
    if title and author:
        book = {"title": title, "author": author, "price": price}
        st.session_state.books.append(book)
        st.success("The book is added")
    else:
        st.error("Please fill in title and author")

if st.button("Show all books"):
    if not st.session_state.books:
        st.write("No added books")
    else:
        for book in st.session_state.books:
            st.write(f"Title: {book['title']} | Author: {book['author']} | Price: {book['price']}")
            st.write("--------------------")

st.header("Search by author")
search_author = st.text_input("Enter Author name:")
if st.button("Search by author"):
    found = False
    for book in st.session_state.books:
        if book["author"].lower() == search_author.lower():
            st.write(book)
            found = True
    if not found:
        st.write("There are no books from this author")

st.header("Search by Title")
search_title = st.text_input("Enter title to search:")
if st.button("Search by Title"):
    found = False
    for book in st.session_state.books:
        if book["title"].lower() == search_title.lower():
            st.write(book)
            found = True
    if not found:
        st.write("There are no books with this title")

if st.button("Show the cheapest book"):
    if not st.session_state.books:
        st.write("There's no book")
    else:
        cheapest = st.session_state.books[0]
        for book in st.session_state.books:
            if book["price"] < cheapest["price"]:
                cheapest = book
        st.write("The cheapest book is:")
        st.write(cheapest)
