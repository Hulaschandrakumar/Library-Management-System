from tkinter import *
from tkinter import ttk  # Import ttk for Combobox
import mysql.connector
from tkinter import messagebox
import datetime


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")
        
        # ============================================Variables=======================================================
        self.Member_var = StringVar()
        self.PRN_No_var = StringVar()
        self.ID_var = StringVar()
        self.FirstName_var = StringVar()
        self.LastName_var = StringVar()
        self.Address1_var = StringVar()
        self.Address2_var = StringVar()
        self.PostId_var = StringVar()
        self.Mobile_var = StringVar()
        self.BookId_var = StringVar()
        self.BookTitle_var = StringVar()
        self.Auther_var = StringVar()
        self.DateBorrowed_var = StringVar()
        self.DueDate_var = StringVar()
        self.Days_var = StringVar()
        self.LateReturnFine_var = StringVar()
        self.DateOverDue_var = StringVar()
        self.FinalPrice_var = StringVar()
        
        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("arial", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)
        
        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)
        
        # ===================================== Data Frame Left ========================================
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg="green", bd=12, relief=RIDGE, font=("arial", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)
        
        lblMember = Label(DataFrameLeft, bg="powder blue", text="Member Type", font=("arial", 15, "bold"), padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)
        
        comMember = ttk.Combobox(DataFrameLeft, font=("arial", 15, "bold"), textvariable=self.Member_var, width=22, state="readonly")
        comMember["value"] = ("Admin staff", "Student", "Lecturer")
        comMember.current(0)
        comMember.grid(row=0, column=1)
        
        lblPRN_No = Label(DataFrameLeft, bg="powder blue", text="PRN No:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_No = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.PRN_No_var, width=29)
        txtPRN_No.grid(row=1, column=1)
        
        lblID_No = Label(DataFrameLeft, bg="powder blue", text="ID No:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblID_No.grid(row=2, column=0, sticky=W)
        txtID_No = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.ID_var, width=29)
        txtID_No.grid(row=2, column=1)
        
        lblFirstName = Label(DataFrameLeft, bg="powder blue", text="First Name", font=("arial", 12, "bold"), padx=2, pady=6)
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.FirstName_var, width=29)
        txtFirstName.grid(row=3, column=1)
        
        lblLastName = Label(DataFrameLeft, bg="powder blue", text="Last Name", font=("arial", 12, "bold"), padx=2, pady=6)
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.LastName_var, width=29)
        txtLastName.grid(row=4, column=1)
        
        lblAddress1 = Label(DataFrameLeft, bg="powder blue", text="Address 1", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.Address1_var, width=29)
        txtAddress1.grid(row=5, column=1)
        
        lblAddress2 = Label(DataFrameLeft, bg="powder blue", text="Address 2", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.Address2_var, width=29)
        txtAddress2.grid(row=6, column=1)
        
        lblPostCode = Label(DataFrameLeft, bg="powder blue", text="Post Code", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.PostId_var, width=29)
        txtPostCode.grid(row=7, column=1)
        
        lblMobile = Label(DataFrameLeft, bg="powder blue", text="Mobile", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.Mobile_var, width=29)
        txtMobile.grid(row=8, column=1)
        
        lblBookId = Label(DataFrameLeft, bg="powder blue", text="Book ID", font=("arial", 12, "bold"), padx=2, pady=6)
        lblBookId.grid(row=0, column=2, sticky=W)
        txtBookId = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.BookId_var, width=29)
        txtBookId.grid(row=0, column=3)
        
        lblBookTitle = Label(DataFrameLeft, bg="powder blue", text="Book Title", font=("arial", 12, "bold"), padx=2, pady=6)
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.BookTitle_var, width=29)
        txtBookTitle.grid(row=1, column=3)
        
        lblAuther = Label(DataFrameLeft, bg="powder blue", text="Author Name", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAuther.grid(row=2, column=2, sticky=W)
        txtAuther = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.Auther_var, width=29)
        txtAuther.grid(row=2, column=3)
        
        lblDateBorrowed = Label(DataFrameLeft, bg="powder blue", text="Date Borrowed", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.DateBorrowed_var, width=29)
        txtDateBorrowed.grid(row=3, column=3)
        
        lblDateDue = Label(DataFrameLeft, bg="powder blue", text="Date Due", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.DueDate_var, width=29)
        txtDateDue.grid(row=4, column=3)
        
        lblDays = Label(DataFrameLeft, bg="powder blue", text="Days on Book", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDays.grid(row=5, column=2, sticky=W)
        txtDays = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.Days_var, width=29)
        txtDays.grid(row=5, column=3)
        
        lblLateReturnFine = Label(DataFrameLeft, bg="powder blue", text="Late Return Fine", font=("arial", 12, "bold"), padx=2,pady=6)
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.LateReturnFine_var, width=29)
        txtLateReturnFine.grid(row=6, column=3)

        lblDateOverDue = Label(DataFrameLeft, bg="powder blue", text="Date Over Due", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDateOverDue.grid(row=7, column=2, sticky=W)
        txtDateOverDue = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.DateOverDue_var, width=29)
        txtDateOverDue.grid(row=7, column=3)

        lblFinalPrice = Label(DataFrameLeft, bg="powder blue", text="Actual Price", font=("arial", 12, "bold"), padx=2, pady=6)
        lblFinalPrice.grid(row=8, column=2, sticky=W)
        txtFinalPrice = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.FinalPrice_var, width=29)
        txtFinalPrice.grid(row=8, column=3)

        # ===================================== Data Frame Right ========================================
        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue", fg="green", bd=12, relief=RIDGE, font=("arial", 12, "bold"))
        DataFrameRight.place(x=910, y=5, width=570, height=350)

        self.txtBox = Text(DataFrameRight, font=("arial", 12, "bold"), width=32, height=13, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollBar = Scrollbar(DataFrameRight)
        listScrollBar.grid(row=0, column=1, sticky="ns")

        listBooks = ['Head First Book', 'Learn Python The Hard Way', 'Python Programming', 'Secerete Rahshy','Python Cook Book', 'Into The Machine Learning', 'Machine Technology', 'My Python',
                    'Joss Elif Guru', 'Python Crash Course', 'Automate the Boring Stuff with Python','Fluent Python', 'Learning Python', 'Effective Python: 90 Specific Ways to Write Better Python',
                    'Python for Data Analysis', 'Introduction to Machine Learning with Python','Python Programming: An Introduction to Computer Science', 'Head-First Python',
                    'Python Tricks: The Book', 'Test-Driven Development with Python', 'Python Deep Learning','Mastering Python', 'Think Python: How to Think Like a Computer Scientist',
                    'Data Science from Scratch: First Principles with Python']
        
        
        
        def SelectBook(event=""):
            value = str(listBox.get(listBox.curselection()))
            x = value

            if x == "Head First Book":
                self.BookId_var.set("BID001")
                self.BookTitle_var.set("Head First Book")
                self.Auther_var.set("Kathy Sierra & Bert Bates")

            elif x == "Learn Python The Hard Way":
                self.BookId_var.set("BID002")
                self.BookTitle_var.set("Learn Python The Hard Way")
                self.Auther_var.set("Zed A. Shaw")

            elif x == "Python Programming":
                self.BookId_var.set("BID003")
                self.BookTitle_var.set("Python Programming")
                self.Auther_var.set("Guido van Rossum")

            elif x == "Secerete Rahshy":
                self.BookId_var.set("BID004")
                self.BookTitle_var.set("Secerete Rahshy")
                self.Auther_var.set("Unknown")

            elif x == "Python Cook Book":
                self.BookId_var.set("BID005")
                self.BookTitle_var.set("Python Cook Book")
                self.Auther_var.set("David Beazley & Brian K. Jones")

            elif x == "Into The Machine Learning":
                self.BookId_var.set("BID006")
                self.BookTitle_var.set("Into The Machine Learning")
                self.Auther_var.set("Unknown")

            elif x == "Machine Technology":
                self.BookId_var.set("BID007")
                self.BookTitle_var.set("Machine Technology")
                self.Auther_var.set("Unknown")

            elif x == "My Python":
                self.BookId_var.set("BID008")
                self.BookTitle_var.set("My Python")
                self.Auther_var.set("Unknown")

            elif x == "Joss Elif Guru":
                self.BookId_var.set("BID009")
                self.BookTitle_var.set("Joss Elif Guru")
                self.Auther_var.set("Unknown")

            elif x == "Python Crash Course":
                self.BookId_var.set("BID010")
                self.BookTitle_var.set("Python Crash Course")
                self.Auther_var.set("Eric Matthes")

            elif x == "Automate the Boring Stuff with Python":
                self.BookId_var.set("BID011")
                self.BookTitle_var.set("Automate the Boring Stuff with Python")
                self.Auther_var.set("Al Sweigart")

            elif x == "Fluent Python":
                self.BookId_var.set("BID012")
                self.BookTitle_var.set("Fluent Python")
                self.Auther_var.set("Luciano Ramalho")

            elif x == "Learning Python":
                self.BookId_var.set("BID013")
                self.BookTitle_var.set("Learning Python")
                self.Auther_var.set("Mark Lutz")

            elif x == "Effective Python: 90 Specific Ways to Write Better Python":
                self.BookId_var.set("BID014")
                self.BookTitle_var.set("Effective Python: 90 Specific Ways to Write Better Python")
                self.Auther_var.set("Brett Slatkin")

            elif x == "Python for Data Analysis":
                self.BookId_var.set("BID015")
                self.BookTitle_var.set("Python for Data Analysis")
                self.Auther_var.set("Wes McKinney")

            elif x == "Introduction to Machine Learning with Python":
                self.BookId_var.set("BID016")
                self.BookTitle_var.set("Introduction to Machine Learning with Python")
                self.Auther_var.set("Andreas C. Müller & Sarah Guido")

            elif x == "Python Programming: An Introduction to Computer Science":
                self.BookId_var.set("BID017")
                self.BookTitle_var.set("Python Programming: An Introduction to Computer Science")
                self.Auther_var.set("John Zelle")

            elif x == "Head-First Python":
                self.BookId_var.set("BID018")
                self.BookTitle_var.set("Head-First Python")
                self.Auther_var.set("Paul Barry")

            elif x == "Python Tricks: The Book":
                self.BookId_var.set("BID019")
                self.BookTitle_var.set("Python Tricks: The Book")
                self.Auther_var.set("Dan Bader")

            elif x == "Test-Driven Development with Python":
                self.BookId_var.set("BID020")
                self.BookTitle_var.set("Test-Driven Development with Python")
                self.Auther_var.set("Harry J.W. Percival")

            elif x == "Python Deep Learning":
                self.BookId_var.set("BID021")
                self.BookTitle_var.set("Python Deep Learning")
                self.Auther_var.set("Ivan Vasilev")

            elif x == "Mastering Python":
                self.BookId_var.set("BID022")
                self.BookTitle_var.set("Mastering Python")
                self.Auther_var.set("Rick van Hattem")

            elif x == "Think Python: How to Think Like a Computer Scientist":
                self.BookId_var.set("BID023")
                self.BookTitle_var.set("Think Python: How to Think Like a Computer Scientist")
                self.Auther_var.set("Allen B. Downey")

            elif x == "Data Science from Scratch: First Principles with Python":
                self.BookId_var.set("BID024")
                self.BookTitle_var.set("Data Science from Scratch: First Principles with Python")
                self.Auther_var.set("Joel Grus")


        
        def SelectBook(event=""):
            value = str(listBox.get(listBox.curselection()))
            x = value
            if x == "Cinderella":
                self.BookId_var.set("BID123")
                self.BookTitle_var.set("Cinderella")
                self.Auther_var.set("Unknown")

            elif x == "Python Programming":
                self.BookId_var.set("BID124")
                self.BookTitle_var.set("Python Programming")
                self.Auther_var.set("Guido van Rossum")

            elif x == "Data Science":
                self.BookId_var.set("BID125")
                self.BookTitle_var.set("Data Science")
                self.Auther_var.set("Cathy O'Neil")
                
                

        listBox = Listbox(DataFrameRight, font=("arial", 12, "bold"), width=20, height=13)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0, column=0, padx=4)
        listScrollBar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END, item)

        # ===================================== Buttons ========================================
        framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        framebutton.place(x=0, y=530, width=1530, height=70)

        btnAddData = Button(framebutton, command=self.add_data, text="Add Data", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=0)

        btnShowData = Button(framebutton, command=self.show_data, text="Show Data", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnShowData.grid(row=0, column=1)

        btnUpdate = Button(framebutton, command=self.update, text="Update", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(framebutton, command=self.delete, text="Delete", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnDelete.grid(row=0, column=3)

        btnReset = Button(framebutton, command=self.reset, text="Reset", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnReset.grid(row=0, column=4)

        btnExit = Button(framebutton, command=self.exit, text="Exit", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnExit.grid(row=0, column=5)

        # ===================================== Table Frame ========================================
        frameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frameDetails.place(x=0, y=600, width=1530, height=190)

        table_frame = Frame(frameDetails, bd=6, relief=RIDGE, bg="powder blue")
        table_frame.place(x=0, y=2, width=1490, height=170)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(table_frame, column=("membertype", "prnno", "idno", "firstname", "lastname", "address1", "address2",
                                                              "postcode", "mobile", "bookid", "booktitle", "auther", "dateborrowed", "datedue", 
                                                              "days", "latereturnfine", "dateoverdue", "finalprice"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.library_table.xview)
        scroll_y.config(command=self.library_table.yview)

        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("prnno", text="PRN No.")
        self.library_table.heading("idno", text="ID No.")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address1", text="Address 1")
        self.library_table.heading("address2", text="Address 2")
        self.library_table.heading("postcode", text="Post Code")
        self.library_table.heading("mobile", text="Mobile")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("auther", text="Author")
        self.library_table.heading("dateborrowed", text="Date Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="Days On Book")
        self.library_table.heading("latereturnfine", text="Late Return Fine")
        self.library_table.heading("dateoverdue", text="Date Over Due")
        self.library_table.heading("finalprice", text="Final Price")

        self.library_table["show"] = "headings"

        self.library_table.column("membertype", width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("idno", width=100)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("postcode", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("auther", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)

        self.library_table.pack(fill=BOTH, expand=1)
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

        # self.fetch_data()

    # ===================================== Functionality ========================================
    def add_data(self):
        if self.Member_var.get() == "" or self.PRN_No_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                con = mysql.connector.connect(host="localhost", username="root", password="12114496", database="signup_form")
                cur = con.cursor()
                cur.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.Member_var.get(),
                    self.PRN_No_var.get(),
                                        self.ID_var.get(),
                    self.FirstName_var.get(),
                    self.LastName_var.get(),
                    self.Address1_var.get(),
                    self.Address2_var.get(),
                    self.PostId_var.get(),
                    self.Mobile_var.get(),
                    self.BookId_var.get(),
                    self.BookTitle_var.get(),
                    self.Auther_var.get(),
                    self.DateBorrowed_var.get(),
                    self.DueDate_var.get(),
                    self.Days_var.get(),
                    self.LateReturnFine_var.get(),
                    self.DateOverDue_var.get(),
                    self.FinalPrice_var.get()
                ))
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Success", "Member has been inserted successfully")
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}")

    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", username="root", password="12114496", database="signup_form")
        cur = con.cursor()
        cur.execute("select * from library")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for row in rows:
                self.library_table.insert("", END, values=row)
            con.commit()
        con.close()

    def get_cursor(self, event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content["values"]
        self.Member_var.set(row[0])
        self.PRN_No_var.set(row[1])
        self.ID_var.set(row[2])
        self.FirstName_var.set(row[3])
        self.LastName_var.set(row[4])
        self.Address1_var.set(row[5])
        self.Address2_var.set(row[6])
        self.PostId_var.set(row[7])
        self.Mobile_var.set(row[8])
        self.BookId_var.set(row[9])
        self.BookTitle_var.set(row[10])
        self.Auther_var.set(row[11])
        self.DateBorrowed_var.set(row[12])
        self.DueDate_var.set(row[13])
        self.Days_var.set(row[14])
        self.LateReturnFine_var.set(row[15])
        self.DateOverDue_var.set(row[16])
        self.FinalPrice_var.set(row[17])

    def update(self):
        if self.Member_var.get() == "" or self.PRN_No_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                con = mysql.connector.connect(host="localhost", username="root", password="12114496", database="signup_form")
                cur = con.cursor()
                cur.execute(
                    "update library set Member=%s, ID=%s, FirstName=%s, LastName=%s, Address1=%s, Address2=%s, PostCode=%s, Mobile=%s, BookID=%s, BookTitle=%s, Auther=%s, DateBorrowed=%s, DueDate=%s, Days=%s, LateReturnFine=%s, DateOverDue=%s, FinalPrice=%s where PRN_No=%s", (
                        self.Member_var.get(),
                        self.ID_var.get(),
                        self.FirstName_var.get(),
                        self.LastName_var.get(),
                        self.Address1_var.get(),
                        self.Address2_var.get(),
                        self.PostId_var.get(),
                        self.Mobile_var.get(),
                        self.BookId_var.get(),
                        self.BookTitle_var.get(),
                        self.Auther_var.get(),
                        self.DateBorrowed_var.get(),
                        self.DueDate_var.get(),
                        self.Days_var.get(),
                        self.LateReturnFine_var.get(),
                        self.DateOverDue_var.get(),
                        self.FinalPrice_var.get(),
                        self.PRN_No_var.get()
                    ))
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Success", "Record has been updated successfully")
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}")

    def delete(self):
        try:
            con = mysql.connector.connect(host="localhost", username="root", password="12114496", database="signup_form")
            cur = con.cursor()
            cur.execute("delete from library where PRN_No=%s", (self.PRN_No_var.get(),))
            con.commit()
            con.close()
            self.fetch_data()
            self.reset()
            messagebox.showinfo("Success", "Member has been deleted")
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}")

    def reset(self):
        self.Member_var.set("")
        self.PRN_No_var.set("")
        self.ID_var.set("")
        self.FirstName_var.set("")
        self.LastName_var.set("")
        self.Address1_var.set("")
        self.Address2_var.set("")
        self.PostId_var.set("")
        self.Mobile_var.set("")
        self.BookId_var.set("")
        self.BookTitle_var.set("")
        self.Auther_var.set("")
        self.DateBorrowed_var.set("")
        self.DueDate_var.set("")
        self.Days_var.set("")
        self.LateReturnFine_var.set("")
        self.DateOverDue_var.set("")
        self.FinalPrice_var.set("")

    def show_data(self):
        self.txtBox.delete("1.0", END)
        self.txtBox.insert(END, f"Member Type: {self.Member_var.get()}\n")
        self.txtBox.insert(END, f"PRN No: {self.PRN_No_var.get()}\n")
        self.txtBox.insert(END, f"ID No: {self.ID_var.get()}\n")
        self.txtBox.insert(END, f"First Name: {self.FirstName_var.get()}\n")
        self.txtBox.insert(END, f"Last Name: {self.LastName_var.get()}\n")
        self.txtBox.insert(END, f"Address 1: {self.Address1_var.get()}\n")
        self.txtBox.insert(END, f"Address 2: {self.Address2_var.get()}\n")
        self.txtBox.insert(END, f"Post Code: {self.PostId_var.get()}\n")
        self.txtBox.insert(END, f"Mobile: {self.Mobile_var.get()}\n")
        self.txtBox.insert(END, f"Book ID: {self.BookId_var.get()}\n")
        self.txtBox.insert(END, f"Book Title: {self.BookTitle_var.get()}\n")
        self.txtBox.insert(END, f"Author: {self.Auther_var.get()}\n")
        self.txtBox.insert(END, f"Date Borrowed: {self.DateBorrowed_var.get()}\n")
        self.txtBox.insert(END, f"Date Due: {self.DueDate_var.get()}\n")
        self.txtBox.insert(END, f"Days On Book: {self.Days_var.get()}\n")
        self.txtBox.insert(END, f"Late Return Fine: {self.LateReturnFine_var.get()}\n")
        self.txtBox.insert(END, f"Date Over Due: {self.DateOverDue_var.get()}\n")
        self.txtBox.insert(END, f"Final Price: {self.FinalPrice_var.get()}\n")

    def exit(self):
        exit_confirm = messagebox.askyesno("Library Management System", "Do you really want to exit?")
        if exit_confirm > 0:
            self.root.destroy()
        return


if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()