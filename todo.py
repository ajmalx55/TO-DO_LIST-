from tkinter import *
from tkinter import ttk

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do-list')
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text="To-Do List App", font='Arial 25 bold', width=15, bd=5, bg='orange', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task', font='Arial 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text="Tasks", font='Arial 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font="Arial 20 italic bold")
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='Arial 10 bold')
        self.text.place(x=20, y=120)

        # Function to add a task
        def add_task():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content)
            self.text.delete(1.0, END)

        # Function to delete a task
        def delete_task():
            delete = self.main_text.curselection()
            self.main_text.delete(delete)
            with open('data.txt', 'r+') as f:
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    if line.strip() != self.main_text.get(delete):
                        f.write(line)
                f.truncate()

        # Function to mark a task as completed
        def mark_as_completed():
            selected = self.main_text.curselection()
            self.main_text.itemconfig(selected, {'bg': 'orange', 'fg': 'black'})

        # Function to delete all completed tasks
        def delete_completed_tasks():
            for i in range(self.main_text.size()):
                if self.main_text.itemcget(i, 'bg') == 'orange':
                    self.main_text.delete(i)
            with open('data.txt', 'r+') as f:
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    if line.strip() not in [self.main_text.get(i) for i in range(self.main_text.size())]:
                        f.write(line)
                f.truncate()

        # Function to clear all tasks
        def clear_all_tasks():
            self.main_text.delete(0, END)
            open('data.txt', 'w').close()

        # Read tasks from file and display
        with open('data.txt', 'r') as file:
            for line in file.readlines():
                self.main_text.insert(END, line.strip())

        self.button_add = Button(self.root, text="Add", font='Arial 20 bold italic', width=10, bd=5, bg='orange', fg='black', command=add_task)
        self.button_add.place(x=30, y=180)

        self.button_delete = Button(self.root, text="Delete", font='Arial 20 bold italic', width=10, bd=5, bg='orange', fg='black', command=delete_task)
        self.button_delete.place(x=30, y=280)

        self.button_completed = Button(self.root, text="Mark as Completed", font='Arial 16 bold italic', width=18, bd=5, bg='orange', fg='black', command=mark_as_completed)
        self.button_completed.place(x=20, y=330)

        self.button_delete_completed = Button(self.root, text="Delete Completed", font='Arial 16 bold italic', width=18, bd=5, bg='orange', fg='black', command=delete_completed_tasks)
        self.button_delete_completed.place(x=20, y=380)

        self.button_clear_all = Button(self.root, text="Clear All Tasks", font='Arial 16 bold italic', width=18, bd=5, bg='orange', fg='black', command=clear_all_tasks)
        self.button_clear_all.place(x=420, y=330)


def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()