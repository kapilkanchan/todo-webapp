FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the
    list of to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_list, filepath=FILEPATH):
    """ Write the to-do items list in a text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_list)


print(__name__)
if __name__ == "__main__":
    print("hello from functions")