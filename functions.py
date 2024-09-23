FILE_PATH = "todos.txt"

def get_todos(filepath=FILE_PATH):
    with open(FILE_PATH, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todo_arg, filepath=FILE_PATH):
    with open(filepath, 'w') as file:
        file.writelines(todo_arg)

# if __name__ == '__main__':
#     print("Hello")