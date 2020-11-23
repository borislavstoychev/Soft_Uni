command = input()
todo_list = [0] * 10
while not command == "End":
    importance, value = command.split("-")
    importance = int(importance)
    todo_list.insert(importance, value)
    todo_list.remove(0)

    command = input()

list_importance = list(values for values in todo_list if not values == 0)

print(list_importance)
