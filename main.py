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
            company_name text,
            med_type text,
            med_name text,
            lot_no integer,
            issue_date integer,
            expiry_date integer,
            dosage integer,
            tab_price integer,
            precs_warning text,
            uses text,
            side_effects text
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
            "INSERT INTO addresses VALUES (:ref_no, :company_name, :med_name, :med_type, :lot_no, :issue_date, :expiry_date, :dosage, :tab_price, :precs_warning, :uses, :side_effects)",
            {
                'ref_no': Refno_entry.get(),
                'company_name': Company_entry.get(),
                'med_type': MedType_combo.get(),
                'med_name': Medname_entry.get(),
                'lot_no': Lot_entry.get(),
                'issue_date': Issue_entry.get(),
                'expiry_date': Expiry_entry.get(),
                'dosage': Dosage_entry.get(),
                'tab_price': Tablets_entry.get(),
                'precs_warning': Precs_entry.get(),
                'uses': Uses_entry.get(),
                'side_effects': Sideeffects_entry.get()
            })
        conn.commit()
        conn.close()
        # clear the text boxes
        Refno_entry.delete(0, END)
        Company_entry.delete(0, END)
        MedType_combo.delete(0, END)
        Medname_entry.delete(0, END)
        Lot_entry.delete(0, END)
        Issue_entry.delete(0, END)
        Expiry_entry.delete(0, END)
        Dosage_entry.delete(0, END)
        Tablets_entry.delete(0, END)
        Precs_entry.delete(0, END)
        Uses_entry.delete(0, END)
        Sideeffects_entry.delete(0, END)
        messagebox.showinfo("Medicine added", "MEDICINE ADDED SUCCESSFULLY")
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
        global Company_editor
        global med_type_editor
        global med_name_editor
        global lot_no_editor
        global issue_editor
        global dosage_editor
        global tab_price_editor
        global precs_editor
        global uses_editor
        global side_effects_editor
        # Creating an update function
        def update():
            # Create a databases or connect to one
            conn = sqlite3.connect('address_book1.db')
            # Create cursor
            c = conn.cursor()
            record_id = txtsearch.get()
            c.execute(""" UPDATE addresses SET
                 ref_no = :ref,
                 company_name = :company,
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
                       'company': Company_editor.get(),
                       'med_t': med_type_editor.get(),
                       'med_n': med_name_editor.get(),
                       'lot': lot_no_editor.get(),
                       'issue': issue_editor.get(),
                       'expiry': expiry_editor.get(),
                       'dos': dosage_editor.get(),
                       'tab_p': tab_price_editor.get(),
                       'precs': precs_editor.get(),
                       'use': uses_editor.get(),
                       'side': side_effects_editor.get(),
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
        Company_editor = Entry(editor, width=30)
        Company_editor.grid(row=1, column=1, padx=20, pady=(10, 0))
        med_type_editor = Entry(editor, width=30)
        med_type_editor.grid(row=2, column=1, padx=20, pady=(10, 0))
        med_name_editor = Entry(editor, width=30)
        med_name_editor.grid(row=3, column=1, padx=20, pady=(10, 0))
        lot_no_editor = Entry(editor, width=30)
        lot_no_editor.grid(row=4, column=1, padx=20, pady=(10, 0))
        issue_editor = Entry(editor, width=30)
        issue_editor.grid(row=5, column=1, padx=20, pady=(10, 0))
        expiry_editor = Entry(editor, width=30)
        expiry_editor.grid(row=6, column=1, padx=20, pady=(10, 0))
        dosage_editor = Entry(editor, width=30)
        dosage_editor.grid(row=7, column=1, padx=20, pady=(10, 0))
        tab_price_editor = Entry(editor, width=30)
        tab_price_editor.grid(row=8, column=1, padx=20, pady=(10, 0))
        precs_editor = Entry(editor, width=30)
        precs_editor.grid(row=9, column=1, padx=20, pady=(10, 0))
        uses_editor = Entry(editor, width=30)
        uses_editor.grid(row=10, column=1, padx=20, pady=(10, 0))
        side_effects_editor = Entry(editor, width=30)
        side_effects_editor.grid(row=11, column=1, padx=20, pady=(10, 0))
        # Create textbox labels
        ref_no_label = Label(editor, text="Refrence no")
        ref_no_label.grid(row=0, column=0, pady=(10, 0))
        Company_label = Label(editor, text="Company/Customer Name")
        Company_label.grid(row=1, column=0)
        med_type_label = Label(editor, text="Medicine Type")
        med_type_label.grid(row=2, column=0)
        med_name_label = Label(editor, text="Medicine Type")
        med_name_label.grid(row=3, column=0)
        lot_no_label = Label(editor, text="Lot no.")
        lot_no_label.grid(row=4, column=0)
        issue_label = Label(editor, text="Issue Date.")
        issue_label.grid(row=5, column=0)
        expiry_label = Label(editor, text="Expiry Date")
        expiry_label.grid(row=6, column=0)
        dosage_label = Label(editor, text="Dosage")
        dosage_label.grid(row=7, column=0)
        tab_price_label = Label(editor, text="Tablets price")
        tab_price_label.grid(row=8, column=0)
        precs_label = Label(editor, text="Precs & Warning")
        precs_label.grid(row=9, column=0)
        uses_label = Label(editor, text=" Uses")
        uses_label.grid(row=10, column=0)
        side_effects_label = Label(editor, text=" Side Effects")
        side_effects_label.grid(row=11, column=0)
        # loop through the results
        for record in records:
            ref_no_editor.insert(0, record[0])
            Company_editor.insert(0, record[1])
            med_type_editor.insert(0, record[2])
            med_name_editor.insert(0, record[3])
            lot_no_editor.insert(0, record[4])
            issue_editor.insert(0, record[5])
            expiry_editor.insert(0, record[6])
            dosage_editor.insert(0, record[7])
            tab_price_editor.insert(0, record[8])
            precs_editor.insert(0, record[9])
            uses_editor.insert(0, record[10])
            side_effects_editor.insert(0, record[11])
        # Create a update button
        edit_btn = Button(editor, text=" SAVE ", command=update)
        edit_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=125)
    def exit_fun():
        ask = messagebox.askyesno("exit", "Do you want to exit?")
        if ask == 1:
            root.destroy()


    root = Toplevel()
    root.title("Pharmacy Management System")
    root.iconbitmap('pill.png')
    root.geometry("1280x680")
    # top title
    title = Label(root, text="Pharmacy Management System", bg="black", fg="red", font=("Bradley Hand ITC", 50, "bold"))
    title.pack(side=TOP, fill=X, padx=10, pady=10)
    # logo image
    img1 = Image.open("logo.png")
    img1 = img1.resize((80, 80), Image.ANTIALIAS)
    photoimg1 = ImageTk.PhotoImage(img1)
    btn = Button(root, image=photoimg1, borderwidth=0)
    btn.place(x=40, y=14)
    # dataframe
    DataFrame = Frame(root, bd=10, bg="black", relief=RIDGE, padx=20, pady=20)
    DataFrame.place(x=0, y=110, width=1280, height=420)
    # dataframe left
    DataFrameLeft = LabelFrame(DataFrame, bd=10, bg="lightblue", relief=RIDGE, padx=20, text="Medicine Information",
                               fg="black", font=("arial", 16, "bold"))
    DataFrameLeft.place(x=0, y=5, width=900, height=355)
    # images in left dataframe
    img2 = Image.open("tab.png")
    img2 = img2.resize((100, 80), Image.ANTIALIAS)
    photoimg2 = ImageTk.PhotoImage(img2)
    btn = Button(root, image=photoimg2, borderwidth=0)
    btn.place(x=800, y=177)
    img3 = Image.open("doc.png")
    img3 = img3.resize((430, 200), Image.ANTIALIAS)
    photoimg3 = ImageTk.PhotoImage(img3)
    btn = Button(root, image=photoimg3, borderwidth=0)
    btn.place(x=470, y=270)
    # images in right dataframe
    img4 = Image.open("abc.png")
    img4 = img4.resize((70, 120), Image.ANTIALIAS)
    photoimg4 = ImageTk.PhotoImage(img4)
    btn = Button(root, image=photoimg4, borderwidth=0)
    btn.place(x=1140, y=200)
    img5 = Image.open("123.png")
    img5 = img5.resize((70, 80), Image.ANTIALIAS)
    photoimg5 = ImageTk.PhotoImage(img5)
    btn = Button(root, image=photoimg5, borderwidth=0)
    btn.place(x=1140, y=387)
    # textfield and entry for dataframe in left
    # refrence no
    Refno = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Reference no", bg="lightblue", padx=2, pady=6)
    Refno.grid(row=0, column=0, sticky=W)
    Refno_entry = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
    Refno_entry.grid(row=0, column=1)
    # company/costumer name
    Company = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Company/Customer Name", bg="lightblue", padx=2, pady=6)
    Company.grid(row=1, column=0, sticky=W)
    Company_entry = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
    Company_entry.grid(row=1, column=1)
    # medicine type
    Med_type = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Medicine Type", bg="lightblue", padx=2, pady=6)
    Med_type.grid(row=2, column=0, sticky=W)
    MedType_combo = ttk.Combobox(DataFrameLeft, width=27, font=("arial", 10, "bold"), state="readonly")
    MedType_combo["values"] = ("Tablet", "Liquid", "Capsules", "Drops", "Inhales", "Injection")
    MedType_combo.grid(row=2, column=1)
    MedType_combo.current(0)
    # medicine name
    Med_name = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Medicine Name", bg="lightblue", padx=2, pady=6)
    Med_name.grid(row=3, column=0, sticky=W)
    Medname_entry = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
    Medname_entry.grid(row=3, column=1)
    # lot no
    LotNo = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Lot no.", bg="lightblue", padx=2, pady=6)
    LotNo.grid(row=4, column=0, sticky=W)
    Lot_entry = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
    Lot_entry.grid(row=4, column=1)
    # issue date
    Issue_date = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Issue Date", bg="lightblue", padx=2, pady=6)
    Issue_date.grid(row=5, column=0, sticky=W)
    Issue_entry = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
    Issue_entry.grid(row=5, column=1)
    # expiry date
    Expiry_date = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Expiry Date", bg="lightblue", padx=2, pady=6)
    Expiry_date.grid(row=6, column=0, sticky=W)
    Expiry_entry = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
    Expiry_entry.grid(row=6, column=1)
    # dosage
    Dosage = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Dosage", bg="lightblue", padx=2, pady=6)
    Dosage.grid(row=7, column=0, sticky=W)
    Dosage_entry = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
    Dosage_entry.grid(row=7, column=1)
    # tablets price
    Tablets_price = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Tablets Price", bg="lightblue", padx=2, pady=6)
    Tablets_price.grid(row=8, column=0, sticky=W)
    Tablets_entry = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
    Tablets_entry.grid(row=8, column=1)
    # precution and warning
    Precs_Warning = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Precs & Warning", bg="lightblue", padx=6, pady=6)
    Precs_Warning.grid(row=0, column=3, sticky=W)
    Precs_entry = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
    Precs_entry.grid(row=0, column=4)
    # uses
    Uses = Label(DataFrameLeft, font=("arial", 10, "bold"), text=" Uses", bg="lightblue", padx=2, pady=6)
    Uses.grid(row=1, column=3, sticky=W)
    Uses_entry = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
    Uses_entry.grid(row=1, column=4)
    # side effects
    Sideeffects = Label(DataFrameLeft, font=("arial", 10, "bold"), text=" Side Effects", bg="lightblue", padx=2, pady=6)
    Sideeffects.grid(row=2, column=3, sticky=W)
    Sideeffects_entry = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
    Sideeffects_entry.grid(row=2, column=4)
    # dataframe Right
    DataFrameRight = LabelFrame(DataFrame, bd=10, bg="lightblue", relief=RIDGE, padx=20, text="Medicine Edit Department",
                                fg="darkgreen", font=("arial", 16, "bold"))
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