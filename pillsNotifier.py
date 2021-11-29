from tkinter import *
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk
import time

t = Tk()
t.title('Notifier')
t.geometry("500x500")
img = Image.open("pill_title_img.jpg")
tkimage = ImageTk.PhotoImage(img)

# get details
def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_color = color.get()
    get_time = time1.get()
    # print(get_title,get_msg, tt)

    if get_title == "" or get_msg == "" or get_color == "" or get_time == "":
        messagebox.showerror("Alert", "All fields are required!")
    else:
        int_time = int(float(get_time))
        hr_to_sec = int_time * 60 * 60
        messagebox.showinfo("notifier set", "set notification ?")
        t.destroy()
        time.sleep(hr_to_sec)

        notification.notify("Pill Name: {title}".format(title=get_title),
                            message="take a pill : {ptake} \n pill Color : {pcolor}".format(ptake=get_msg, pcolor=get_color),
                            app_name="pillsNotifier",
                            app_icon="pills.ico",
                            toast=True,
                            timeout=30)

img_label = Label(t, image=tkimage).grid()

# Label - Title
t_label = Label(t, text="Pill Name",font=("poppins", 10))
t_label.place(x=12, y=70)

# ENTRY - Title
title = Entry(t, width="25",font=("poppins", 13))
title.place(x=123, y=70)

# Label - Message
m_label = Label(t, text="taken half or full", font=("poppins", 10))
m_label.place(x=12, y=120)

# ENTRY - Message
msg = Entry(t, width="40", font=("poppins", 13))
msg.place(x=123,height=30, y=120)

# Label - color
m_label = Label(t, text="Color of pill", font=("poppins", 10))
m_label.place(x=12, y=175)

# ENTRY - color
color = Entry(t, width="40", font=("poppins", 13))
color.place(x=123,height=30, y=175)

# Label - Time
time_label = Label(t, text="Set Time", font=("poppins", 10))
time_label.place(x=12, y=230)

# ENTRY - Time
time1 = Entry(t, width="5", font=("poppins", 13))
time1.place(x=123, y=230)

# Label - min
time_min_label = Label(t, text="hr", font=("poppins", 10))
time_min_label.place(x=175, y=230)

# Button
but = Button(t, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
             relief="raised",
             command=get_details)
but.place(x=170, y=280)

t.resizable(0,0)
t.mainloop()
