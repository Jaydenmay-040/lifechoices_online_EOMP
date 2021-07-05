from tkinter import *
from tkinter import messagebox
import pymysql

class Login:
    def __init__(self, window):
        self.window = window
        self.window.title("Life Choices Online")
        self.window.geometry("1366x700")
        self.window.resizable(False, False)
        self.loginform()


    def loginform(self):
        Frame_login = Frame(self.window, bg="white")
        Frame_login.place(x=0, y=0, height=700, width=1366)

        self.img = PhotoImage(file="./images/life-choices-logo.png")
        img = Label(Frame_login, image=self.img).place(x=0, y=0, width=1366, height=700)

        frame_input = Frame(self.window, bg='white')
        frame_input.place(x=320, y=130, height=450, width=350)

        label1 = Label(frame_input, text="Login Here", font=('Arial', 32, 'bold'), fg='black', bg='white')
        label1.place(x=75, y=20)

        label2 = Label(frame_input, text='Username', font=('Arial', 20, 'bold'), fg='black', bg='white')
        label2.place(x=30, y=95)
        self.email_txt = Entry(frame_input, font=("time new roman", 15, 'bold'), bg='lightgray')
        self.email_txt.place(x=30, y=145, width=270, height=35)

        label3 = Label(frame_input, text="Password", font=("Arial", 20, 'bold'), fg="black", bg='white')
        label3.place(x=30, y=195)
        self.password = Entry(frame_input, font=("Arial", 15, 'bold'), bg='lightgray')
        self.password.place(x=30, y=245, width=270, height=35)

        btn1 = Button(frame_input, text="forgot password?", cursor='hand2', font=('calibri', 10), fg='black', bg='white', bd=0)
        btn1.place(x=125, y=305)

        btn2 = Button(frame_input, text="Login", command=self.login, cursor="hand2", font=("Arial", 15), fg='black', bg='white', bd=0, width=15, height=1)
        btn2.place(x=90, y=340)

        btn3 = Button

