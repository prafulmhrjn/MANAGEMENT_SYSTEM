#imports
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
def login_page():
    # Databases
    # Create a databases or connect to one
    conn = sqlite3.connect('address_book1.db')
    # Create cursor
    c = conn.cursor()
    # Create table
    '''
    c.execute(""" CREATE TABLE addresses(
            ref_no integer,
            Bookname text,
            MemType text,
            BookG text,
            Address text,
            issue_date integer,
            Actualprice integer,
            Mobile integer,
            Author integer,
            Post text,
            Dateo text,
            Description text
    ) """)
    '''
    # Create submit button for databases
    def submit():
        # Create a databases or connect to one
        conn = sqlite3.connect('address_book1.db')
        # Create cursor
        c = conn.cursor()
        # Insert into table
        c.execute(
            "INSERT INTO addresses VALUES (:ref_no, :Bookname, :Mem_type, :BookG, :Address, :issue_date, :Actualprice, :Mobile, :Author, :Post, :Dateo, :Description)",
            {
                'ref_no': Refno_entry.get(),
                'Bookname': Bookname_entry.get(),
                'Mem_type': MemType_combo.get(),
                'BookG': BookG_entry.get(),
                'Address': Address_entry.get(),
                'issue_date': Issue_entry.get(),
                'Actualprice': Actual_entry.get(),
                'Mobile': Mobile_entry.get(),
                'Author': Author_entry.get(),
                'Post': Post_entry.get(),
                'Dateo': Dateo_entry.get(),
                'Description': Description_entry.get(),

            })
        conn.commit()
        conn.close()
        # clear the text boxes
        Refno_entry.delete(0, END)
        Bookname_entry.delete(0, END)
        MemType_combo.delete(0, END)
        BookG_entry.delete(0, END)
        Address_entry.delete(0, END)
        Issue_entry.delete(0, END)
        Actual_entry.delete(0, END)
        Mobile_entry.delete(0, END)
        Author_entry.delete(0, END)
        Post_entry.delete(0, END)
        Dateo_entry.delete(0, END)
        Description_entry.delete(0, END)
        messagebox.showinfo("Book added", "BOOK ADDED SUCCESSFULLY")
    def query():
        # Create a databases or connect to one
        conn = sqlite3.connect('address_book1.db')
        # Create cursor
        c = conn.cursor()
        # query of the database
        c.execute("SELECT *, oid FROM addresses")
        records = c.fetchall()
        print("After show button", records)
        # Loop through the results
        print_record = ''
        for record in records:
            print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[2]) + ' ' + str(record[3]) + ' ' + str(
                record[4]) + ' ' + str(record[5]) + ' ' + str(record[6]) + ' ' + str(record[7]) + ' ' + str(
                record[8]) + ' ' + str(record[9]) + ' ' + str(record[10]) + ' ' + str(record[11]) + ' ' + str(
                record[12]) + "\n"
        print("showing data", print_record)
        query_label = Label(details_frame, text=print_record)
        query_label.place(x=0, y=0)
        conn.commit()
        conn.close()
    def delete():
        # Create a databases or connect to one
        conn = sqlite3.connect('address_book1.db')
        # Create cursor
        c = conn.cursor()
        # Delete a record
        c.execute("DELETE from addresses WHERE oid = " + txtsearch.get())
        print("deleted sucessfully")
        # query of databases
        c.execute("SELECT *, oid FROM addresses")
        records = c.fetchall()
        print(records)
        # Loop through the results
        print_record = ''
        for record in records:
            print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[2]) + ' ' + str(record[3]) + ' ' + str(
                record[4]) + ' ' + str(record[5]) + ' ' + str(record[6]) + ' ' + str(record[7]) + ' ' + str(
                record[8]) + ' ' + str(record[9]) + ' ' + str(record[10]) + ' ' + str(record[11]) + ' ' + str(
                record[12]) + "\n"
        query_label = Label(details_frame, text=print_record)
        query_label.place(x=0, y=0)
        conn.commit()
        conn.close()
        messagebox.showinfo("Deleted successfully", "Data Deleted sucessfully")
    def edit():
        global editor

        editor = Tk()
        editor.title('Update Data')
        editor.geometry('600x600')
        editor.geometry('400x400')

        # Create a databases or connect to one
        conn = sqlite3.connect('address_book1.db')
        # Create cursor
        c = conn.cursor()
        record_id = txtsearch.get()
        # query of the database
        c.execute("SELECT * FROM addresses WHERE oid=" + record_id)
        records = c.fetchall()
        # Creating global variable for all text boxes
        global ref_no_editor
        global Bookname_editor
        global Memtype_editor
        global BookG_editor
        global Address_editor
        global Issue_editor
        global Actual_editor
        global Author_editor
        global Post_editor
        global Dateo_editor
        global Description_editor
        # Creating an update function
        def update():
            # Create a databases or connect to one
            conn = sqlite3.connect('address_book1.db')
            # Create cursor
            c = conn.cursor()
            record_id = txtsearch.get()
            c.execute(""" UPDATE addresses SET
                 ref_no = :ref,
                 book_name = :company,
                 med_type = :med_t,
                 med_name = :med_n,
                 lot_no = :lot,
                 issue_date = :issue,
                 expiry_date = :expiry,
                 dosage = :dos,
                 tab_price = :tab_p,
                 precs_warning = :precs,
                 uses = :use,
                 side_effects = :side
                 WHERE oid = :oid""",
                      {'ref': ref_no_editor.get(),
                       'Bookname': Bookname_editor.get(),
                       'Mem_type': Mem_type_editor.get(),
                       'BookG': Bookname_editor.get(),
                       'Address': Address_editor.get(),
                       'issue': issue_editor.get(),
                       'Actualprice': Actualprice_editor.get(),
                       'Mobile': Mobile_editor.get(),
                       'Author': Author_editor.get(),
                       'Post': precs_editor.get(),
                       'Dateo': Dateo_editor.get(),
                       'Description': Description_editor.get(),
                       'oid': record_id
                       }
                      )
            conn.commit()
            conn.close()
            messagebox.showinfo("Updated sucessfully", "YOUR DATA HAVE BEEN SUCCESSFULLY UPDATED")
            # Destroying all the data and closing window
            editor.destroy()
        # Create text boxes
        ref_no_editor = Entry(editor, width=30)
        ref_no_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
        Bookname_editor = Entry(editor, width=30)
        Bookname_editor.grid(row=1, column=1, padx=20, pady=(10, 0))
        Mem_type_editor = Entry(editor, width=30)
        Mem_type_editor.grid(row=2, column=1, padx=20, pady=(10, 0))
        BookG_editor = Entry(editor, width=30)
        BookG_editor.grid(row=3, column=1, padx=20, pady=(10, 0))
        Address_editor = Entry(editor, width=30)
        Address_editor.grid(row=4, column=1, padx=20, pady=(10, 0))
        issue_editor = Entry(editor, width=30)
        issue_editor.grid(row=5, column=1, padx=20, pady=(10, 0))
        Actualprice_editor = Entry(editor, width=30)
        Actualprice_editor.grid(row=6, column=1, padx=20, pady=(10, 0))
        Mobile_editor = Entry(editor, width=30)
        Mobile_editor.grid(row=7, column=1, padx=20, pady=(10, 0))
        Author_editor = Entry(editor, width=30)
        Author_editor.grid(row=8, column=1, padx=20, pady=(10, 0))
        Post_editor = Entry(editor, width=30)
        Post_editor.grid(row=9, column=1, padx=20, pady=(10, 0))
        Dateo_editor = Entry(editor, width=30)
        Dateo_editor.grid(row=10, column=1, padx=20, pady=(10, 0))
        Description_editor = Entry(editor, width=30)
        Description_editor.grid(row=11, column=1, padx=20, pady=(10, 0))
        # Create textbox labels
        ref_no_label = Label(editor, text="Refrence no")
        ref_no_label.grid(row=0, column=0, pady=(10, 0))
        Bookname_label = Label(editor, text="Book Name")
        Bookname_label.grid(row=1, column=0)
        Memtype_label = Label(editor, text="Membership Type")
        Memtype_label.grid(row=2, column=0)
        BookG_label = Label(editor, text="Book G")
        BookG_label.grid(row=3, column=0)
        Address_label = Label(editor, text="Address")
        Address_label.grid(row=4, column=0)
        issue_label = Label(editor, text="Issue Date")
        issue_label.grid(row=5, column=0)
        Actualprice_label = Label(editor, text="Actual Price")
        Actualprice_label.grid(row=6, column=0)
        Mobile_label = Label(editor, text="Mobile")
        Mobile_label.grid(row=7, column=0)
        Author_label = Label(editor, text="Author")
        Author_label.grid(row=8, column=0)
        Post_label = Label(editor, text="Post")
        Post_label.grid(row=9, column=0)
        Dateo_label = Label(editor, text="Dateo")
        Dateo_label.grid(row=10, column=0)
        Description_label = Label(editor, text="Description")
        Description_label.grid(row=11, column=0)
        # loop through the results
        for record in records:
            ref_no_editor.insert(0, record[0])
            Bookname_editor_editor.insert(0, record[1])
            Memtype_editor.insert(0, record[2])
            BookG_editor.insert(0, record[3])
            Address_editor.insert(0, record[4])
            Issue_editor.insert(0, record[5])
            Actualprice_editor.insert(0, record[6])
            Mobile_editor.insert(0, record[7])
            Author_editor.insert(0, record[8])
            Post_editor.insert(0, record[9])
            Dateo_editor.insert(0, record[10])
            Description_editor.insert(0, record[11])
        # Create a update button
        edit_btn = Button(editor, text=" SAVE ", command=update)
        edit_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=125)
    def exit_fun():
        ask = messagebox.askyesno("exit", "Do you want to exit?")
        if ask == 1:
            root.destroy()


    root = Toplevel()
    root.title("Library Management System")
    root.iconbitmap('pill.png')
    root.geometry("1280x680")
    # top title
    title = Label(root, text="Library Management System", bg="maroon", fg="white", font=("Bradley Hand ITC", 50, "bold"))
    title.pack(side=TOP, fill=X, padx=10, pady=10)

    # dataframe
    DataFrame = Frame(root, bd=10, bg="white", relief=RIDGE, padx=20, pady=20)
    DataFrame.place(x=0, y=110, width=1280, height=420)
    # dataframe left
    DataFrameLeft = LabelFrame(DataFrame, bd=10, bg="maroon", relief=RIDGE, padx=20, text="Information",
                               fg="black", font=("arial", 16, "bold"))
    DataFrameLeft.place(x=0, y=5, width=900, height=355)

    # textfield and entry for dataframe in left
    # refrence no
    Refno = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Reference no",fg='white', bg="maroon", padx=2, pady=6)
    Refno.grid(row=0, column=0, sticky=W)
    Refno_entry = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
    Refno_entry.grid(row=0, column=1)
    # company/costumer name
    Bookname = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Book name",fg='white', bg="maroon", padx=2, pady=6)
    Bookname.grid(row=1, column=0, sticky=W)
    Bookname_entry = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
    Bookname_entry.grid(row=1, column=1)
    # medicine type
    Mem_type = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Member Type", bg="maroon",fg='white', padx=2, pady=6)
    Mem_type.grid(row=2, column=0, sticky=W)
    MemType_combo = ttk.Combobox(DataFrameLeft, width=27, font=("arial", 10, "bold"), state="readonly")
    MemType_combo["values"] = ("Temporary", "Permanent", "Staff")
    MemType_combo.grid(row=2, column=1)
    MemType_combo.current(0)
    # medicine name
    BookG = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Book Genre", bg="maroon",fg='white', padx=2, pady=6)
    BookG.grid(row=3, column=0, sticky=W)
    BookG_entry = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
    BookG_entry.grid(row=3, column=1)
    # lot no
    Address = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Address ", bg="maroon",fg='white', padx=2, pady=6)
    Address.grid(row=4, column=0, sticky=W)
    Address_entry = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
    Address_entry.grid(row=4, column=1)
    # issue date
    Issue_date = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Issue Date", bg="maroon",fg='white', padx=2, pady=6)
    Issue_date.grid(row=5, column=0, sticky=W)
    Issue_entry = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
    Issue_entry.grid(row=5, column=1)
    # expiry date
    Actualprice = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Actual Price", bg="maroon",fg='white', padx=2, pady=6)
    Actualprice.grid(row=6, column=0, sticky=W)
    Actual_entry = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
    Actual_entry.grid(row=6, column=1)
    # dosage
    Mobile = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Mobile Number", bg="maroon",fg='white', padx=2, pady=6)
    Mobile.grid(row=7, column=0, sticky=W)
    Mobile_entry = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
    Mobile_entry.grid(row=7, column=1)
    # tablets price
    Author = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Author", bg="maroon",fg='white', padx=2, pady=6)
    Author.grid(row=8, column=0, sticky=W)
    Author_entry = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
    Author_entry.grid(row=8, column=1)
    # precution and warning
    Post = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Post", bg="maroon",fg='white', padx=6, pady=6)
    Post.grid(row=0, column=3, sticky=W)
    Post_entry = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
    Post_entry.grid(row=0, column=4)
    # uses
    Dateo = Label(DataFrameLeft, font=("arial", 10, "bold"), text=" Date Overdue", bg="maroon",fg='white', padx=2, pady=6)
    Dateo.grid(row=1, column=3, sticky=W)
    Dateo_entry = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
    Dateo_entry.grid(row=1, column=4)
    # side effects
    Description = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Description", bg="maroon",fg='white', padx=2, pady=6)
    Description.grid(row=2, column=3, sticky=W)
    Description_entry = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
    Description_entry.grid(row=2, column=4)
    # dataframe Right
    DataFrameRight = LabelFrame(DataFrame, bd=10, bg="maroon", relief=RIDGE, padx=20, text="Edit Department",
                                fg="black", font=("arial", 16, "bold"))
    DataFrameRight.place(x=910, y=5, width=300, height=355)
    # edit buttons and refrence id entry on dataframe Right
    # buttons
    btnAddData = Button(DataFrameRight, text="Add Medicine", font=("arial", 12, "bold"), width=14, fg="white",
                        bg="darkgreen", padx=2, command=submit)
    btnAddData.grid(row=1, column=0, padx=3, pady=3)
    btnUpdate = Button(DataFrameRight, text="Update", font=("arial", 12, "bold"), width=14, fg="white", bg="darkgreen",
                       padx=2, command=edit)
    btnUpdate.grid(row=2, column=0, padx=3, pady=3)
    btnDelete = Button(DataFrameRight, text="Delete", font=("arial", 12, "bold"), width=14, fg="white", bg="darkred",
                       command=delete)
    btnDelete.grid(row=3, column=0, padx=3, pady=3)
    btnExit = Button(DataFrameRight, text="Exit", font=("arial", 12, "bold"), width=14, fg="white", bg="darkred",
                     command=exit_fun)
    btnExit.grid(row=5, column=0, padx=3, pady=3)
    # search entry
    txtsearch = Entry(DataFrameRight, bd=3, relief=RIDGE, width=14, font=("arial", 12, "bold"))
    txtsearch.grid(row=7, column=0, padx=3, pady=3)
    ShowAllbtn = Button(DataFrameRight, text="Show All", font=("arial", 12, "bold"), width=14, fg="white", bg="darkgreen",
                        command=query)
    ShowAllbtn.grid(row=9, column=0, padx=3, pady=3)
    # Details frame
    details_frame = Frame(root, bd=10, relief=RIDGE)
    details_frame.place(x=0, y=540, width=1279, height=200)
    # details and scrollbar
    sc_x = ttk.Scrollbar(details_frame, orient=HORIZONTAL)
    sc_x.pack(side=BOTTOM, fill=X)
    sc_y = ttk.Scrollbar(details_frame, orient=VERTICAL)
    sc_y.pack(side=RIGHT, fill=Y)
    sc_x.pack(side=BOTTOM, fill=X)
    sc_y.pack(side=RIGHT, fill=Y)
    mainloop()