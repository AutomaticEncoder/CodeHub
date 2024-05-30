from tkinter import *
import plyer
root = Tk()
root.title('CodeHub')
root.geometry('300x300')
root.resizable(width = False, height = False)
def projects():
    def new():
        def post():
            codes = code_input.get(1.0, END)
            j = e.get()
            name_project = input('Name project:')
            plyer.notification.notify(title = 'CodeHub',
                                      message = 'Code posted!')
            l = Label(project, text = f'{j}:')
            l.pack()
            l1 = Label(project, text = f'{codes}',
                       fg = 'blue')
            l1.pack()
            with open('main.py', 'r') as codehub:
                lines = codehub.readlines()
                lines.insert(15, f'l = Label(project, text = f"{j}:")\n')
                lines.insert(16, 'l.pack()\n')
                lines.insert(17, f'l1 = Label(project, text = f"{codes}",\n')
                lines.insert(18, 'fg = "blue")\n')
                lines.insert(19, 'l1.pack()\n')
            with open('main.py', 'w') as codehub:
                codehub.writelines(lines)
        code = Tk()
        menu = Menu(code)
        projects = Menu(menu, tearoff = 0)
        projects.add_command(label = 'Post code', command = post)
        menu.add_cascade(label = 'Project', menu = projects)
        code.title('Code')
        code.geometry('500x500')
        code_input = Text(code, fg = 'blue', width = 5000, height = 5000)
        code_input.insert(1.0, 'Enter a code')
        code_input.pack()
        code.config(menu = menu)
        code.mainloop()
    project = Tk()
    project.title('Projects')
    project.geometry('1440x900')
    b1 = Button(project, text = 'New Project',
           command = new)
    b1.pack()
    project.mainloop()
e = Entry(root)
e.insert(0, 'Name')
e.pack()
b = Button(root, text = 'Projects',
           command = projects)
b.pack()
root.mainloop() мои гитхаб
