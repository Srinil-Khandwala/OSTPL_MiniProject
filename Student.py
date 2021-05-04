from tkinter import *
from tkinter import ttk, messagebox
import pymysql


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+250+180")
        self.root.config(bg="#50626B")

        # canvas=Canvas(self.root,bg="#50626B")
        # canvas.place(x=0,y=0,height=700,width=1350)

        # --------------Student Management sys Title in window(yellow,Red)----------------------
        title = Label(self.root, text="STUDENT MANAGEMENT SYSTEM", font=("Calibre", 40), bg="#50626B", bd=5, fg="white")
        title.place(x=0, y=0, width=1150)

        # ------Logout button-------------
        btn_logout = Button(self.root, text="Logout", width=10, fg="white", bg="Red", command=self.logout_window).place(width=100, x=1200, y=20, height=40)

        # ---------------All Variables-----------------------
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        # -------Search Variables------
        self.search_by = StringVar()
        self.search_txt = StringVar()

        # ---------------Left Frame = Manage Frame(Crimson)------------------
        Manage_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="#2A3338")
        Manage_Frame.place(x=20, y=100, width=450, height=580)

        m_title = Label(Manage_Frame, text="MANAGE STUDENTS", font=("Calibre", 20), fg="white", bg="#2A3338")
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = Label(Manage_Frame, text="ROLL NO", font=("Calibre", 15), fg="white", bg="#2A3338")
        lbl_roll.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        txt_Roll = Entry(Manage_Frame, textvariable=self.Roll_No_var, font=("Calibre", 13), width=22, bd=5, relief=FLAT)
        txt_Roll.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        lbl_name = Label(Manage_Frame, text="NAME", font=("Calibre", 15), fg="white", bg="#2A3338")
        lbl_name.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        txt_name = Entry(Manage_Frame, textvariable=self.name_var, font=("Calibre", 13), width=22, bd=5, relief=FLAT)
        txt_name.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        lbl_email = Label(Manage_Frame, text="E-MAIL", font=("Calibre", 15), fg="white", bg="#2A3338")
        lbl_email.grid(row=3, column=0, padx=20, pady=10, sticky="w")

        txt_email = Entry(Manage_Frame, textvariable=self.email_var, font=("Calibre", 13), width=22, bd=5, relief=FLAT)
        txt_email.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        lbl_gender = Label(Manage_Frame, text="GENDER", font=("Calibre", 15), fg="white", bg="#2A3338")
        lbl_gender.grid(row=4, column=0, padx=20, pady=10, sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("Calibre", 13), width=22, state='readonly')
        combo_gender['values'] = ("Select","Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=4, column=1, padx=20, pady=10, sticky="w")

        lbl_contact = Label(Manage_Frame, text="CONTACTS", font=("Calibre", 15), fg="white", bg="#2A3338")
        lbl_contact.grid(row=5, column=0, padx=20, pady=10, sticky="w")

        txt_contact = Entry(Manage_Frame, textvariable=self.contact_var, font=("Calibre", 13), width=22, bd=5, relief=FLAT)
        txt_contact.grid(row=5, column=1, padx=20, pady=10, sticky="w")

        lbl_DOB = Label(Manage_Frame, text="DOB", font=("Calibre", 15), fg="white", bg="#2A3338")
        lbl_DOB.grid(row=6, column=0, padx=20, pady=10, sticky="w")

        txt_DOB = Entry(Manage_Frame, textvariable=self.dob_var, font=("Calibre", 13), width=22, bd=5, relief=FLAT)
        txt_DOB.grid(row=6, column=1, padx=20, pady=10, sticky="w")

        lbl_Address = Label(Manage_Frame, text="ADDRESS", font=("Calibre", 15), fg="white", bg="#2A3338")
        lbl_Address.grid(row=7, column=0, padx=20, pady=10, sticky="w")

        self.txt_Address = Text(Manage_Frame, font=("Calibre", 13), width=23, height=3)
        self.txt_Address.grid(row=7, column=1, padx=20, pady=10, sticky="w")

        # ---------------Button Frame----------------------------
        btn_Frame = Frame(Manage_Frame, bd=2, relief=RIDGE, bg="#2A3338")
        btn_Frame.place(x=10, y=510, width=420)

        Addbtn = Button(btn_Frame, text="ADD", width=10, command=self.Add_Students).grid(row=0, column=0, pady=10, padx=10)
        updatebtn = Button(btn_Frame, text="UPDATE", width=10, command=self.update_data).grid(row=0, column=1, pady=10, padx=10)
        deletebtn = Button(btn_Frame, text="DELETE", width=10, command=self.delete_data).grid(row=0, column=2, pady=10, padx=10)
        Clearbtn = Button(btn_Frame, text="CLEAR", width=10, command=self.clear).grid(row=0, column=3, pady=10, padx=10)

        # ---------------Right Frame = Detail Frame(Crimson)------------------------
        Detail_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="#2A3338")
        Detail_Frame.place(x=500, y=100, width=800, height=580)

        lbl_searchBy = Label(Detail_Frame, text="SEARCH BY", font=("Calibre", 15), fg="white", bg="#2A3338")
        lbl_searchBy.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, font=("Calibre", 13), width=10, state='readonly')
        combo_search['values'] = ("Select","Roll_no", "Name", "contact","gender","address","dob")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        txt_search = Entry(Detail_Frame, textvariable=self.search_txt, font=("Calibre", 13), bd=5, relief=SUNKEN)
        txt_search.grid(row=0, column=2, padx=20, pady=10, sticky="w")

        searchbtn = Button(Detail_Frame, text="SEARCH", width=10, command=self.search_data).grid(row=0, column=3, pady=10, padx=10)
        showallbtn = Button(Detail_Frame, text="SHOW ALL", width=10, command=self.fetch_data).grid(row=0, column=4, pady=10, padx=10)

        # ------------------------Table Frame-------------------------------------
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="#2A3338")
        Table_Frame.place(x=20, y=70, width=760, height=490)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame, columns=("roll", "name", "email", "gender", "contact", "dob", "address"), xscrollcomman=scroll_x, yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("roll", text="Roll no.")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="DOB")
        self.Student_table.heading("address", text="Address")
        self.Student_table['show'] = 'headings'
        self.Student_table.column("roll", width=80)
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("address", width=150)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    def Add_Students(self):
        dob = self.dob_var.get()
        dob_date = dob[0]+dob[1]
        dob_month = dob[3]+dob[4]
        dob_year=dob[6]+dob[7]
        contact = self.contact_var.get()
        if self.Roll_No_var.get() == "":
            messagebox.showerror("Error", "Roll no not Entered!!")
        elif self.name_var.get() == "":
            messagebox.showerror("Error", "Name not Entered!!")
        elif self.email_var.get() == "":
            messagebox.showerror("Error", "Email not Entered!!")
        elif self.gender_var.get() == "":
            messagebox.showerror("Error", "Gender not Entered!!")
        elif len(str(self.dob_var.get()))<10 or int(dob_year)>20 or int(dob_year)<19 or int(dob_date)>31 or int(dob_month)>12:
            messagebox.showerror("Error", "Enter valid DOB (DD/MM/YYYY)!!")
        elif len(str(self.contact_var.get())) < 10 or int(contact[0])<7:
            messagebox.showerror("Error", "Enter a valid 10 digit Mobile no!!")
        elif self.txt_Address.get('1.0', END) == "":
            messagebox.showerror("Error", "Address not Entered")
        else:
            con = pymysql.connect(port=3307, host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("INSERT INTO students values(%s,%s,%s,%s,%s,%s,%s)", (self.Roll_No_var.get(),
                                                                              self.name_var.get(),
                                                                              self.email_var.get(),
                                                                              self.gender_var.get(),
                                                                              self.contact_var.get(),
                                                                              self.dob_var.get(),
                                                                              self.txt_Address.get('1.0', END)
                                                                              ))
            result = messagebox.askquestion("Add", "Do you want to Add the record?")
            if result == "yes":
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success", "Record Inserted!!")
            else:
                con.close()
                self.fetch_data()
            # con.commit()
            # self.fetch_data()
            # self.clear()
            # con.close()


    # ---------------fetch data---------------------
    def fetch_data(self):
        con = pymysql.connect(port=3307, host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children()) # delete every row present in the Student_table
            for row in rows:
                self.Student_table.insert('', END, values=row) # insert all rows fetched from the database in Student_table
                con.commit()
        con.close()


    # ---------------------Clear values in Entry fields----------------
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.gender_var.set("")
        self.txt_Address.delete("1.0", END)

    # -----------assigns data to the Entry fields on clicking on a particular row in the table-----------
    def get_cursor(self, ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)  # returns dictionary
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END, row[6])


    # ----------------Update data-----------------
    def update_data(self):
        con = pymysql.connect(port=3307, host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("UPDATE students SET name=%s, email=%s, gender=%s, contact=%s, dob=%s, address=%s WHERE roll_no=%s",(self.name_var.get(),
                                                                                                                         self.email_var.get(),
                                                                                                                         self.gender_var.get(),
                                                                                                                         self.contact_var.get(),
                                                                                                                         self.dob_var.get(),
                                                                                                                         self.txt_Address.get('1.0', END),
                                                                                                                         self.Roll_No_var.get()
                                                                                                                         ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    # -------------Delete data---------------
    def delete_data(self):
        con = pymysql.connect(port=3307, host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("DELETE FROM students WHERE roll_no=%s", self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()



    # -------------------Search data-----------------------
    def search_data(self):
        con = pymysql.connect(port=3307, host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("SELECT * FROM students WHERE " + str(self.search_by.get()) + " LIKE '%" + str(self.search_txt.get()) + "%'")
        rows = cur.fetchall()
        if rows == None:
            messagebox.showerror("Error", "No record Found!")
        elif len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
                con.commit()
        con.close()


    # ---------redirect to register.py----------------
    def logout_window(self):
        self.root.destroy()
        import login


root = Tk()
ob = Student(root)
root.mainloop()
