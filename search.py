from tkinter import *
import mysql.connector
import sys


def nbook():
     uid=txt1.get()
     password=int(txt2.get())
     try:
          con=mysql.connector.connect(user='root',password='',host='localhost',database='login')
          print("database connected successfully")
          cursor=con.cursor()
          qry="select * from user where uid=%s"%\
               (uid)
          qry="select * from user where password=%s"%\
               (password)
          cursor.execute(qry)
          if cursor.rowcount>0:
               print("login successfully")
               messagebox.showinfo("welcome to nbook","welcome user.....")
          else:
               messagebox.showinfo("invalid","invalid uid and password")
               
     except mysql.connector.Error as err:
          print(err)
def funExit():
     sys.exit(0)
root=Tk()
root.geometry("400x400+100+100")
root.title("first gui")

lbl1=Label(root,text="enter user name")
lbl1.place(x=100,y=100)

txt1=Entry(root)
txt1.place(x=220,y=100)

lbl2=Label(root,text="enter password")
lbl2.place(x=100,y=130)

txt2=Entry(root)
txt2.place(x=220,y=130)

n=StringVar()
btn1=Button(root,text="enter",command=nbook)
btn1.place(x=220,y=270)


btn2=Button(root,text="exit",command=funExit)
btn2.place(x=240,y=300)
lbl3=Label(root,text=" ",textvariable=n)
lbl3.place(x=100,y=320)
root.mainloop()

          
