from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk
import sqlite3
import tkinter.messagebox
root=tk.Tk()
#v = tk.StringVar()
global combo,combo1,combo2,combo3
global rollno
class Student:
   rollno = 0
   student_name = ""
   father_name = ""
   post = ""
   select = ""
   city = ""
   course = ""
   dist = ""
   state = ""
   pincode = 0
   email = ""
   dob = ""
   mno = 0

   def __init__(self, rollno, student_name, father_name, post, select, city, course, dist, state, pincode, email, dob,mno):
       self.rollno = rollno
       self.student_name = student_name
       self.father_name = father_name
       self.post = post
       self.select = select
       self.city = city
       self.course = course
       self.dist = dist
       self.state = state
       self.pincode = pincode
       self.email = email
       self.dob = dob
       self.mno = mno


def ad():
    try:
        global combo, combo1, combo2, combo3
        global ROLLNO, STUDENT_NAME, FATHER_NAME, POSTOL_ADDRESS, CITY, COURSE, DISTRICT, STATE, PINCODE, EMAILID, DOB, MOBNO
        global rollno, student_name, father_name, post, select, city, course, dist, state, pincode, email, dob, mno
        global combo, combo1, combo2, combo3,comboo
        v = tk.StringVar()
        rollno=rollno.get()
        #rollno.delete(0, END)
        student_name=student_name.get()
        #student_name.delete(0, END)
        father_name=father_name.get()
        #father_name.delete(0,END)
        post=post.get()
        #post.delete(0,END)
        #select =v.get()
        #print(select)
        select=comboo.get()
        #comboo.current(0)
        city=city.get()
        #combo.current(0)
        course=course.get()
        #combo1.current(0)
        dist=dist.get()
        #combo2.current(0)
        state=state.get()
        #combo3.current(0)
        pincode=pincode.get()
        #pincode.delete(0,END)
        #pincode.delete(0,END)
        email=email.get()
        #email.delete(0,END)
        dob=dob.get()
        #dob.delete(0,END)
        mno=mno.get()
        #mno.delete(0,END)
        con.execute("INSERT INTO management VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", (rollno, student_name,father_name,post,select,city,course,dist,state,pincode,email,dob,mno))
        con.commit()
        tkinter.messagebox.showinfo("msg", "Record inserted successfully")
    except Exception as e:
        print(e)
def rf():
    try:
        global  student_name, father_name, post, select, city, course, dist, state, pincode, email, dob, mno
        c = con.cursor()
        nn = mm.get()
        mm.delete(0,END)
        c.execute('DELETE FROM management WHERE ROLLNO=?',(nn,))

        #c.execute("DELETE FROM management(ROLLNO) VALUES (?)",(rollno))
        #c.execute('DELETE FROM management WHERE ROLLNO = ' + rollno)
        con.commit()
        tkinter.messagebox.showinfo("msg", "Record deleted successfully")
    except Exception as e:
        print(e)
def delete():
    try:
        global mm
        dell = tk.Tk()
        dell.geometry('1000x600')
        tk.Label(dell,text="Enter the rollnumber for delete",fg="blue").grid(row=0)
        mm=int
        mm= Entry(dell, textvariable=mm)
        mm.grid(row=0, column=1)
        bb=tk.Button(dell,text="Delete",fg="green",command=rf)
        bb.grid(row=1,column=1)
        dell.mainloop()

    except Exception as e:
        print(e)

def ho():
    try:
        global ROLLNO,STUDENT_NAME,FATHER_NAME,POSTOL_ADDRESS,CITY,COURSE,DISTRICT,STATE,PINCODE,EMAILID,DOB,MOBNO
        global rollno, student_name, father_name, post, select, city, course, dist, state, pincode, email, dob, mno
        global combo, combo1, combo2, combo3,comboo
        v = tk.StringVar()
        newwindow =tk.Tk()
        #newwindow=Toplevel(root)
        newwindow.geometry('900x1600')
        tk.Label(newwindow, text="_________STUDENT FORM________", font="Helvetica 20 bold italic").place(x=300, y=30)
        tk.Label(newwindow, text="Rollno", font="Helvetica 17 bold italic").place(x=340, y=90)
        tk.Label(newwindow, text="Student Name", font="Helvetica 17 bold italic").place(x=340, y=130)
        tk.Label(newwindow, text="Fathers Name", font="Helvetica 17 bold italic").place(x=340, y=170)
        tk.Label(newwindow, text="Postol Address", font="Helvetica 17 bold italic").place(x=340, y=210)
        tk.Label(newwindow, text="Gender", font="Helvetica 17 bold italic").place(x=340, y=250)
        tk.Label(newwindow, text="City", font="Helvetica 17 bold italic").place(x=340, y=330)
        tk.Label(newwindow, text="Course", font="Helvetica 17 bold italic").place(x=340, y=370)
        tk.Label(newwindow, text="District", font="Helvetica 17 bold italic").place(x=340, y=410)
        tk.Label(newwindow, text="State", font="Helvetica 17 bold italic").place(x=340, y=450)
        tk.Label(newwindow, text="Pincode", font="Helvetica 17 bold italic").place(x=340, y=490)
        tk.Label(newwindow, text="Email", font="Helvetica 17 bold italic").place(x=340, y=530)
        tk.Label(newwindow, text="Date Of Birth", font="Helvetica 17 bold italic").place(x=340, y=570)
        tk.Label(newwindow, text="Mobile_Number", font="Helvetica 17 bold italic").place(x=340, y=610)
        rollno= StringVar()
        rollno = Entry(newwindow)
        student_name=StringVar()
        student_name = Entry(newwindow)
        father_name=StringVar()
        father_name = Entry(newwindow)
        post=StringVar()
        post = Entry(newwindow)
        comboo = Combobox(newwindow)
        comboo['values'] = ("male", "female")
        comboo.current(0)
        #global v
        #r1 = tk.Radiobutton(newwindow, text="male", variable=v , value="m",fg="blue")
        #r2 = tk.Radiobutton(newwindow, text="female", variable=v , value="f",fg="blue")
        # city
        city=StringVar()
        city=Entry(newwindow)
        """combo= Combobox(newwindow)
        combo['values'] = ("magalore","bangalore")
        combo.current(0)"""
        # course
        course = StringVar()
        course = Entry(newwindow)
        """combo1 =Combobox(newwindow)
        combo1['values'] = ("mca", "mtech")
        combo1.current(0)"""
        # district
        dist= StringVar()
        dist = Entry(newwindow)
        """combo2=Combobox(newwindow)
        combo2['values']=("D.K","U.K")
        combo2.current(0)"""
        # state
        state = StringVar()
        state = Entry(newwindow)
        """combo3 = Combobox(newwindow)
        combo3['values'] = ("karnataka", "kerala")
        combo3.current(0)"""
        pincode = StringVar()
        pincode = Entry(newwindow)
        email = StringVar()
        email = Entry(newwindow)
        dob = StringVar()
        dob = Entry(newwindow)
        mno = StringVar()
        mno = Entry(newwindow)
        rollno.place(x=540, y=90)
        student_name.place(x=540, y=130)
        father_name.place(x=540, y=170)
        post.place(x=540, y=210)
        comboo.place(x=540, y=250)
        city.place(x=540, y=330)
        course.place(x=540, y=370)
        dist.place(x=540, y=410)
        state.place(x=540, y=450)
        pincode.place(x=540, y=490)
        email.place(x=540, y=530)
        dob.place(x=540, y=570)
        mno.place(x=540, y=610)
        button = tk.Button(newwindow, text="Add", command=ad, font="Helvetica 17 bold italic")
        button.place(x=540, y=650)
        rollno.place(x=540, y=90)
        student_name.place(x=540, y=130)
        father_name.place(x=540, y=170)
        post.place(x=540, y=210)
        comboo.place(x=540, y=250)
        #r2.place(x=540, y=290)
        city.place(x=540, y=330)
        course.place(x=540, y=370)
        dist.place(x=540, y=410)
        state.place(x=540, y=450)
        pincode.place(x=540, y=490)
        email.place(x=540, y=530)
        dob.place(x=540, y=570)
        mno.place(x=540, y=610)
        button = tk.Button(newwindow, text="Add", command=ad, font="Helvetica 17 bold italic")
        button.place(x=540, y=650)
        newwindow.mainloop()
    except Exception as e:
        print(e)
def dis():
    root3 = tk.Tk()
    tree = ttk.Treeview(root3)
    tree["columns"] = ("1", "2", "3", "4","5","6","7","8","9","10","11","12","13")
    tree.column("1",width=90)
    tree.column("2",width=90)
    tree.column("3",width=90)
    tree.column("4", width=90)
    tree.column("5", width=90)
    tree.column("6", width=90)
    tree.column("7", width=90)
    tree.column("8", width=90)
    tree.column("9", width=90)
    tree.column("10", width=90)
    tree.column("11", width=90)
    tree.column("12", width=90)
    tree.column("13", width=90)
    tree.heading("1", text="rollno")
    tree.heading("2", text="student_name")
    tree.heading("3", text="father_name")
    tree.heading("4", text="address")
    tree.heading("5", text="gender")
    tree.heading("6", text="city")
    tree.heading("7", text="course")
    tree.heading("8", text="district")
    tree.heading("9", text="state")
    tree.heading("10", text="pincode")
    tree.heading("11", text="email")
    tree.heading("12", text="dob")
    tree.heading("13", text="mno")
    mm=con.execute("SELECT * FROM management")
    i=0
    for row in mm:
        tree.insert('',0,values=(row[0],row[1], row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]))
        i=i+1
    tree.pack()
    root3.mainloop()

root.title("student")
con = sqlite3.connect('mana.db')
root.geometry("1200x1200")
menubar = Menu(root, bg="blue")
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="FEATURES", menu=filemenu)
filemenu.add_command(label="ADD", command=ho)
filemenu.add_command(label="DELETE",command=delete)
filemenu.add_command(label="DISPLAY", command=dis)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.quit)
root.config(menu=menubar)
#TABLE_NAME = "management"
ROLLNO="rollno"
STUDENT_NAME = "student_name"
FATHER_NAME ="father_name"
POSTOL_ADDRESS="post"
SEX="select"
CITY="city"
COURSE="course"
DISTRICT="dist"
STATE="state"
PINCODE="pincode"
EMAILID="email"
DOB="dob"
MOBNO="mno"
con.execute('''CREATE TABLE IF NOT EXISTS management
        ( ROLLNO TEXT PRIMARY KEY     NOT NULL,
         STUDENT_NAME         TEXT    NOT NULL,
         FATHER_NAME          TEXT,
         POSTOL_ADDRESS       TEXT,
        SEX                  CHAR(10),
        CITY                 CHAR(50),
        COURSE               CHAR(50),
        DISTRICT             CHAR(50),
        STATE                CHAR(50),
        PINCODE              INT(6),
        EMAILID              TEXT,
        DOB                  TEXT,
        MOBNO                INT);''')
c = con.cursor()
root.configure(background='#00008B')
root.mainloop()

