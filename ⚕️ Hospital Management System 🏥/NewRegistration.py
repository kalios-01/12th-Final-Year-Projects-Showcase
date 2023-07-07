from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql

mydb = pymysql.connect(user='root', password='1234')
cur = mydb.cursor()


def Newregist():
    new_r = Toplevel()
    new_r.title('Registration Page')
    new_r.geometry('2000x1550')
    new_r.config(bg='sky blue')
    path1 = r'2.jpg'
    image1 = ImageTk.PhotoImage(Image.open(path1))
    image1_label = Label(new_r, image=image1, height=1000, width=1500)
    image1_label.image = image1
    image1_label.place(x=0, y=0)
    new_label = Label(new_r, text='NEW REGISTRATION', fg='white', bg='black', bd=6, relief=RAISED, font=('ariel', 30))
    new_label.place(x=570, y=20)

    # ------------------Labels---------------------------
    new_name = Label(new_r, text="First Name", bd=5, bg='white', font=('ariel', 18))
    new_name.place(x=480, y=200)
    new_last = Label(new_r, text="Last Name", bd=5, bg='white', font=('ariel', 18))
    new_last.place(x=770, y=200)
    new_age = Label(new_r, text="Age", bg='white', bd=5, font=('ariel', 18))
    new_age.place(x=560, y=250)
    new_gender = Label(new_r, text="Gender", bg='white', bd=5, font=('ariel', 18))
    new_gender.place(x=550, y=300)
    new_num = Label(new_r, text="Phone Number", bg='white', bd=5, font=('ariel', 18))
    new_num.place(x=550, y=350)
    new_app = Label(new_r, text="Appointment Time", bg='white', bd=5, font=('ariel', 18))
    new_app.place(x=550, y=400)

    # ------------------Entry---------------------------
    name_e = Entry(new_r, width=20, bd=6)
    name_e.place(x=620, y=200)
    last_e = Entry(new_r, width=20, bd=6)
    last_e.place(x=910, y=200)
    age_e = Entry(new_r, width=40, bd=6)
    age_e.place(x=750, y=250)
    v = StringVar()
    gender_e = Radiobutton(new_r, text='Male', variable=v, relief=RAISED, value='Male', font=('ariel', 12))
    gender_e.place(x=750, y=300)
    gender_e = Radiobutton(new_r, text='Female', variable=v, relief=RAISED, value='Female', font=('ariel', 12))
    gender_e.place(x=840, y=300)
    gender_e = Radiobutton(new_r, text='Other', variable=v, relief=RAISED, value='Other', font=('ariel', 12))
    gender_e.place(x=940, y=300)
    num_e = Entry(new_r, width=40, bd=6)
    num_e.place(x=750, y=350)
    time = StringVar()
    choices = list(range(1, 13))
    time.set('Hour')
    hour = OptionMenu(new_r, time, *choices)
    hour.place(x=780, y=400)
    minutes = StringVar()
    choices1 = list(range(1, 61))
    minutes.set('Minutes')
    minute = OptionMenu(new_r, minutes, *choices1)
    minute.place(x=850, y=400)
    ampm = StringVar()
    choices2 = {'AM', 'PM'}
    ampm.set('AM/PM')
    am_pm = OptionMenu(new_r, ampm, *choices2)
    am_pm.place(x=935, y=400)

    def insert():
        name = name_e.get()
        last = last_e.get()
        age = age_e.get()
        gender = v.get()
        phone = num_e.get()
        hours = time.get()
        minutex = minutes.get()
        amopm = ampm.get()
        timex = hours + ':' + minutex + amopm
        mydb = pymysql.connect(user='root', password='1234')
        cur = mydb.cursor()
        cur.execute('create database if not exists project')
        cur.execute(
            'create table if not exists project.hospital(name varchar(255), last varchar(255), age varchar(255), gender varchar(255), phone varchar(255), appt varchar(255))')
        cur.execute('insert into project.hospital(name, last, age, gender, phone, appt) values(%s, %s, %s, %s, %s, %s)',
                    (name, last, age, gender, phone, timex))

        mydb.commit()
        messagebox.showinfo(title='Registration Complete', message='Appointment Successfully Placed')
        new_r.destroy()

    # ------------------Buttons------------------
    Button(new_r, text='Back', relief=RAISED, bg='white', font=('ariel', 20), command=new_r.destroy).place(x=600, y=600)
    Button(new_r, text='Submit', relief=RAISED, bg='white', font=('ariel', 20), command=insert).place(x=800, y=600)

    new_r.mainloop()
