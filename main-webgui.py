import streamlit as st
import functions


def add_todo():
    newTodo = st.session_state["newTodo"]
    todos.append(newTodo.title() + "\n")
    functions.addTodoToFile(todos)


print("START")
st.title("Todo Manager")
st.subheader("App to manage daily activities")

todos = functions.showTodos()
for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox == True:
        del st.session_state[todo]
        todos.pop(todos.index(todo))
        functions.addTodoToFile(todos)
        st.experimental_rerun()

newTodo = st.text_input(
    "todo",
    label_visibility="hidden",
    placeholder="Enter new or edit todo...",
    key="newTodo",
    on_change=add_todo,
)

st.session_state
