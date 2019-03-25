# -*- coding: utf-8 -*-
# use ffmplay to play the videos with tkinter

import tkinter as tk
import tkinter.ttk as ttk
import os
from subprocess import call
from threading import Thread


def main():
    root = tk.Tk()
    root.geometry("400x400")
    lb = tk.Listbox(root, width=60, height=10)
    lb.grid(column=0, row=0, sticky="WE")


    def doubleclickbutton(event):
        if lb.curselection():
            file = lb.curselection()[0]
            print(lb.get(file))
            thread = Thread(target=tarea, args=("ffplay " + "\"" + lb.get(file) + "\"",))
            thread.daemon = True
            thread.start()

    def ffexec(event):
        print("ffexec ..")
        if lb.curselection():
            file = lb.curselection()[0]
            # os.startfile(lb.get(file), operation="start")
            print(lb.get(file))
            print(os.getcwd())
            current_file = os.getcwd() + '\\' + lb.get(file)
            print(current_file)
            run_code = call(["ffplay ", current_file])
            print(run_code)

    def ffplay(event):
        if lb.curselection():
            file = lb.curselection()[0]
            print(lb.get(file))
            # os.system("ffplay " + lb.get(file))
            thread = Thread(target=tarea, args=("ffplay " + "\"" + lb.get(file) + "\"",))
            thread.daemon = True
            thread.start()

    def tarea(args=None):
        if not args:
            return
        os.system(args)

    def init_listbox() -> object:
        """ listar los ficheros en el directorio."""
        for file in os.listdir():
            if file.endswith(".mp4"):
                lb.insert(0, file)
            if file.endswith(".flv"):
                lb.insert(0, file)

    init_listbox()
    bstart = ttk.Button(root, text="Start movie")
    bstart.grid(column=0, row=1, sticky="WE")
    bstartexe = ttk.Button(root, text='Start exec')
    bstartexe.grid(column=0, row=2, sticky="WE")

    bstart.bind("<ButtonPress-1>", ffplay)
    bstartexe.bind("<ButtonPress-1>", ffexec)
    lb.bind('<Double-Button-1>', doubleclickbutton)
    root.mainloop()
    #root.destroy()


if __name__ == '__main__':
    main()
