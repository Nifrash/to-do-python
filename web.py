import streamlit as st
import functions



todos = functions.get_todos()
def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

todo_items = functions.get_todos()

st.title("Hello Akp")
st.subheader("This is TODO")
st.write("This make you things Remember")

st.text_input(label="Enter Your TODO", placeholder="your Plan", on_change=add_todo, key="new_todo")

for index, item in enumerate(todo_items):
    checked = st.checkbox(item, key=item)
    if checked:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item]
        st.rerun()

st.session_state


