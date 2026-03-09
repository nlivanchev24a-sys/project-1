import streamlit as st

st.title("My mini library app")

# Инициализация на сесията - името на ключа трябва да е в кавички
if "books" not in st.session_state:
    st.session_state.books = []

st.header("Add book")
title = st.text_input("Title")
author = st.text_input("Author")
# Използваме number_input за цена, за да можем да сравняваме числа
price = st.number_input("Price", min_value=0.0, step=0.01)

if st.button("Add book"):
    if title and author:
        book = {
            "title": title,
            "author": author,
            "price": price
        }
        st.session_state.books.append(book)
        st.success(f"Книгата '{title}' беше добавена успешно!")
    else:
        st.error("Моля, попълнете заглавие и автор.")

if st.button("Show all books"):
    if not st.session_state.books:
        st.write("No added books")
    else:
        for book in st.session_state.books:
            st.write(f"**Title:** {book['title']} | **Author:** {book['author']} | **Price:** {book['price']:.2f}")
            st.write("---")

st.header("Search by author")
search_author = st.text_input("Enter Author name:")
if st.button("Search by author"):
    found = False
    for book in st.session_state.books:
        if search_author.lower() in book["author"].lower():
            st.write(book)
            found = True
    if not found:
        st.write("There are no books from this author")

st.header("Search by Title")
search_title = st.text_input("Enter title")
if st.button("Search by Title"):
    found = False
    for book in st.session_state.books:
        if search_title.lower() in book["title"].lower():
            st.write(book)
            found = True
    if not found:
        st.write("There are no books with this title")

if st.button("Show the cheapest book"):
    if not st.session_state.books:
        st.write("There are no books in the library.")
    else:
        # Намиране на най-евтината книга чрез функцията min
        cheapest = min(st.session_state.books, key=lambda x: x['price'])
        st.write("### The cheapest book:")
        st.write(f"Title: {cheapest['title']}")
        st.write(f"Author: {cheapest['author']}")
        st.write(f"Price: {cheapest['price']:.2f}")
