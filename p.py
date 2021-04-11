from tkinter import *
import os

def create():
    f = open(file.get(), 'w+')
    f.close()

def delete():
    os.remove(file.get())

root = Tk()
root.geometry("800x600")
root.title("Files")
btn = Button(text="Create file", 
             font="20", 
             width="10", height="5", 
             command=create)
btn.place(relx=.3, rely=.5)

btn = Button(text="Delete file", 
             font="20", 
             width="10", height="5", 
             command=delete)
btn.place(relx=.5, rely=.5)

file = StringVar()
file_entry = Entry(textvariable=file)
file_entry.place(relx=.5, rely=.1)

root.mainloop()