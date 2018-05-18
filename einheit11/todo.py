import Tkinter

todos = [
    'groceries',
    'taxes',
    'cooking'
]

window = Tkinter.Tk()

def add_todo():
    todo_label = Tkinter.Label(window, text=new_todo_entry.get())
    todo_label.pack()

new_todo_entry = Tkinter.Entry(window)
new_todo_entry.pack()
new_todo_button = Tkinter.Button(window, text="Add", command=add_todo)
new_todo_button.pack()

for todo in todos:
    # gehe alle Eintraege in todos durch
    # Erstelle ein Label mit dem entsprechenden Text
    todo_label = Tkinter.Label(window, text=todo)
    todo_label.pack()

# todo: als erledigt kennzeichnen

window.mainloop()