from tkinter import *

def showMessage():
     n=txtname.get()
     if a1.get()==1:
          messagebox.showinfo("info","hello..MR.."+n)
     else:
          messagebox.showinfo("info","hello..Miss"+n)
root=Tk()
root.geometry("500x500+100+100")
a1=IntVar()

lblname=Label(root,text="Enter your name")

txtname=Entry(root)

rdmale=Radiobutton(root,text="Male",variable=a1,value=1)
rdfemale=Radiobutton(root,text="Female",variable=a1,value=2)

btncheck=Button(root,text="Check",command=showMessage)


lblname.place(x=100,y=50)
txtname.place(x=220,y=50)

rdmale.place(x=100,y=100)
rdfemale.place(x=220,y=100)

btncheck.place(x=150,y=150)



root.mainloop()
