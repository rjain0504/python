from tkinter import *
def calbill():
     bill=0
     if a1.get()==1:
          bill=bill+250
     if a2.get()==1:
          bill=bill+130
     if a3.get()==1:
          bill=bill+80
     
     messagebox.showinfo("bill","Your bill is "+str(bill))

root=Tk()
root.geometry("500x500+50+50")
root.title("Pizza Caffe")

a1=IntVar()
a2=IntVar()
a3=IntVar()
lbl1=Label(root,text="BHATIA PIZZA CAFFE")
lbl1.place(x=100,y=50)

chkpiz=Checkbutton(root,text="PIZZA 250/-",variable=a1)
chkbur=Checkbutton(root,text="BURGER 130/-",variable=a2)
chkchow=Checkbutton(root,text="CHOWMIN 80/-",variable=a3)

chkpiz.place(x=80,y=80)
chkbur.place(x=80,y=110)
chkchow.place(x=80,y=150)

btnbill=Button(root,text="MyBill",command=calbill)
btnbill.place(x=160,y=190)



root.mainloop()
