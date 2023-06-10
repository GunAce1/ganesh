from tkinter import *
def getdata():
    print("Firstname is : %s"%(fname.get()))
    print("Lastname is : %s"%(lname.get()))

root=Tk()
root.configure(background='AntiqueWhite2')

root.geometry("800x600")
Label(text="Firstname: ",font="comissansms 20 bold italic",bg="yellow").grid(row=0,column=0)
Label(text="Lastname: ",font="comissansms 20 bold italic",bg="yellow").grid(row=1,column=0)
#Variable: StringVar,IntVar,DoubleVar,BooleanVar
fname=StringVar()
lname=StringVar()
Entry(root,textvariable=fname).grid(row=0,column=1)
Entry(root,textvariable=lname).grid(row=1,column=1)

Label(text="kaley ko hobbies: ",font="comissansms 20 bold italic",bg="yellow").grid(row=2,column=0)
Checkbutton(text="porn khelnay ").grid(row=2,column=1)
Checkbutton(text="gaja taneey ").grid(row=2,column=2)
Checkbutton(text="nihanng ko chak hanney").grid(row=2,column=3)
Checkbutton(text="kalo kando ").grid(row=2,column=4)

var=IntVar()
Label(text="gender: ",font="comissansms 20 bold italic",bg="yellow").grid(row=3,column=0)
Radiobutton(text="gay ",variable=var,value=1).grid(row=3,column=1)
Radiobutton(text="kt ",variable=var,value=2).grid(row=3,column=2)
Radiobutton(text="kta",variable=var,value=3).grid(row=3,column=3)


Button(text="submit",command=getdata).grid(row=4,column=0)

root.mainloop()