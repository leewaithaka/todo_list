import tkinter as tk
from tkinter import messagebox
app = tk.Tk()
app.title("To-Do List App")
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")
def delete_task():
    try:
        selected_task = listbox.get(listbox.curselection())
        listbox.delete(listbox.curselection())
    except:
        pass
label = tk.Label(app, text="Enter a task:")
entry = tk.Entry(app)
add_button = tk.Button(app, text="Add Task", command=add_task)
delete_button = tk.Button(app, text="Delete Task", command=delete_task)
listbox = tk.Listbox(app)
label.grid(row=0, column=0, padx=10, pady=10)
entry.grid(row=0, column=1, padx=10, pady=10)
add_button.grid(row=0, column=2, padx=10, pady=10)
delete_button.grid(row=0, column=3, padx=10, pady=10)
listbox.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
app.mainloop()
