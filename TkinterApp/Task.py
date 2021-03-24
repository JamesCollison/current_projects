import tkinter as tk


class Task(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(background='green')
        self.pack_propagate(False)

        f1 = tk.Frame(self)
        f1.pack_propagate(False)
        f1.config(background="blue")
        f1.pack(side="top", fill="both", expand=True)
        f1.grid_columnconfigure(0, weight=1)
        f1.grid_rowconfigure(0, weight=1)
        f1.grid_rowconfigure(1, weight=1)

        b1 = tk.Button(f1, text="CURRENT TASK \n small desc")
        b1.grid(row=0, column=0, sticky="nsew")
        b2 = tk.Button(f1, text="NEXT TASK \n small desc")
        b2.grid(row=1, column=0, sticky="nsew")

