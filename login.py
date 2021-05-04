from tkinter import *
from tkinter import ttk, messagebox
import pymysql

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1350x700+250+180")
        self.root.config(bg="#021e2f")

        #------------------------Login Frame-----------------------
        login_frame= Frame(self.root ,bg="white")
        login_frame.place(height=450,width=500,y=100,x=425)

        title=Label(login_frame,text="LOGIN",font=("Calibre",18),fg="black",bg="white").place(x=220,y=30)

        email=Label(login_frame,text="E-mail",font=("Calibre",13),fg="grey",bg="white").place(x=125,y=100)
        self.txt_email=Entry(login_frame,font=("Calibre",15),bg="light grey")
        self.txt_email.place(x=125,y=130,width=250)

        password=Label(login_frame,text="Password",font=("Calibre",13),fg="grey",bg="white").place(x=125,y=180)
        self.txt_password=Entry(login_frame,font=("Calibre",15),bg="light grey")
        self.txt_password.place(x=125,y=210,width=250)

        btn_reg=Button(login_frame,text="Register new Account?",font=("Calibre",11),fg="blue",bg="white",bd=0,cursor="hand2",command=self.register_window).place(x=125,y=260)
        btn_forgot = Button(login_frame, text="Forgot Password?", font=("Calibre", 11), fg="blue", bg="white", bd=0,cursor="hand2",command=self.Forget_Password_window).place(x=125, y=290, width=150)
        btn_login=Button(login_frame,text="Login",font=("Calibre",14),fg="white",bg="green",bd=0,cursor="hand2",command=self.login).place(x=175,y=350,width=150)

    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error", "All fields are required!!", parent=self.root)
        else:
            try:
                con = pymysql.connect(port=3307, host="localhost", user="root", password="", database="employee")
                cur = con.cursor()
                cur.execute("SELECT * FROM employee WHERE email =%s and password =%s",(self.txt_email.get(),self.txt_password.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Username or password. Enter correct credentials!!",parent=self.root)
                else:
                    self.root.destroy()
                    import Student
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


    #------redirect to register.py-------------
    def register_window(self):
        self.root.destroy()
        import register


    #-------forgot password tkinter---------
    def Forget_Password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter a valid email address to reset",parent=self.root)
        else:
            try:
                con = pymysql.connect(port=3307, host="localhost", user="root", password="", database="employee")
                cur = con.cursor()
                cur.execute("SELECT * FROM employee WHERE email =%s",self.txt_email.get())
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid email ID!!",parent=self.root)
                else:
                    # con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forgot Password")
                    self.root2.geometry("500x450+675+290")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    forgot_pass = Frame(self.root2, bg="white")
                    forgot_pass.place(height=450, width=500)

                    title = Label(forgot_pass, text="FORGOT PASSWORD", font=("Calibre", 18), fg="black", bg="white").place(x=125, y=30)

                    question = Label(forgot_pass, text="Security Question", font=("Calibre", 13), fg="grey", bg="white").place(x=125, y=100)
                    self.cmb_quest = ttk.Combobox(forgot_pass, font=("Calibre", 12), state='readonly', justify=CENTER)
                    self.cmb_quest['values'] = ("Choose", "Your favourite subject", "Your college name", "Your friend name")
                    self.cmb_quest.place(x=125, y=135, width=250)
                    self.cmb_quest.current(0)

                    answer = Label(forgot_pass, text="Answer", font=("Calibre", 13), fg="grey", bg="white").place(x=125, y=180)
                    self.txt_answer = Entry(forgot_pass, font=("Calibre", 15), bg="light grey")
                    self.txt_answer.place(x=125, y=210, width=250)

                    new_password = Label(forgot_pass, text="New Password", font=("Calibre", 13), fg="grey", bg="white").place(x=125, y=260)
                    self.txt_new_password = Entry(forgot_pass, font=("Calibre", 15), bg="light grey")
                    self.txt_new_password.place(x=125, y=290, width=250)
                    # print(self.cmb_quest.get(),self.txt_answer.get(),self.txt_new_password.get())

                    btn_change_pass = Button(forgot_pass, text="Reset Password", font=("Calibre", 11), fg="white",bg="green", bd=0, cursor="hand2",command=self.Forget_window).place(x=175, y=360, height=40, width=150)
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


    #------------Change password Button----------
    def Forget_window(self):
        if self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                con = pymysql.connect(port=3307, host="localhost", user="root", password="", database="employee")
                cur = con.cursor()
                cur.execute("SELECT * FROM employee WHERE email =%s and question=%s and answer=%s", (self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Please select the correct Security Question / answer!!", parent=self.root)
                else:
                    cur.execute("UPDATE employee SET password=%s WHERE email=%s",(self.txt_new_password.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your password has been reset,Please login with new password",parent=self.root2)
                    self.reset()
                    self.root2.destroy()
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent= self.root2)


    #-------------Reset value in Login and forgot password window---------------
    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_password.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_email.delete(0,END)


root = Tk()
ob = Login(root)
root.mainloop()