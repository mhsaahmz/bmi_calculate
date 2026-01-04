from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry('300x300')
win.config(bg="#c2b2e5")

# function
def bmi_calculate():
    try:
        height = float(ent_height.get()) / 100
        weight = float(ent_weight.get())
    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numbers')
        return

    if height <= 0 or weight <= 0:
        messagebox.showerror('Error', 'Values must be greater than zero!')
        return

    bmi = weight / (height ** 2)
    messagebox.showinfo('BMI', f'Your BMI is : {bmi:.2f}')

    ent_height.delete(0, END)
    ent_weight.delete(0, END)
    ent_height.focus_set()

# widget
lbl_height = Label(win,text='Height:',font='arial 16')
lbl_height.place(x=20,y=100)

lbl_weight = Label(win,text='Weight:',font='arial 16')
lbl_weight.place(x=20,y=160)

ent_height = Entry(win,font='arial 16',width=12)
ent_height.place(x=130,y=103)

ent_weight = Entry(win,font='arial 16',width=12)
ent_weight.place(x=130,y=163)

lbl_welcome = Label(win,text='Welcome to BMI calculate',font='arial 17 bold')
lbl_welcome.place(x=7,y=20)

btn_run = Button(win,text='Run',font='arial 18',fg='red',width=10,command=bmi_calculate)
btn_run.place(x=80,y=240)

win.mainloop()