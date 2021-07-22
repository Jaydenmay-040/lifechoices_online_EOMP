import datetime

import rsaidnumber
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import pymysql
import tkinter as tk
from tkinter import ttk
import random
import datetime as dt
from validate_email import validate_email
import smtplib


class Login:
    def __init__(self, window):
        self.window = window
        self.window.title("Life Choices Online")
        self.window.geometry("1366x800")
        self.window.resizable(False, False)
        self.window.bind('<Control-a>', lambda z: self.Admin())
        self.Login()

    def Login(self):
        Frame_login = Frame(self.window, bg="#d9d9d9")
        Frame_login.place(x=0, y=0, height=700, width=1366)

        self.img = PhotoImage(file="./images/life-choices-logo.png")
        img = Label(Frame_login, image=self.img).place(x=150, y=0, width=440, height=100)

        self.img2 = PhotoImage(file="./images/life-choices-logo.png")
        img2 = Label(Frame_login, image=self.img2).place(x=400, y=300, width=440, height=100)

        self.img3 = PhotoImage(file="./images/life-choices-logo.png")
        img3 = Label(Frame_login, image=self.img3).place(x=800, y=100, width=440, height=100)

        self.img4 = PhotoImage(file="./images/life-choices-logo.png")
        img4 = Label(Frame_login, image=self.img4).place(x=650, y=550, width=440, height=100)

        self.img5 = PhotoImage(file="./images/life-choices-logo.png")
        img5 = Label(Frame_login, image=self.img5).place(x=1130, y=350, width=440, height=100)

        self.img6 = PhotoImage(file="./images/life-choices-logo.png")
        img6 = Label(Frame_login, image=self.img6).place(x=-235, y=350, width=440, height=100)

        login_frame = Frame(self.window, bg='white')
        login_frame.place(x=320, y=130, height=450, width=350)

        label1 = Label(login_frame, text="Login Here", font=('Arial', 32, 'bold'), fg='black', bg='white')
        label1.place(x=75, y=20)

        label2 = Label(login_frame, text='Username', font=('Arial', 20, 'bold'), fg='black', bg='white')
        label2.place(x=30, y=95)
        self.user_name = Entry(login_frame, font=("time new roman", 15, 'bold'), bg='lightgray')
        self.user_name.place(x=30, y=145, width=270, height=35)

        label3 = Label(login_frame, text="Password", font=("Arial", 20, 'bold'), fg="black", bg='white')
        label3.place(x=30, y=195)
        self.password = Entry(login_frame, font=("Arial", 15, 'bold'), bg='lightgray', show="*")
        self.password.place(x=30, y=245, width=270, height=35)

        btn1 = Button(login_frame, text="forgot password?", command=self.registration, cursor='hand2', font=('calibri', 10), fg='black', bg='white', bd=0)
        btn1.place(x=125, y=305)

        btn2 = Button(login_frame, text="Login", command=self.login, cursor="hand2", font=("Arial", 15), fg='black', bg='#8dc63f', bd=0, width=15, height=1)
        btn2.place(x=90, y=340)

        btn3 = Button(login_frame, command=self.Register, text="Not Registered?register", cursor="hand2", font=('Arial', 10), bg='white', fg='black', bd=0)
        btn3.place(x=1, y=390)

    def login(self):
        if self.user_name.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "Ensure that all field filled in", parent=self.window)
        else:
            # try:
                con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LifeChoices_Online')
                cur = con.cursor()
                cur.execute('select * from Login where username=%s and password=%s', (self.user_name.get(), self.password.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Username And Password", parent=self.window)
                else:
                    self.appscreen()
                    con.close()
                    date = f"{dt.datetime.now():%a, %b %d %Y %H:%M:%S}"
                    with open("User_Code.txt", 'a') as file:
                        file.write('Username: ' + str(self.user_name.get()) + '\n')
                        file.write('LogIn Date and Time: ' + date + '\n')
            # except Exception as es:
            #     messagebox.showerror('Error', 'Error Something Went Wrong', parent=self.window)

    def registration(self):
        Registration_login = Frame(self.window, bg="#d9d9d9")
        Registration_login.place(x=0, y=0, height=700, width=1366)

        self.img = PhotoImage(file="./images/life-choices-logo.png")
        img = Label(Registration_login, image=self.img).place(x=150, y=0, width=440, height=100)

        self.img2 = PhotoImage(file="./images/life-choices-logo.png")
        img2 = Label(Registration_login, image=self.img2).place(x=400, y=300, width=440, height=100)

        self.img3 = PhotoImage(file="./images/life-choices-logo.png")
        img3 = Label(Registration_login, image=self.img3).place(x=800, y=100, width=440, height=100)

        self.img4 = PhotoImage(file="./images/life-choices-logo.png")
        img4 = Label(Registration_login, image=self.img4).place(x=650, y=550, width=440, height=100)

        self.img5 = PhotoImage(file="./images/life-choices-logo.png")
        img5 = Label(Registration_login, image=self.img5).place(x=1130, y=350, width=440, height=100)

        self.img6 = PhotoImage(file="./images/life-choices-logo.png")
        img6 = Label(Registration_login, image=self.img6).place(x=-235, y=350, width=440, height=100)

        registration_frame = Frame(self.window, bg='white')
        registration_frame.place(x=320, y=130, height=450, width=400)

        label1 = Label(registration_frame, text="Security Details", font=('Arial', 32, 'bold'), fg='black', bg='white')
        label1.place(x=35, y=20)

        Username_lbl = Label(registration_frame, text='Username', font=('Arial', 20, 'bold'), fg='black', bg='white')
        Username_lbl.place(x=30, y=95)
        self.Username_ent = Entry(registration_frame, font=("time new roman", 15, 'bold'), bg='lightgray')
        self.Username_ent.place(x=30, y=145, width=270, height=35)

        Email_lbl = Label(registration_frame, text="Email", font=("Arial", 20, 'bold'), fg="black", bg='white')
        Email_lbl.place(x=30, y=195)
        self.Email_ent = Entry(registration_frame, font=("Arial", 15, 'bold'), bg='lightgray', fg="black")
        self.Email_ent.place(x=30, y=245, width=270, height=35)

        btn2 = Button(registration_frame, text="Confirm", command=self.confirm, cursor="hand2",
                      font=("Arial", 15), fg='black',
                      bg='#8dc63f', bd=0, width=15, height=1)
        btn2.place(x=90, y=340)
        btn3 = Button(registration_frame, command=self.Login, text="Already Registered?login", cursor="hand2",
                      font=('Arial', 10), bg='white', fg='black', bd=0)
        btn3.place(x=1, y=390)

    def confirm(self):
        if self.Email_ent.get() == "" or self.Username_ent.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.window)
        con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LifeChoices_Online')
        cur = con.cursor()
        cur.execute("select * from Login where username=%s", self.Username_ent.get())
        row = cur.fetchone()
        if row!=None:
            self.forgotPassword()
            self.list = []
            self.num = sorted(random.sample(range(1, 21), 4))
            print(self.num)
        else:
            messagebox.showerror("Error", "Username doesn't Exist, Please try with another Username", parent=self.window)

    def forgotPassword(self):
        forgot_login = Frame(self.window, bg="#d9d9d9")
        forgot_login.place(x=0, y=0, height=700, width=1366)

        self.img = PhotoImage(file="./images/life-choices-logo.png")
        img = Label(forgot_login, image=self.img).place(x=150, y=0, width=440, height=100)

        self.img2 = PhotoImage(file="./images/life-choices-logo.png")
        img2 = Label(forgot_login, image=self.img2).place(x=400, y=300, width=440, height=100)

        self.img3 = PhotoImage(file="./images/life-choices-logo.png")
        img3 = Label(forgot_login, image=self.img3).place(x=800, y=100, width=440, height=100)

        self.img4 = PhotoImage(file="./images/life-choices-logo.png")
        img4 = Label(forgot_login, image=self.img4).place(x=650, y=550, width=440, height=100)

        self.img5 = PhotoImage(file="./images/life-choices-logo.png")
        img5 = Label(forgot_login, image=self.img5).place(x=1130, y=350, width=440, height=100)

        self.img6 = PhotoImage(file="./images/life-choices-logo.png")
        img6 = Label(forgot_login, image=self.img6).place(x=-235, y=350, width=440, height=100)

        forgot_frame = Frame(self.window, bg='white')
        forgot_frame.place(x=320, y=130, height=450, width=400)

        label1 = Label(forgot_frame, text="Security Details", font=('Arial', 32, 'bold'), fg='black', bg='white')
        label1.place(x=35, y=20)

        label2 = Label(forgot_frame, text='Enter your four-digit-code', font=('Arial', 20, 'bold'), fg='black',
                       bg='white')
        label2.place(x=30, y=100)
        self.first_entry = Entry(forgot_frame, font=('Arial', 15, 'bold'), bg='lightgray')
        self.first_entry.place(x=80, y=190, width=40)
        self.second_entry = Entry(forgot_frame, font=('Arial', 15, 'bold'), bg='lightgray')
        self.second_entry.place(x=140, y=190, width=40)
        self.third_entry = Entry(forgot_frame, font=('Arial', 15, 'bold'), bg='lightgray')
        self.third_entry.place(x=200, y=190, width=40)
        self.fourth_entry = Entry(forgot_frame, font=('Arial', 15, 'bold'), bg='lightgray')
        self.fourth_entry.place(x=260, y=190, width=40)

        btn1 = Button(forgot_frame, text="Didn't receive code?", command=self.reload, cursor='hand2', font=('calibri', 10), fg='black', bg='white', bd=0)
        btn1.place(x=125, y=305)
        btn2 = Button(forgot_frame, text="Confirm", command=self.notRegistered, cursor="hand2",
                      font=("Arial", 15), fg='black',
                      bg='#8dc63f', bd=0, width=15, height=1)
        btn2.place(x=90, y=340)
        btn3 = Button(forgot_frame, command=self.Login, text="Already Registered?login", cursor="hand2",
                      font=('Arial', 10), bg='white', fg='black', bd=0)
        btn3.place(x=1, y=390)

    def reload(self):
        self.list = []
        self.num = sorted(random.sample(range(1, 21), 4))
        print(self.num)

    def notRegistered(self):
        self.list = [int(self.first_entry.get()), int(self.second_entry.get()), int(self.third_entry.get()), int(self.fourth_entry.get())]
        if self.list != self.num:
            messagebox.showerror("Error", "Ensure that your four-digit-code is entered correctly")
        else:
            self.update_user()

    def update_user(self):
        Update_login = Frame(self.window, bg="#d9d9d9")
        Update_login.place(x=0, y=0, height=700, width=1366)

        self.img = PhotoImage(file="./images/life-choices-logo.png")
        img = Label(Update_login, image=self.img).place(x=150, y=0, width=440, height=100)

        self.img2 = PhotoImage(file="./images/life-choices-logo.png")
        img2 = Label(Update_login, image=self.img2).place(x=400, y=300, width=440, height=100)

        self.img3 = PhotoImage(file="./images/life-choices-logo.png")
        img3 = Label(Update_login, image=self.img3).place(x=800, y=100, width=440, height=100)

        self.img4 = PhotoImage(file="./images/life-choices-logo.png")
        img4 = Label(Update_login, image=self.img4).place(x=650, y=550, width=440, height=100)

        self.img5 = PhotoImage(file="./images/life-choices-logo.png")
        img5 = Label(Update_login, image=self.img5).place(x=1130, y=350, width=440, height=100)

        self.img6 = PhotoImage(file="./images/life-choices-logo.png")
        img6 = Label(Update_login, image=self.img6).place(x=-235, y=350, width=440, height=100)

        update_frame = Frame(self.window, bg='white')
        update_frame.place(x=320, y=130, height=450, width=400)

        label1 = Label(update_frame, text="Security Details", font=('Arial', 32, 'bold'), fg='black', bg='white')
        label1.place(x=35, y=20)

        label2 = Label(update_frame, text='Password', font=('Arial', 20, 'bold'), fg='black', bg='white')
        label2.place(x=30, y=95)
        self.Password_ent = Entry(update_frame, font=("Arial", 15, 'bold'), bg='lightgray', show="*")
        self.Password_ent.place(x=30, y=145, width=270, height=35)

        label3 = Label(update_frame, text="Confirm Password", font=("Arial", 20, 'bold'), fg="black", bg='white')
        label3.place(x=30, y=195)
        self.ConfirmPass_ent = Entry(update_frame, font=("Arial", 15, 'bold'), bg='lightgray', show="*")
        self.ConfirmPass_ent.place(x=30, y=245, width=270, height=35)

        btn1 = Button(update_frame, text="Cancel?", command=self.Login, cursor='hand2', font=('calibri', 10), fg='black', bg='white', bd=0)
        btn1.place(x=125, y=305)

        btn2 = Button(update_frame, text="Confirm", command=self.Update_User, cursor="hand2", font=("Arial", 15), fg='black', bg='#8dc63f', bd=0, width=15, height=1)
        btn2.place(x=90, y=340)

    def Update_User(self):
        Pass = self.Password_ent.get()
        confirmPass = self.ConfirmPass_ent.get()
        Username = self.Username_ent.get()
        if messagebox.askyesno("confirm Please?", "Are you sure you want to update?"):
            con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LifeChoices_Online')
            cur = con.cursor()
            query = "UPDATE Login SET password=%s, confirmpassword=%s WHERE username=%s"
            cur.execute(query, (Pass, confirmPass, Username))
            con.commit()
            con.close()
            self.Login()
        else:
            return True


    def Register(self):

        Frame_login = Frame(self.window, bg='white')
        Frame_login.place(x=0, y=0, height=700, width=1366)

        self.img = PhotoImage(file="./images/life-choices-logo.png")
        img = Label(Frame_login, image=self.img).place(x=0, y=0, width=1366, height=700)

        register_frame = Frame(self.window, bg='white')
        register_frame.place(x=320, y=100, height=520, width=630)

        label1 = Label(register_frame, text="Register Here", font=('Arial', 20, 'bold'), fg='black', bg='white')
        label1.place(x=45, y=20)

        label2 = Label(register_frame, text='First Name', font=('Arial', 20, "bold"), bg='white')
        label2.place(x=30, y=95)
        self.name_entry = Entry(register_frame, font=('Arial', 15, 'bold'), bg='lightgray')
        self.name_entry.place(x=30, y=145, width=270, height=35)

        label3 = Label(register_frame, text="ID Number", font=('Arial', 20, 'bold'), fg='black', bg='white')
        label3.place(x=30, y=195)
        self.ID_entry2 = Entry(register_frame, font=('Arial', 15, 'bold'), bg='lightgray')
        self.ID_entry2.place(x=30, y=245, width=270, height=35)

        label4 = Label(register_frame, text="Last Name", font=("Arial", 20, "bold"), fg='black', bg='white')
        label4.place(x=330, y=95)
        self.last_entry3 = Entry(register_frame, font=('Arial', 15, 'bold'), bg='lightgray')
        self.last_entry3.place(x=330, y=145, width=270, height=35)

        label5 = Label(register_frame, text='Phone Number', font=('Arial', 20, 'bold'), fg='black', bg='white')
        label5.place(x=330, y=195)
        self.number_entry4 = Entry(register_frame, font=('Arial', 15, 'bold'), bg='lightgray')
        self.number_entry4.place(x=330, y=245, width=270, height=35)

        nxt_label = Label(register_frame, text="Next of Kin Details", font=('Arial', 20, 'bold'), fg='black', bg='white')
        nxt_label.place(x=180, y=295)

        label6 = Label(register_frame, text="Name", font=("Arial", 20, "bold"), fg='black', bg='white')
        label6.place(x=30, y=350)
        self.nxt_entry5 = Entry(register_frame, font=('Arial', 15, 'bold'), bg='lightgray')
        self.nxt_entry5.place(x=30, y=400, width=270, height=35)

        label7 = Label(register_frame, text='Next Phone Number', font=('Arial', 20, 'bold'), fg='black', bg='white')
        label7.place(x=330, y=350)
        self.nxt_num_entry6 = Entry(register_frame, font=('Arial', 15, 'bold'), bg='lightgray')
        self.nxt_num_entry6.place(x=330, y=400, width=270, height=35)

        btn = Button(register_frame, command=self.nxtRegister, text="Next", cursor="hand2", font=('Arial', 15),
                      fg='black', bg='#8dc63f', bd=0, width=15, height=1)
        btn.place(x=90, y=470)

    def nxtRegister(self):
        Frame_login1 = Frame(self.window, bg='white')
        Frame_login1.place(x=0, y=0, height=700, width=1366)

        self.img = PhotoImage(file="./images/life-choices-logo.png")
        img = Label(Frame_login1, image=self.img).place(x=0, y=0, width=1366, height=700)

        frame_input2 = Frame(self.window, bg='white')
        frame_input2.place(x=320, y=130, height=450, width=630)

        label1 = Label(frame_input2, text="Register Here", font=('Arial', 20, 'bold'), fg='black', bg='white')
        label1.place(x=45, y=20)

        label2 = Label(frame_input2, text='Username', font=('Arial', 20, "bold"), bg='white')
        label2.place(x=30, y=95)
        self.entry = Entry(frame_input2, font=('Arial', 15, 'bold'), bg='lightgray')
        self.entry.place(x=30, y=145, width=270, height=35)

        label3 = Label(frame_input2, text="Password", font=('Arial', 20, 'bold'), fg='black', bg='white')
        label3.place(x=30, y=195)
        self.entry2 = Entry(frame_input2, font=('Arial', 15, 'bold'), bg='lightgray', show="*")
        self.entry2.place(x=30, y=245, width=270, height=35)

        label4 = Label(frame_input2, text="Email", font=("Arial", 20, "bold"), fg='black', bg='white')
        label4.place(x=330, y=95)
        self.email_entry3 = Entry(frame_input2, font=('Arial', 15, 'bold'), bg='lightgray')
        self.email_entry3.place(x=330, y=145, width=270, height=35)

        label5 = Label(frame_input2, text='Confirm Password', font=('Arial', 20, 'bold'), fg='black', bg='white')
        label5.place(x=330, y=195)
        self.entry4 = Entry(frame_input2, font=('Arial', 15, 'bold'), bg='lightgray', show="*")
        self.entry4.place(x=330, y=245, width=270, height=35)

        btn2 = Button(frame_input2, command=self.register, text="Register", cursor="hand2", font=('Arial', 15), fg='black', bg='#8dc63f', bd=0, width=15, height=1)
        btn2.place(x=90, y=340)

        btn3 = Button(frame_input2, command=self.Login, text="Already Registered?Login", cursor="hand2", font=('Arial', 10), bg='white', fg='black', bd=0)
        btn3.place(x=110, y=390)

        btn4 = Button(frame_input2, command=self.back, text="back", cursor="hand2", font=('Arial', 15),
                      fg='black', bg='#8dc63f', bd=0, width=13, height=1)
        btn4.place(x=350, y=340)

    def register(self):
        if self.entry.get() == "" or self.entry2.get() == "" or self.email_entry3.get() == "" or self.entry4.get() == "" or self.name_entry.get() == "" or self.ID_entry2.get() == "" or self.last_entry3.get() == "" or self.number_entry4.get() == "" or self.nxt_entry5.get() == "" or self.nxt_num_entry6.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.window)
        elif self.entry2.get()!=self.entry4.get():
            messagebox.showerror("Error", "Password and Confirm Password Should Be The Same", parent=self.window)
        con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LifeChoices_Online')
        cur = con.cursor()
        cur.execute("select * from Login where username=%s", self.entry.get())
        row = cur.fetchone()
        if row!=None:
            messagebox.showerror("Error", "Username already Exist, Please try with another Username", parent=self.window)
        else:
            # try:
                con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LifeChoices_Online')
                cur = con.cursor()
                cur.execute("insert into registration(name, surname, IDnumber, phoneNumber, nxtOfKinName, nxtOfKinNumber) values(%s, %s, %s, %s, %s, %s)", ( self.name_entry.get(), self.last_entry3.get(), self.ID_entry2.get(), self.number_entry4.get(), self.nxt_entry5.get(), self.nxt_num_entry6.get()))
                con.commit()
                cur1 = con.cursor()
                cur1.execute("insert into Login(username, email, password, confirmpassword) values(%s, %s, %s, %s)", (self.entry.get(), self.email_entry3.get(), self.entry2.get(), self.entry4.get()))
                con.commit()
                messagebox.showinfo("Success", "Register Successful", parent=self.window)
                self.Login()
                con.close()
            # except Exception as es:
            #     messagebox.showerror("Error", "Error Something Went Wrong", parent=self.window)

    def back(self):
        self.Register()

    def appscreen(self):
        Appscreen = Frame(self.window, bg="#d9d9d9")
        Appscreen.place(x=0, y=0, height=700, width=1366)

        self.img = PhotoImage(file="./images/life-choices-logo.png")
        img = Label(Appscreen, image=self.img).place(x=150, y=0, width=440, height=100)

        self.img2 = PhotoImage(file="./images/life-choices-logo.png")
        img2 = Label(Appscreen, image=self.img2).place(x=400, y=300, width=440, height=100)

        self.img3 = PhotoImage(file="./images/life-choices-logo.png")
        img3 = Label(Appscreen, image=self.img3).place(x=800, y=100, width=440, height=100)

        self.img4 = PhotoImage(file="./images/life-choices-logo.png")
        img4 = Label(Appscreen, image=self.img4).place(x=650, y=550, width=440, height=100)

        self.img5 = PhotoImage(file="./images/life-choices-logo.png")
        img5 = Label(Appscreen, image=self.img5).place(x=1130, y=350, width=440, height=100)

        self.img6 = PhotoImage(file="./images/life-choices-logo.png")
        img6 = Label(Appscreen, image=self.img6).place(x=-235, y=350, width=440, height=100)

        Appscreen_frame = Frame(self.window, bg='white')
        Appscreen_frame.place(x=320, y=100, height=520, width=630)

        label1 = Label(Appscreen_frame, text="Hi! Welcome To", font=('times new romain', 22, 'bold'), fg='black', bg='white')
        label1.place(x=200, y=40)
        label2 = Label(Appscreen_frame, text="Life Choices Online", font=('times new romain', 22, 'bold'), fg='black', bg='white')
        label2.place(x=170, y=75)

        lbl4 = Label(Appscreen_frame, text="Username:", font=('Arial', 20, 'bold'), fg='black', bg='white')
        lbl4.place(x=90, y=195)
        lbl5 = Label(Appscreen_frame, text=self.user_name.get(), font=('Arial', 20, 'bold'), fg='black', bg="white")
        lbl5.place(x=300, y=195)

        lbl2 = Label(Appscreen_frame, text='Login Time:', font=('Arial', 20, "bold"), bg='white', fg='black')
        lbl2.place(x=90, y=245)
        lbl3 = Label(Appscreen_frame, text=f"{dt.datetime.now():%a, %b %d %Y %H:%M:%S}", font=('Arial', 20, 'bold'), bg='white', fg='black')
        lbl3.place(x=300, y=245)
        btn2 = Button(Appscreen_frame, text="LOGOUT", command=self.logOut, cursor="hand2", font=('times new romain', 15), fg='black', bg='#8dc63f', bd=0, width=15, height=1)
        btn2.place(x=200, y=400)

    def Admin(self):
        Frame_Admin = Frame(self.window, bg='#d9d9d9')
        Frame_Admin.place(x=0, y=0, height=700, width=1366)

        self.img = PhotoImage(file="./images/life-choices-logo.png")
        img = Label(Frame_Admin, image=self.img).place(x=150, y=0, width=440, height=100)

        self.img2 = PhotoImage(file="./images/life-choices-logo.png")
        img2 = Label(Frame_Admin, image=self.img2).place(x=400, y=300, width=440, height=100)

        self.img3 = PhotoImage(file="./images/life-choices-logo.png")
        img3 = Label(Frame_Admin, image=self.img3).place(x=800, y=100, width=440, height=100)

        self.img4 = PhotoImage(file="./images/life-choices-logo.png")
        img4 = Label(Frame_Admin, image=self.img4).place(x=650, y=550, width=440, height=100)

        self.img5 = PhotoImage(file="./images/life-choices-logo.png")
        img5 = Label(Frame_Admin, image=self.img5).place(x=1130, y=350, width=440, height=100)

        self.img6 = PhotoImage(file="./images/life-choices-logo.png")
        img6 = Label(Frame_Admin, image=self.img6).place(x=-235, y=350, width=440, height=100)

        Admin_frame = Frame(self.window, bg='white')
        Admin_frame.place(x=320, y=130, height=450, width=350)

        label1 = Label(Admin_frame, text="Admin Login", font=('Arial', 32, 'bold'), fg='black', bg='white')
        label1.place(x=40, y=20)

        label2 = Label(Admin_frame, text='Username', font=('Arial', 20, 'bold'), fg='black', bg='white')
        label2.place(x=30, y=95)
        self.user_name = Entry(Admin_frame, font=("time new roman", 15, 'bold'), bg='lightgray')
        self.user_name.place(x=30, y=145, width=270, height=35)

        label3 = Label(Admin_frame, text="Password", font=("Arial", 20, 'bold'), fg="black", bg='white')
        label3.place(x=30, y=195)
        self.password = Entry(Admin_frame, font=("Arial", 15, 'bold'), bg='lightgray', show="*")
        self.password.place(x=30, y=245, width=270, height=35)

        btn2 = Button(Admin_frame, text="Login", command=self.admin, cursor="hand2", font=("Arial", 15), fg='black',
                      bg='#8dc63f', bd=0, width=15, height=1)
        btn2.place(x=90, y=340)

        btn3 = Button(Admin_frame, command=self.Login, text="Not Admin?login", cursor="hand2",
                      font=('Arial', 10), bg='white', fg='black', bd=0)
        btn3.place(x=1, y=390)

        # ADMIN USERNAME AND PASSWORD
        self.userName = "Admin"
        self.passWord = "Admin1234"

    # Admin login page, displays when clicking ctr+a
    def adminLogin(self):
        try:
            if self.user_name.get() == self.userName and (self.password.get()) == self.passWord:
                self.admin()
                return messagebox.showinfo("CONGRATULATIONS", "Click Ok to continue")
            elif (self.user_name.get()) == "" and (self.password.get()) == "":
                return messagebox.showerror("Error", "incorrect username and password")
            elif (self.user_name.get() != self.userName or self.password != self.passWord):
                messagebox.showerror("Error", "Please Enter a Valid Username and Password ")
        except IndexError:
            messagebox.showerror("Error", "Please Enter a Valid Username and Password ")

    # refreshes the admin page
    def refresh_details(self):
        self.admin()

    # logout function
    def logOut(self):
        if messagebox.askyesno("confirm Log Out?", "Are you sure you want to Log Out?"):
            self.Login()
            date = f"{dt.datetime.now():%a, %b %d %Y %H:%M:%S}"
            with open("User_Code.txt", 'a') as file:
                file.write('LogOut Date and Time: ' + date + '\n' + '\n')
        else:
            return True

    # Admin page
    def admin(self):
        Frame_admin = Frame(self.window, bg='#d9d9d9')
        Frame_admin.place(x=0, y=0, height=1500, width=1366)

        # Displays the images
        self.img = PhotoImage(file="./images/life-choices-logo.png")
        img = Label(Frame_admin, image=self.img).place(x=150, y=0, width=440, height=100)

        self.img2 = PhotoImage(file="./images/life-choices-logo.png")
        img2 = Label(Frame_admin, image=self.img2).place(x=400, y=300, width=440, height=100)

        self.img3 = PhotoImage(file="./images/life-choices-logo.png")
        img3 = Label(Frame_admin, image=self.img3).place(x=800, y=100, width=440, height=100)

        self.img4 = PhotoImage(file="./images/life-choices-logo.png")
        img4 = Label(Frame_admin, image=self.img4).place(x=650, y=550, width=440, height=100)

        self.img5 = PhotoImage(file="./images/life-choices-logo.png")
        img5 = Label(Frame_admin, image=self.img5).place(x=1130, y=350, width=440, height=100)

        self.img6 = PhotoImage(file="./images/life-choices-logo.png")
        img6 = Label(Frame_admin, image=self.img6).place(x=-235, y=350, width=440, height=100)

        admin_frame = Frame(self.window, bg='white')
        admin_frame.place(x=180, y=40, height=700, width=1000)


        def update(row):
            trv.delete(*trv.get_children())
            for i in row:
                trv.insert("", 'end', values=i)

        # This function gets the item that is searcher for
        def search():
            con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LifeChoices_Online')
            cur = con.cursor()
            q2 = q.get()
            cur.execute("select id, name, surname, IDnumber, phoneNumber, nxtOfKinName, nxtOfKinNumber from registration where name like '%"+q2+"%' or surname like '%"+q2 +"%' or IDnumber like '%"+q2+"%' or phoneNumber like '%"+q2 +"%' or nxtOfKinName like '%"+q2+"%' or nxtOfKinNumber like '%"+q2 +"%'")
            row = cur.fetchall()
            update(row)

        # This function clears the in info in the search bar
        def clear():
            con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LifeChoices_Online')
            cur = con.cursor()
            cur.execute("select id, name, surname, IDnumber, phoneNumber, nxtOfKinName, nxtOfKinNumber from registration")
            row = cur.fetchall()
            update(row)

        # This function allows admin to display the users details in the Data when double clicking on it in Details
        def getrow(event):
            rowid = trv.identify_row(event.y)
            item = trv.item(trv.focus())
            t1.set(item['values'][0])
            t2.set(item['values'][1])
            t3.set(item['values'][2])
            t4.set(item['values'][3])
            t5.set(item['values'][4])
            t6.set(item['values'][5])
            t7.set(item['values'][6])

        # Function that allows admin to make changes to the user
        def update_details():
            User_id = t1.get()
            name = t2.get()
            surname = t3.get()
            ID = t4.get()
            phone = t5.get()
            nxtName = t6.get()
            nxtNumber = t7.get()
            if messagebox.askyesno("confirm Please?", "Are you sure you want to update?"):
                con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LifeChoices_Online')
                cur = con.cursor()
                query = "UPDATE registration SET name=%s, surname=%s, IDnumber=%s, phoneNumber=%s, nxtOfKinName=%s, nxtOfKinNumber=%s WHERE id=%s"
                cur.execute(query, (name, surname, ID, phone, nxtName, nxtNumber, User_id))
                con.commit()
                con.close()
                clear()
            else:
                return True

        # Function that creates new user
        def add_new():
            name = t2.get()
            surname = t3.get()
            ID = t4.get()
            phone = t5.get()
            nxtName = t6.get()
            nxtNumber = t7.get()
            con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LifeChoices_Online')
            cur = con.cursor()
            cur.execute("insert into registration(name, surname, IDnumber, phoneNumber, nxtOfKinName, nxtOfKinNumber) values(%s, %s, %s, %s, %s, %s)", (name, surname, ID, phone, nxtName, nxtNumber))
            con.commit()
            con.close()

        # Delete function
        def delete_details():
            User_id = t1.get()
            if messagebox.askyesno("confirm Delete?", "Are you sure you want to delete this customer?"):
                con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LifeChoices_Online')
                cur = con.cursor()
                query = "DELETE FROM registration WHERE id=%s" %(User_id)
                cur.execute(query)
                con.commit()
                con.close()
                clear()
            else:
                return True

        q = StringVar()
        t1 = StringVar()
        t2 = StringVar()
        t3 = StringVar()
        t4 = StringVar()
        t5 = StringVar()
        t6 = StringVar()
        t7 = StringVar()

        # Creates The Frames For Details, Search and Data
        wrapper1 = LabelFrame(admin_frame, text="Details", bg='#8dc63f')
        wrapper2 = LabelFrame(admin_frame, text="Search")
        wrapper3 = LabelFrame(admin_frame, text="Data")

        wrapper1.place(x=25, y=10, width=950, height=200)
        wrapper2.place(x=25, y=225, width=950, height=150)
        wrapper3.place(x=25, y=390, width=950, height=300)

        # Displays The Headings In Details
        trv = ttk.Treeview(wrapper1, column=(1, 2, 3, 4, 5, 6, 7), show="headings", height="7")
        trv.pack(side=tk.LEFT)
        trv.place(x=0, y=0)
        trv.heading(1, text="User_id")
        trv.heading(2, text="Name")
        trv.heading(3, text="Surname")
        trv.heading(4, text="ID Number")
        trv.heading(5, text="Phone Number")
        trv.heading(6, text="Next Of Kin Name")
        trv.heading(7, text="Next Of Kin Number")
        trv.column(1, width=50, minwidth=100)
        trv.column(2, width=150, minwidth=200)
        trv.column(3, width=150, minwidth=200)
        trv.column(4, width=150, minwidth=200)
        trv.column(5, width=150, minwidth=200)
        trv.column(6, width=150, minwidth=200)
        trv.column(7, width=150, minwidth=200)


        trv.bind('<Double 1>', getrow)

        # Vertical Scrollbar
        yScrollBar = ttk.Scrollbar(wrapper1, orient="vertical", command=trv.yview)
        yScrollBar.place(x=930, y=0, height=160)

        # Horizontal Scrollbar
        xScrollBar = ttk.Scrollbar(wrapper1, orient="horizontal", command=trv.xview)
        xScrollBar.place(x=0, y=163, width=930)
        trv.configure(yscrollcommand=yScrollBar.set, xscrollcommand=xScrollBar.set)

        # Displaying the details in Details
        con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LifeChoices_Online')
        cur = con.cursor()
        cur.execute("select * from registration")
        row = cur.fetchall()
        update(row)

        # Search Labels and Entries
        lbl = Label(wrapper2, text="Seacrh")
        lbl.pack(side=tk.LEFT, padx=10)
        ent = Entry(wrapper2, textvariable=q)
        ent.pack(side=tk.LEFT, padx=6)
        btn = Button(wrapper2, text="Search", command=search, bg='#8dc63f')
        btn.pack(side=tk.LEFT, padx=6)
        clear_btn = Button(wrapper2, text="Clear", command=clear, bg='#8dc63f')
        clear_btn.pack(side=tk.LEFT, padx=6)

        # User Data Labels and Entries
        lbl1 = Label(wrapper3, text="User_id")
        lbl1.grid(row=0, column=0, padx=5, pady=3)
        self.ent1 = Entry(wrapper3, textvariable=t1)
        self.ent1.grid(row=0, column=1, padx=5, pady=3)

        lbl2 = Label(wrapper3, text="Name")
        lbl2.grid(row=1, column=0, padx=5, pady=3)
        ent2 = Entry(wrapper3, textvariable=t2)
        ent2.grid(row=1, column=1, padx=5, pady=3)

        lbl3 = Label(wrapper3, text="Surname")
        lbl3.grid(row=2, column=0, padx=5, pady=3)
        ent3 = Entry(wrapper3, textvariable=t3)
        ent3.grid(row=2, column=1, padx=5, pady=3)

        lbl4 = Label(wrapper3, text="ID Number")
        lbl4.grid(row=3, column=0, padx=5, pady=3)
        ent4 = Entry(wrapper3, textvariable=t4)
        ent4.grid(row=3, column=1, padx=5, pady=3)

        lbl5 = Label(wrapper3, text="Phone Number")
        lbl5.grid(row=4, column=0, padx=5, pady=3)
        ent5 = Entry(wrapper3, textvariable=t5)
        ent5.grid(row=4, column=1, padx=5, pady=3)

        lbl6 = Label(wrapper3, text="Next of Kin Name")
        lbl6.grid(row=5, column=0, padx=5, pady=3)
        ent6 = Entry(wrapper3, textvariable=t6)
        ent6.grid(row=5, column=1, padx=5, pady=3)

        lbl7 = Label(wrapper3, text="Next of Kin ")
        lbl7.grid(row=6, column=0, padx=5, pady=3)
        ent7 = Entry(wrapper3, textvariable=t7)
        ent7.grid(row=6, column=1, padx=5, pady=3)

        # Buttons
        update_btn = Button(wrapper3, text="Update", command=update_details, bg='#8dc63f')
        add_btn = Button(wrapper3, text="Add New", command=add_new, bg='#8dc63f')
        delete_btn = Button(wrapper3, text="Delete", command=delete_details, bg='#8dc63f')
        refresh_btn = Button(wrapper3, text="Refresh", command=self.refresh_details, bg='#8dc63f')
        logout_btn = Button(wrapper3, text="LOGOUT", command=self.logOut, bg='#8dc63f')

        add_btn.grid(row=7, column=0, padx=5, pady=3)
        update_btn.grid(row=7, column=1, padx=5, pady=3)
        delete_btn.grid(row=7, column=2, padx=5, pady=3)
        refresh_btn.place(x=720, y=205)
        logout_btn.place(x=850, y=205)


window = Tk()
ob = Login(window)
window.mainloop()
