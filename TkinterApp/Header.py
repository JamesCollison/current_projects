import tkinter as tk


class Header(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.pack_propagate(False)
        self.controller = controller
        self.pack_propagate(False)

        lbl_frame = tk.Frame(self)
        lbl_frame.pack_propagate(False)
        lbl_frame.pack(side="top", fill="both", expand=True)

        lbl_frame.grid_columnconfigure(0, weight=1)
        lbl_frame.grid_columnconfigure(1, weight=1)
        lbl_frame.grid_rowconfigure(0, weight=1)

        lbl1 = tk.Label(lbl_frame, text='TIME_REMAINING', background='grey')
        lbl1.grid(row=0, column=0, sticky="nsew")
        lbl2 = tk.Label(lbl_frame, text='999/999 completed', background='grey')
        lbl2.grid(row=0, column=1, sticky="nsew")
