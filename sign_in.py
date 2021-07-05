from tkinter import *
from tkinter import messagebox, simpledialog
import mysql.connector
import datetime
import tkinter as tk

window = Tk()
window. geometry("500x350")
window.title("LifeChoices Online")
window.config(bg="lightgreen")

#  Title
title_lbl = Label(window, text="Login", font=("Arial", 25, 'bold')).place(x=200, y=10)

# Defining labels
usernme_lbl = Label(window, text='Please enter username', bg="lightgreen", fg='Black')
usernme_lbl.place(x=80, y=120)
usernme_ent = Entry(window)
usernme_ent.place(x=260, y=120)
passwrd_lbl = Label(window, text='Please enter password', bg="lightgreen", fg='Black')
passwrd_lbl.place(x=80, y=170)
passwrd_ent = Entry(window, show='*')
passwrd_ent.place(x=260, y=170)

# Buttons
login_btn = Button(window, text="Login", width=10, command='#', bg="black", fg='white')
login_btn.place(x=100, y=280)
register_btn = Button(window, text="Register", width=10, command='#', bg="black", fg='white')
register_btn.place(x=280, y=280)
exit_button = Button(window, text="Exit", width=7, command=exit)
exit_button.place(x=10, y=15)

window.mainloop()
