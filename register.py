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
        img = Label(Frame_login, image=self.img).place(x=30, y=0, width=1366, height=700)

        # self.img2 = PhotoImage(file="./images/life-choices-logo.png")
        # img2 = Label(Frame_login, image=self.img2).place(x=0, y=10, width=1366, height=700)

        frame_input = Frame(self.window, bg='white')
        frame_input.place(x=320, y=130, height=450, width=350)

        label1 = Label(frame_input, text="Login Here", font=('Arial', 32, 'bold'), fg='black', bg='white')
        label1.place(x=75, y=20)

        label2 = Label(frame_input, text='Username', font=('Arial', 20, 'bold'), fg='black', bg='white')
        label2.place(x=30, y=95)
        self.user_name = Entry(frame_input, font=("time new roman", 15, 'bold'), bg='lightgray')
        self.user_name.place(x=30, y=145, width=270, height=35)

        label3 = Label(frame_input, text="Password", font=("Arial", 20, 'bold'), fg="black", bg='white')
        label3.place(x=30, y=195)
        self.password = Entry(frame_input, font=("Arial", 15, 'bold'), bg='lightgray')
        self.password.place(x=30, y=245, width=270, height=35)

        btn1 = Button(frame_input, text="forgot password?", cursor='hand2', font=('calibri', 10), fg='black', bg='white', bd=0)
        btn1.place(x=125, y=305)

        btn2 = Button(frame_input, text="Login", command=self.login, cursor="hand2", font=("Arial", 15), fg='black', bg='#8dc63f', bd=0, width=15, height=1)
        btn2.place(x=90, y=340)

        btn3 = Button(frame_input, command=self.Register, text="Not Registered?register", cursor="hand2", font=('Arial', 10), bg='white', fg='black', bd=0)
        btn3.place(x=1, y=390)

    def login(self):
        if self.user_name.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "Ensure that all field filled in", parent=self.window)
        else:
            try:
                con = pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Lifechoices_Online')
                cur = con.cursor()
                cur.execute('select * from register where username=%s and password=%s', (self.user_name.get(), self.password.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Username And Password", parent=self.window)
                else:
                    self.appscreen()
                    con.close()
            except Exception as es:
                messagebox.showerror('Error', 'Error Due to : {str(es)}', parent=self.window)

    def Register(self):

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
        self.entry2 = Entry(frame_input2, font=('Arial', 15, 'bold'), bg='lightgray')
        self.entry2.place(x=30, y=245, width=270, height=35)

        label4 = Label(frame_input2, text="Email", font=("Arial", 20, "bold"), fg='black', bg='white')
        label4.place(x=330, y=95)
        self.entry3 = Entry(frame_input2, font=('Arial', 15, 'bold'), bg='lightgray')
        self.entry3.place(x=330, y=145, width=270, height=35)

        label5 = Label(frame_input2, text='Confirm Password', font=('Arial', 20, 'bold'), fg='black', bg='white')
        label5.place(x=330, y=195)
        self.entry4 = Entry(frame_input2, font=('Arial', 15, 'bold'), bg='lightgray')
        self.entry4.place(x=330, y=245, width=270, height=35)

        btn2 = Button(frame_input2, command=self.register, text="Register", cursor="hand2", font=('Arial', 15), fg='black', bg='#8dc63f', bd=0, width=15, height=1)
        btn2.place(x=90, y=340)

        btn3 = Button(frame_input2, command=self.loginform, text="Already Registered?Login", cursor="hand2", font=('Arial', 10), bg='white', fg='black', bd=0)
        btn3.place(x=110, y=390)

    def register(self):
        if self.entry.get() == "" or self.entry2.get() == "" or self.entry3.get() == "" or self.entry4.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.window)
        elif self.entry2.get()!=self.entry4.get():
            messagebox.showerror("Error", "Password and Confirm Password Should Be The Same", parent=self.window)
        else:
            try:
                con=pymysql.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Lifechoices_Online')
                cur = con.cursor()
                cur.execute("select * from register where email=%s", self.entry3.get())
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "User already Exist, Please try another", parent=self.window)
                else:
                    cur.execute("insert into register values(%s,%s,%s,%s)", (self.entry.get(), self.entry3.get(), self.entry2.get(), self.entry4.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Register Successful", parent=self.window)
            except Exception as es:
                messagebox.showerror("Error", "Error due to:{str(es)}", parent=self.window)

    def appscreen(self):

        Frame_login = Frame(self.window, bg='white')
        Frame_login.place(x=0, y=0, height=700, width=1366)
        label1 = Label(Frame_login, text="Hi! Welcome To Life Choices Online", font=('times new romain', 32, 'bold'), fg='black', bg='white')
        label1.place(x=375, y=100)
        label2 = Label(Frame_login, text="")
        label2.place(x=235, y=160)
        btn2 = Button(Frame_login, text="LOGOUT", command=self.loginform, cursor="hand2", font=('times new romain', 15), fg='black', bg='white', bd=0, width=15, height=1)
        btn2.place(x=1000, y=10)

window = Tk()
ob = Login(window)
window.mainloop()
