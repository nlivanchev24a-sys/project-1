st.title(" Оценки на ученици ")

if "grades" not in st.session_state:
    st.session_state.grades =
 {
        "Иван": [],
        "Мария": [],
        "Георги": []
    }

student = st.selectbox("Избери ученик", st.session_state.grades.keys())
grade = st.selectbox("Избери оценка", [2, 3, 4, 5, 6])

if st.button(" Запиши оценка "):
    st.session_state.grades[student].append(grade)
    st.success("Оценката е записана")

st.divider( )
st.subheader(" Статистика ")

if st.session_state.grades[student]:
    df = pd.DataFrame( st.session_state.grades[student], columns=["Оценка"] )

    st.write("Оценки на ученика")
    st.bar_chart(df["Оценка"].value_counts().sort_index())

    avg = sum(st.session_state.grades[student]) / len(st.session_state.grades[student])
    st.write(f"Среден успех: **{avg:.2f}**")
else:
    st.write("Няма въведени оценки")

