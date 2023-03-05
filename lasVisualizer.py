import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd

import tkfilebrowser

import sys, os

from fnmatch import fnmatch

import numpy as np

import matplotlib.pyplot as plt

import welly

def read_filePath():
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)

    filePath = fd.askopenfilename()

    return(filePath)

def read_filePaths():
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)

    filePaths = fd.askopenfilenames()

    return(filePaths)

def read_folderPaths():
    root = tk.Tk()
    root.geometry('200x200')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.wm_attributes('-topmost', 1)

    dirs = []

    def get_directories():
        dirs.append(tkfilebrowser.askopendirnames())
        return dirs

    b1 = Button(root, text='select directories...', command=get_directories)
    b1.pack(pady=20)

    # Button for closing
    exit_button = Button(root, text="Exit", command=root.destroy)
    exit_button.pack(pady=20)


    root.mainloop()

    # Creating one list in case the 'Select folder' button was used multiple times
    folderPaths = list()
    for dir in dirs:
        [folderPaths.append(sub_dir) for sub_dir in dir]
    folderPaths = [*set(folderPaths)]

    return(folderPaths)

def read_folderPath():
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)

    folderPath = fd.Directory()
    return(folderPath.show())


def main():
    # Run main functions
    lasPath = read_filePath()
    print(lasPath)

    print(welly.__version__)
    myWell, = welly.read_las(lasPath)
    myWell.plot()



if __name__ == "__main__":
    main()