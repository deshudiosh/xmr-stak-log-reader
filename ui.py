from tkinter import Tk
from tkinter.constants import *
from tkinter.ttk import Treeview
from typing import List

from log_reader import Session


def show(sessions: List[Session]):
    root = Tk()

    tree = Treeview(root)

    tree["columns"] = ("date_start", "date_end", "duration", "hashrate")
    # tree.column("one", width=100)
    # tree.column("two", width=100)

    tree.heading("date_start", text="Start")
    tree.column("date_start", width=130, stretch=NO)
    tree.heading("date_end", text="End")
    tree.column("date_end", width=130, stretch=NO)
    tree.heading("duration", text="Duration")
    tree.column("duration", width=80, stretch=NO)
    tree.heading("hashrate", text="Hashrate")
    tree.column("hashrate", width=80, stretch=NO)

    tree.column('#0', width=50, stretch=NO)


    for idx, s in enumerate(sessions):
        tree.insert("", idx, text=idx+1, values=(s.date_start, s.date_end, s.duration, s.hashrate))

    tree.pack(expand=YES, fill=BOTH)
    root.mainloop()

