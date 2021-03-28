from tkinter import *
from tkinter import messagebox

def concat():
    f = "Фамилия " + fam.get()
    n = "Имя " + name.get()
    messagebox.showinfo("test",f + " " + n)

root = Tk()
root.geometry("800x600")
root.title("FIO")
btn = Button(text="Ok", 
             background="red", 
             foreground="blue", 
             font="20", 
             width="10", height="5", 
             command=concat)
btn.place(relx=.5, rely=.5)

fam = StringVar()
fam_entry = Entry(textvariable=fam)
fam_entry.place(relx=.5, rely=.1)

fam_label = Label(text="Фамилия: ")
fam_label.place(relx=.1, rely=.1)

name = StringVar()
name_entry = Entry(textvariable=name)
name_entry.place(relx=.5, rely=.2) 

name_label = Label(text="Имя: ")
name_label.place(relx=.1, rely=.2)

root.mainloop()