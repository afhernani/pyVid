#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hernani
#
# Created:     03/03/2019
# Copyright:   (c) hernani 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# _*_ coding:UTF-8 _*_

# use ffmplay to play the videos with tkinter

import tkinter as tk
import tkinter.ttk as ttk
import os


def main():
    root = tk.Tk()

    lb = tk.Listbox(root)
    lb.pack()

    for file in os.listdir():
        if file.endswith(".mp4"):
            lb.insert(0, file)
        if file.endswith(".flv"):
            lb.insert(0, file)

    root.mainloop()


if __name__ == '__main__':
    main()
