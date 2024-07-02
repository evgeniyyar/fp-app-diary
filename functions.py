FILEPATH = "todos.txt"


def read_todos(filepath=FILEPATH):
    """Функция читает файл и возвращает построчный список"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """Функция записывает в файл построчно индексы списка"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)


#print(__name__)

#if __name__ == "functions":
#    print("hello")



