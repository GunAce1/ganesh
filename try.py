from tkinter import *
from tkinter import messagebox
root=Tk()
def exitwc():
    root.quit()
def wc():
    messagebox.showinfo("hello","Don po")

root.geometry("800x600")
Button(text="ON").pack()
Button(text="OFF",command=exitwc).pack(anchor="ne")
Button(root,text="welcome",command=wc).pack()
root.mainloop()