# my first todo app
import json

todos = []

def add(t):
    todos.append({"task": t, "done": False})
    print("added")

def remove(i):
    del todos[i]

def show():
    for i in range(len(todos)):
        status = "done" if todos[i]["done"] == True else "not done"
        print(str(i) + ". " + todos[i]["task"] + " - " + status)

def mark_done(i):
    todos[i]["done"] = True

def save():
    f = open("todos.json", "w")
    f.write(json.dumps(todos))
    f.close()

def load():
    f = open("todos.json", "r")
    global todos
    todos = json.loads(f.read())
    f.close()

while True:
    cmd = input("Enter command (add/remove/show/done/save/load/quit): ")
    if cmd == "add":
        task = input("Enter task: ")
        add(task)
    elif cmd == "remove":
        idx = int(input("Enter index: "))
        remove(idx)
    elif cmd == "show":
        show()
    elif cmd == "done":
        idx = int(input("Enter index: "))
        mark_done(idx)
    elif cmd == "save":
        save()
    elif cmd == "load":
        load()
    elif cmd == "quit":
        break
    else:
        print("unknown command")
