importnstreamlit as st
st.title("Моето мини-библиотечно приложение")
if "books" not in st.session_state:
st.session_state = []
st.header("+ Добави книга")
title = st.text_input("Заглавие")
author = st.text_input("Автор")
price = st.number_input("Цена", min_value=0.0)
if st.button("Добави книгата"):

book ={
"title": title, 
"author": author,
"price": price
}

st.session_state.books.append(book)
st.succwss("Книгата е добавена!")

if st.button("Покажи всички книги"):

if len(st.session_state.books) == 0:
st.write("Няма добавени  книги.")
else:
for book in st.session_state.books:
st.write("Заглавие:", books["tittle")
