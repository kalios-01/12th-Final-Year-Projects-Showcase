from tkinter import *
import pymysql
from PIL import ImageTk, Image

mydb = pymysql.connect(user='root', password='1234')
cur = mydb.cursor()


def Viewregist():
    view_r = Toplevel()
    view_r.title('Registration Page')
    view_r.geometry('2000x2000')
    view_r.config(bg='sky blue')
    path1 = r'2.jpg'
    image1 = ImageTk.PhotoImage(Image.open(path1))
    image1_label = Label(view_r, image=image1, height=1000, width=1500)
    image1_label.image = image1
    image1_label.place(x=0, y=0)
    new_label = Label(view_r, text='VIEW REGISTRATION', fg='white', bg='black', bd=6, relief=RAISED, font=('ariel', 30))
    new_label.place(x=570, y=20)

    # ------------------Labels---------------------------
    new_name = Label(view_r, text="First Name", bd=5, bg='white', font=('ariel', 18))
    new_name.place(x=480, y=200)
    new_last = Label(view_r, text="Last Name", bd=5, bg='white', font=('ariel', 18))
    new_last.place(x=770, y=200)
    # new_age = Label(view_r, text="Patient's Age", bg='white', bd=5, font=('ariel', 18))
    # new_age.place(x=550, y=250)

    # ------------------Entry---------------------------
    name_e = Entry(view_r, width=20, bd=6)
    name_e.place(x=620, y=200)
    last_e = Entry(view_r, width=20, bd=6)
    last_e.place(x=910, y=200)

    # num_e = Entry(view_r, width=40, bd=6)
    # num_e.place(x=750, y=250)

    def submit():
        view = Toplevel()
        view.title('Registration Page')
        view.geometry('2000x2000')
        view.config(bg='sky blue')
        path1 = r'2.jpg'
        image1 = ImageTk.PhotoImage(Image.open(path1))
        image1_label = Label(view, image=image1, height=1000, width=1500)
        image1_label.image = image1
        image1_label.place(x=0, y=0)
        new_label = Label(view, text='VIEW REGISTRATION', fg='white', bg='black', bd=6, relief=RAISED,
                          font=('ariel', 30))
        new_label.place(x=570, y=20)

        # ------------------Labels---------------------------
        new_name = Label(view, text="First Name", relief=RAISED, bd=2, bg='white', font=('ariel', 18))
        new_name.place(x=480, y=200)
        new_last = Label(view, text="Last Name", relief=RAISED, bd=2, bg='white', font=('ariel', 18))
        new_last.place(x=770, y=200)
        new_age = Label(view, text="Age", bg='white', relief=RAISED, bd=2, font=('ariel', 18))
        new_age.place(x=550, y=250)
        new_gender = Label(view, text="Gender", bg='white', relief=RAISED, bd=2, font=('ariel', 18))
        new_gender.place(x=550, y=300)
        new_num = Label(view, text="Phone Number", bg='white', bd=2, relief=RAISED, font=('ariel', 18))
        new_num.place(x=550, y=350)
        new_app = Label(view, text="Appointment Time", bg='white', bd=2, relief=RAISED, font=('ariel', 18))
        new_app.place(x=550, y=400)

        iname = name_e.get()
        ilast = last_e.get()
        # iage = num_e.get()
        cur.execute('create database if not exists project')
        cur.execute(
            'create table if not exists project.hospital(name varchar(255), last varchar(255), age varchar(255), gender varchar(255), phone varchar(255), appt varchar(255))')
        cur.execute("select name from project.hospital where name=%s and last=%s ", (iname, ilast))
        dname = cur.fetchone()
        cur.execute("select last from project.hospital where name=%s and last=%s ", (iname, ilast))
        dlast = cur.fetchone()
        cur.execute('select age from project.hospital where name=%s and last=%s ', (iname, ilast))
        dage = cur.fetchone()
        cur.execute('select gender from project.hospital where name=%s and last=%s', (iname, ilast))
        dgender = cur.fetchone()
        cur.execute('select phone from project.hospital where name=%s and last=%s ', (iname, ilast))
        dphone = cur.fetchone()
        cur.execute('select appt from project.hospital where name=%s and last=%s', (iname, ilast))
        dappt = cur.fetchone()

        # ------------------Labels---------------------------
        name = Label(view, text=dname, bd=5, bg='white', font=('ariel', 15))
        name.place(x=620, y=200)
        last = Label(view, text=dlast, bd=5, bg='white', font=('ariel', 15))
        last.place(x=910, y=200)
        age = Label(view, text=dage, bd=5, bg='white', font=('ariel', 15))
        age.place(x=780, y=250)
        gender = Label(view, text=dgender, bd=5, bg='white', font=('ariel', 15))
        gender.place(x=780, y=300)
        num = Label(view, bd=5, text=dphone, bg='white', font=('ariel', 15))
        num.place(x=780, y=350)
        appt = Label(view, bd=5, text=dappt, bg='white', font=('ariel', 15))
        appt.place(x=780, y=400)

        Button(view, text='Back', relief=RAISED, bg='white', font=('ariel', 20), command=view.destroy).place(x=680,
                                                                                                             y=500)

        view.mainloop()

    # ------------------Button---------------------------
    Button(view_r, text='Back', relief=RAISED, bg='white', font=('ariel', 20), command=view_r.destroy).place(x=600,
                                                                                                             y=300)
    Button(view_r, text='Submit', relief=RAISED, bg='white', font=('ariel', 20), command=submit).place(x=800, y=300)
    view_r.mainloop()
