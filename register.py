from tkinter import *
from tkinter import ttk, messagebox
import pymysql

class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1350x700+250+180")
        self.root.config(bg="#021e2f")

        #-----------Register Frame----------
        frame1= Frame(self.root ,bg="white")
        frame1.place(height=500,width=700,y=100,x=325)

        title=Label(frame1,text="REGISTER HERE",font=("Calibre",15),fg="black",bg="white").place(x=272,y=30)

        f_name=Label(frame1,text="First Name",font=("Calibre",13),fg="grey",bg="white").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("Calibre",15),bg="light grey")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last Name",font=("Calibre",13),fg="grey",bg="white").place(x=390,y=100)
        self.txt_lname=Entry(frame1,font=("Calibre",15),bg="light grey")
        self.txt_lname.place(x=390,y=130,width=250)

        contact=Label(frame1,text="Contact",font=("Calibre",13),fg="grey",bg="white").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("Calibre",15),bg="light grey")
        self.txt_contact.place(x=50,y=200,width=250)
                                                                                                         
        email=Label(frame1,text="Email",font=("Calibre",13),fg="grey",bg="white").place(x=390,y=170)
        self.txt_email=Entry(frame1,font=("Calibre",15),bg="light grey")
        self.txt_email.place(x=390,y=200,width=250)

        question=Label(frame1,text="Security Question",font=("Calibre",13),fg="grey",bg="white").place(x=50,y=240)
        self.cmb_quest=ttk.Combobox(frame1,font=("Calibre",12),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("Choose","Your favourite subject","Your college name","Your friend name")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)

        answer=Label(frame1,text="Answer",font=("Calibre",13),fg="grey",bg="white").place(x=390,y=240)
        self.txt_answer=Entry(frame1,font=("Calibre",15),bg="light grey")
        self.txt_answer.place(x=390,y=270,width=250)

        password=Label(frame1,text="Password",font=("Calibre",13),fg="grey",bg="white").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("Calibre",15),bg="light grey")
        self.txt_password.place(x=50,y=340,width=250)

        Confirm_pass=Label(frame1,text="Confirm Password",font=("Calibre",13),fg="grey",bg="white").place(x=390,y=310)
        self.txt_Confirm_pass=Entry(frame1,font=("Calibre",15),bg="light grey")
        self.txt_Confirm_pass.place(x=390,y=340,width=250)

        btn_register = Button(frame1,text="Register",fg="white",bg="green",cursor="hand2",command=self.register_data).place(height=40,width=130,x=50,y=400)
        btn_login = Button(frame1, text="Login", fg="white", bg="#000FE1", cursor="hand2",command=self.login_window).place(height=40, width=130, x=390, y=400)

        Label(frame1,text="Please Login, If you already have an account ! ",bg="white",font=("Calibre",11)).place(x=50,y=450)

    #--------register()----------
    def register_data(self):
        contact = self.txt_contact.get()
        if self.txt_fname.get() == "":
            messagebox.showerror("Error", "first name not Entered!!",parent=self.root)
        elif self.txt_lname.get() == "":
            messagebox.showerror("Error", "Last name not Entered!!",parent=self.root)
        elif self.txt_email.get() == "":
            messagebox.showerror("Error", "Email not Entered!!",parent=self.root)
        elif len(self.txt_contact.get()) < 10 or int(contact[0])<7:
            messagebox.showerror("Error", "Enter a valid 10 digit Mobile no !!",parent=self.root)
        elif self.cmb_quest.get() == "Choose":
            messagebox.showerror("Error", "Security question not chosen!!",parent=self.root)
        elif self.txt_answer.get() == "":
            messagebox.showerror("Error", "Answer not Entered!!",parent=self.root)
        elif self.txt_password.get() == "" or len(self.txt_password.get()) < 5:
            messagebox.showerror("Error", "Enter a password with at-least 5 and at-most 15 characters",parent=self.root)
        elif self.txt_Confirm_pass.get() != self.txt_password.get():
            messagebox.showerror("Error", "Password and Confirm password do not match!!",parent=self.root)
        else:
            try:
                con = pymysql.connect(port=3307, host="localhost", user="root", password="", database="employee")
                cur = con.cursor()
                cur.execute("SELECT * FROM employee WHERE email =%s", self.txt_email.get())   # check if email is already registered
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "Current E-mail is already Registered. Please try with another E-mail!!", parent=self.root)
                else:
                    cur.execute("INSERT INTO employee (f_name,l_name,contact,email,question,answer,password) VALUES(%s,%s,%s,%s,%s,%s,%s)",    (self.txt_fname.get(),
                                                                                                                                                self.txt_lname.get(),
                                                                                                                                                self.txt_contact.get(),
                                                                                                                                                self.txt_email.get(),
                                                                                                                                                self.cmb_quest.get(),
                                                                                                                                                self.txt_answer.get(),
                                                                                                                                                self.txt_password.get(),
                                                                                                                                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","You have Registered Successfully!!",parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

    #--------------clear text Entries--------------
    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_answer.delete(0,END)
        self.txt_Confirm_pass.delete(0, END)
        self.cmb_quest.current(0)

    #-------redirect to login.py--------------
    def login_window(self):
        self.root.destroy()
        import login



root = Tk()
ob = Register(root)
root.mainloop()