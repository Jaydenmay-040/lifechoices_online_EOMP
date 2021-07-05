from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import messagebox, simpledialog
import tkinter.messagebox as tkMessageBox
from datetime import datetime

window = Tk()
window. geometry("500x370")
window.title("LifeChoices Online")

#  Title
title_lbl = Label(window, text="Login", font=("Arial", 25, 'bold')).place(x=200, y=10)

# Defining labels
first_nme_lbl = Label(window, text='First Name', bg="lightgreen", fg='Black')
first_nme_lbl.place(x=100, y=80)
first_nme_ent = Entry(window)
first_nme_ent.place(x=240, y=80)
last_nme_lbl = Label(window, text='Last Name', bg="lightgreen", fg='Black')
last_nme_lbl.place(x=100, y=110)
last_nme_ent = Entry(window)
last_nme_ent.place(x=240, y=110)
ID_no_lbl = Label(window, text='ID Number', bg="lightgreen", fg='Black')
ID_no_lbl.place(x=100, y=140)
ID_no_ent = Entry(window)
ID_no_ent.place(x=240, y=140)
phn_no_lbl = Label(window, text='Phone Number', bg="lightgreen", fg='Black')
phn_no_lbl.place(x=100, y=170)
phn_no_ent = Entry(window)
phn_no_ent.place(x=240, y=170)

# Next of Kin Details Label
nxt_kin_lbl = Label(window, text='Next of Kin Details', bg='lightgreen', fg='Black', font=("Arial", 13))
nxt_kin_lbl.place(x=180, y=210)

nxt_first_nme_ent = Entry(window, width=18)
nxt_first_nme_ent.place(x=80, y=245)
nxt_first_nme_lbl = Label(window, text='First Name', bg="lightgreen", fg='Black')
nxt_first_nme_lbl.place(x=80, y=275)
nxt_phn_no_ent = Entry(window, width=18)
nxt_phn_no_ent.place(x=250, y=245)
nxt_phn_no_lbl = Label(window, text='Phone Number', bg="lightgreen", fg='Black')
nxt_phn_no_lbl.place(x=250, y=275)


# Buttons
submit_btn = Button(window, text="Submit", width=10, command='#', bg="#8dc63f", fg='white')
submit_btn.place(x=100, y=320)
clear_btn = Button(window, text="Clear", width=10, command='#', bg="#8dc63f", fg='white')
clear_btn.place(x=280, y=320)
exit_btn = Button(window, text="Exit", width=7, command=exit)
exit_btn.place(x=10, y=15)

window.mainloop()
