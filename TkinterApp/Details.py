import tkinter as tk


class Details(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.pack_propagate(False)
        self.configure(background="yellow")

        lbl_frame = tk.Frame(self)
        lbl_frame.config(background='purple')
        lbl_frame.pack(side="top", fill="both", expand=True)

        lbl_frame.grid_columnconfigure(0, weight=1)
        lbl_frame.grid_columnconfigure(1, weight=1)
        lbl_frame.grid_rowconfigure(0, weight=10)
        lbl_frame.grid_rowconfigure(1, weight=1)

        lbl1 = tk.Label(lbl_frame, text='TASK DESCRIPTION \n\n'
                                        'TASK DESCRIPTION \n'
                                        'TASK DESCRIPTION \n'
                                        'TASK DESCRIPTION \n', background='white')
        lbl1.grid(row=0, column=0, sticky="nsew", columnspan=2)

        b1 = tk.Button(lbl_frame, text="PASS")
        b1.grid(row=1, column=0, sticky="nsew")
        b2 = tk.Button(lbl_frame, text="FAIL")
        b2.grid(row=1, column=1, sticky="nsew")

