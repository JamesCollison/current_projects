import tkinter as tk

from Task import Task
from Details import Details
from Header import Header


class UI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.grid_config()
        container = self.container_config()
        self.create_header_ui(container)
        self.create_task_ui(container)
        self.create_details_ui(container)

    def create_header_ui(self, container):
        header = Header(container, self)
        header.grid(row=0, column=0, columnspan=2, sticky="nsew")

    def create_details_ui(self, container):
        details = Details(container, self)
        details.grid(row=1, column=1, sticky="nsew")

    def create_task_ui(self, container):
        task = Task(container, self)
        task.grid(row=1, column=0, sticky="nsew")

    def grid_config(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def container_config(self):
        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew")
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)
        container.grid_rowconfigure(0, weight=1)
        container.grid_rowconfigure(1, weight=10)
        return container


interface = UI()
interface.minsize(400, 200)
interface.mainloop()
