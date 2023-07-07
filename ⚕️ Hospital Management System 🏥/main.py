from tkinter import *

from PIL import ImageTk, Image

import NewRegistration as new_r
import ViewRegistration as view_r

# ---------------------Main Window--------------------
window1 = Tk()
window1.title('Welcome')
window1.geometry("{0}x{1}+0+0".format(window1.winfo_screenwidth(), window1.winfo_screenheight()))
window1.config()
path1 = r'1.jpg'
image1 = ImageTk.PhotoImage(Image.open(path1))
image1_label = Label(window1, image=image1, height=850, width=1550)
image1_label.image = image1
image1_label.place(x=0, y=0)
welcome_label = Label(window1, text='ALPHA HOSPITAL', bd=6, fg='black', bg='light pink', relief=RAISED,font=('ariel', 50, 'bold'))
welcome_label.place(x=550, y=20)
Label(window1, text='"where every life counts...."', bd=6, bg='sky blue', font=('ariel', 20, 'italic')).place(x=700,y=120)

# --------------BUTTONS-------------------------------
register = Button(window1, text='New Appointment', fg='black', bg='light green', font=('ariel', 20, 'bold'),command=new_r.Newregist)
register.place(x=700, y=300)

view = Button(window1, text='View Appointment', fg='black', bg='light green', font=('ariel', 20, 'bold'),command=view_r.Viewregist)
view.place(x=700, y=400)

close = Button(window1, text='Close', bg='red', font=('ariel', 20), command=window1.destroy)
close.place(x=760, y=500)

window1.mainloop()
