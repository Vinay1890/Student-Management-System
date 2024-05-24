from time import strftime
from tkinter import *
import pandas
import ttkthemes
from tkinter import ttk, messagebox,filedialog
import pymysql

count = 0
text = ''
s = 'Student Management System'

def export_data():
    url=filedialog.asksaveasfilename(defaultextension='csv')
    indexing=studentTable.get_children()
    newlist=[]
    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)


    table=pandas.DataFrame(newlist,columns=['id','Name','Mobile_No','Email','Address','Gender','DOB','Added_Date','Added_Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is Saved successfuly')





def update_student():
    def update_data():
        if idEntry.get() == '':
            messagebox.showerror('Error', 'Please enter the ID of the student to update', parent=update_window)
        else:
            query = 'UPDATE student SET Name=%s, Mobile_No=%s, Email=%s, Address=%s, Gender=%s, DOB=%s WHERE Id=%s'
            mycursor.execute(query, (
                NameEntry.get(), Mobile_NoEntry.get(), EmailEntry.get(), AddressEntry.get(),
                GenderEntry.get(), DOBEntry.get(), idEntry.get()))
            con.commit()
            messagebox.showinfo('Success', 'Student record updated successfully', parent=update_window)
            update_window.destroy()
            update_student()

    update_window = Toplevel()
    update_window.title('Update student')
    update_window.grab_set()
    update_window.resizable(False, False)
    idLabel = Label(update_window, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(update_window, font=('roman', 20, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    NameLabel = Label(update_window, text='Name', font=('times new roman', 20, 'bold'))
    NameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    NameEntry = Entry(update_window, font=('roman', 20, 'bold'), width=24)
    NameEntry.grid(row=1, column=1, pady=15, padx=10)

    Mobile_NoLabel = Label(update_window, text='Mobile No', font=('times new roman', 20, 'bold'))
    Mobile_NoLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    Mobile_NoEntry = Entry(update_window, font=('roman', 20, 'bold'), width=24)
    Mobile_NoEntry.grid(row=2, column=1, pady=15, padx=10)

    EmailLabel = Label(update_window, text='Email', font=('times new roman', 20, 'bold'))
    EmailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    EmailEntry = Entry(update_window, font=('roman', 20, 'bold'), width=24)
    EmailEntry.grid(row=3, column=1, pady=15, padx=10)

    AddressLabel = Label(update_window, text='Address', font=('times new roman', 20, 'bold'))
    AddressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    AddressEntry = Entry(update_window, font=('roman', 20, 'bold'), width=24)
    AddressEntry.grid(row=4, column=1, pady=15, padx=10)

    GenderLabel = Label(update_window, text='Gender', font=('times new roman', 20, 'bold'))
    GenderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    GenderEntry = Entry(update_window, font=('roman', 20, 'bold'), width=24)
    GenderEntry.grid(row=5, column=1, pady=15, padx=10)

    DOBLabel = Label(update_window, text='DOB', font=('times new roman', 20, 'bold'))
    DOBLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    DOBEntry = Entry(update_window, font=('roman', 20, 'bold'), width=24)
    DOBEntry.grid(row=6, column=1, pady=15, padx=10)

    update_student_button = ttk.Button(update_window, text='UPDATE', command=update_data)
    update_student_button.grid(row=7, columnspan=2, pady=15)

    indexing = studentTable.focus()

    content = studentTable.item(indexing)
    listdata = content['values']
    idEntry.insert(0, listdata[0])
    NameEntry.insert(0, listdata[1])
    Mobile_NoEntry.insert(0, listdata[2])
    EmailEntry.insert(0, listdata[3])
    AddressEntry.insert(0, listdata[4])
    GenderEntry.insert(0, listdata[5])
    DOBEntry.insert(0, listdata[6])

def delete_student():
    selected_item = studentTable.focus()
    if selected_item:
        content = studentTable.item(selected_item)
        content_id = content['values'][0]
        query = 'DELETE FROM student WHERE Id=%s'
        mycursor.execute(query, (content_id,))
        con.commit()
        messagebox.showinfo('Deleted', 'Student record deleted successfully')
        show_student()
    else:
        messagebox.showerror('Error', 'Please select a student record to delete')

def show_student():
    query = 'SELECT * FROM student'
    mycursor.execute(query)
    studentTable.delete(*studentTable.get_children())
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('', END, values=data)


def search_student():
    def search_data():
        query = 'SELECT * FROM student WHERE Id=%s OR Name=%s OR Mobile_No=%s OR Email=%s OR Address=%s OR Gender=%s OR DOB=%s'
        mycursor.execute(query, (idEntry.get(), NameEntry.get(), Mobile_NoEntry.get(), EmailEntry.get(), AddressEntry.get(), GenderEntry.get(), DOBEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data = mycursor.fetchall()
        for data in fetched_data:
            studentTable.insert('', END, values=data)

    search_window = Toplevel()
    search_window.title('Search student')
    search_window.grab_set()
    search_window.resizable(False, False)
    idLabel = Label(search_window, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(search_window, font=('roman', 20, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    NameLabel = Label(search_window, text='Name', font=('times new roman', 20, 'bold'))
    NameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    NameEntry = Entry(search_window, font=('roman', 20, 'bold'), width=24)
    NameEntry.grid(row=1, column=1, pady=15, padx=10)

    Mobile_NoLabel = Label(search_window, text='Mobile No', font=('times new roman', 20, 'bold'))
    Mobile_NoLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    Mobile_NoEntry = Entry(search_window, font=('roman', 20, 'bold'), width=24)
    Mobile_NoEntry.grid(row=2, column=1, pady=15, padx=10)

    EmailLabel = Label(search_window, text='Email', font=('times new roman', 20, 'bold'))
    EmailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    EmailEntry = Entry(search_window, font=('roman', 20, 'bold'), width=24)
    EmailEntry.grid(row=3, column=1, pady=15, padx=10)

    AddressLabel = Label(search_window, text='Address', font=('times new roman', 20, 'bold'))
    AddressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    AddressEntry = Entry(search_window, font=('roman', 20, 'bold'), width=24)
    AddressEntry.grid(row=4, column=1, pady=15, padx=10)

    GenderLabel = Label(search_window, text='Gender', font=('times new roman', 20, 'bold'))
    GenderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    GenderEntry = Entry(search_window, font=('roman', 20, 'bold'), width=24)
    GenderEntry.grid(row=5, column=1, pady=15, padx=10)

    DOBLabel = Label(search_window, text='DOB', font=('times new roman', 20, 'bold'))
    DOBLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    DOBEntry = Entry(search_window, font=('roman', 20, 'bold'), width=24)
    DOBEntry.grid(row=6, column=1, pady=15, padx=10)

    search_student_button = ttk.Button(search_window, text='Search STUDENT', command=search_data)
    search_student_button.grid(row=7, columnspan=2, pady=15)

def add_student():
    def add_data():
        if idEntry.get() == '' or NameEntry.get() == '' or Mobile_NoEntry.get() == '' or EmailEntry.get() == '' or AddressEntry.get() == '' or GenderEntry.get() == '' or DOBEntry.get() == '':
            messagebox.showerror('Error', 'All Fields are required', parent=add_window)
        else:
            currentdate = strftime('%d/%m/%Y')
            currenttime = strftime('%H:%M:%S')
            query = 'INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            mycursor.execute(query, (
                idEntry.get(), NameEntry.get(), Mobile_NoEntry.get(), EmailEntry.get(), AddressEntry.get(), GenderEntry.get(),
                DOBEntry.get(), currentdate, currenttime))
            con.commit()
            result = messagebox.askyesno('Confirm', 'Data added successfully. Do you want to clean the form?', parent=add_window)
            if result:
                idEntry.delete(0, END)
                NameEntry.delete(0, END)
                Mobile_NoEntry.delete(0, END)
                EmailEntry.delete(0, END)
                AddressEntry.delete(0, END)
                GenderEntry.delete(0, END)
                DOBEntry.delete(0, END)
            else:
                add_window.destroy()

    add_window = Toplevel()
    add_window.title('Add student')
    add_window.grab_set()
    add_window.resizable(False, False)
    idLabel = Label(add_window, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(add_window, font=('roman', 20, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    NameLabel = Label(add_window, text='Name', font=('times new roman', 20, 'bold'))
    NameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    NameEntry = Entry(add_window, font=('roman', 20, 'bold'), width=24)
    NameEntry.grid(row=1, column=1, pady=15, padx=10)

    Mobile_NoLabel = Label(add_window, text='Mobile No', font=('times new roman', 20, 'bold'))
    Mobile_NoLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    Mobile_NoEntry = Entry(add_window, font=('roman', 20, 'bold'), width=24)
    Mobile_NoEntry.grid(row=2, column=1, pady=15, padx=10)

    EmailLabel = Label(add_window, text='Email', font=('times new roman', 20, 'bold'))
    EmailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    EmailEntry = Entry(add_window, font=('roman', 20, 'bold'), width=24)
    EmailEntry.grid(row=3, column=1, pady=15, padx=10)

    AddressLabel = Label(add_window, text='Address', font=('times new roman', 20, 'bold'))
    AddressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    AddressEntry = Entry(add_window, font=('roman', 20, 'bold'), width=24)
    AddressEntry.grid(row=4, column=1, pady=15, padx=10)

    GenderLabel = Label(add_window, text='Gender', font=('times new roman', 20, 'bold'))
    GenderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    GenderEntry = Entry(add_window, font=('roman', 20, 'bold'), width=24)
    GenderEntry.grid(row=5, column=1, pady=15, padx=10)

    DOBLabel = Label(add_window, text='DOB', font=('times new roman', 20, 'bold'))
    DOBLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    DOBEntry = Entry(add_window, font=('roman', 20, 'bold'), width=24)
    DOBEntry.grid(row=6, column=1, pady=15, padx=10)

    add_student_button = ttk.Button(add_window, text='Add STUDENT', command=add_data)
    add_student_button.grid(row=7, columnspan=2, pady=15)

def connect_database():
    def connect():
        global mycursor, con
        try:
            con = pymysql.connect(host=hostEntry.get(), user=userEntry.get(), password=passwordEntry.get())
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Invalid Details', parent=connect_window)
            return
        try:
            query = 'CREATE DATABASE studentmanagementsystem'
            mycursor.execute(query)
            query = 'USE studentmanagementsystem'
            mycursor.execute(query)
            query = 'CREATE TABLE student(Id int NOT NULL PRIMARY KEY, Name varchar(30), Mobile_No varchar(10), Email varchar(30), Address varchar(100), Gender varchar(10), DOB varchar(20), Added_Date varchar(20), Added_Time varchar(20))'
            mycursor.execute(query)
        except:
            query = 'USE studentmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection is successful', parent=connect_window)
        connect_window.destroy()
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)
        exitstudentButton.config(state=NORMAL)

    connect_window = Toplevel()
    connect_window.title('Database Connection')
    connect_window.grab_set()
    connect_window.resizable(False, False)
    hostLabel = Label(connect_window, text='Host Name', font=('arial', 20, 'bold'))
    hostLabel.grid(row=0, column=0, padx=20)
    hostEntry = Entry(connect_window, font=('roman', 15, 'bold'), bd=2)
    hostEntry.grid(row=0, column=1, padx=40, pady=20)

    userLabel = Label(connect_window, text='User Name', font=('arial', 20, 'bold'))
    userLabel.grid(row=1, column=0, padx=20)
    userEntry = Entry(connect_window, font=('roman', 15, 'bold'), bd=2)
    userEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connect_window, text='Password', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)
    passwordEntry = Entry(connect_window, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton = ttk.Button(connect_window, text='Connect', command=connect)
    connectButton.grid(row=3, columnspan=2)

def exit_student():
    result = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if result:
        sms_window.destroy()
    else:
        pass

def update_clock():
    global datetimeLabel
    time_string = strftime('%H:%M:%S %p')
    date_string = strftime('%d/%m/%Y')
    datetimeLabel.config(text=f'Date: {date_string}\nTime: {time_string}')
    datetimeLabel.after(1000, update_clock)

def slider():
    global count, text
    if count == len(s):
        count = 0
        text = ''
    text += s[count]
    count += 1
    sliderLabel.config(text=text)
    sliderLabel.after(150, slider)

def open_sms_window():
    global datetimeLabel, sliderLabel, sms_window
    global addstudentButton, searchstudentButton, updatestudentButton
    global deletestudentButton, showstudentButton, exportstudentButton, exitstudentButton
    global studentTable

    sms_window = ttkthemes.ThemedTk()
    sms_window.get_themes()
    sms_window.set_theme('radiance')
    sms_window.geometry('1174x680+0+0')
    sms_window.title('Student Management System')

    datetimeLabel = Label(sms_window, font=('times new roman', 18, 'bold'))
    datetimeLabel.place(x=5, y=5)
    update_clock()

    sliderLabel = Label(sms_window, font=("times new roman", 18, 'bold'))
    sliderLabel.place(x=280, y=0)
    slider()

    connectButton = ttk.Button(sms_window, text='Connect Database', command=connect_database)
    connectButton.place(x=980, y=0)

    leftFrame = Frame(sms_window)
    leftFrame.place(x=50, y=80, width=300, height=600)

    logo_image = PhotoImage(file='student (1).png')
    logo_Label = Label(leftFrame, image=logo_image)
    logo_Label.grid(row=0, column=0)

    addstudentButton = ttk.Button(leftFrame, text="Add Student", width=25, state=DISABLED, command=add_student)
    addstudentButton.grid(row=1, column=0, pady=20)

    searchstudentButton = ttk.Button(leftFrame, text="Search Student", width=25, state=DISABLED, command=search_student)
    searchstudentButton.grid(row=2, column=0, pady=20)

    updatestudentButton = ttk.Button(leftFrame, text="Update Student", width=25, state=DISABLED, command=update_student)
    updatestudentButton.grid(row=3, column=0, pady=20)

    deletestudentButton = ttk.Button(leftFrame, text="Delete Student", width=25, state=DISABLED, command=delete_student)
    deletestudentButton.grid(row=4, column=0, pady=20)

    showstudentButton = ttk.Button(leftFrame, text="Show Student", width=25, state=DISABLED, command=show_student)
    showstudentButton.grid(row=5, column=0, pady=20)

    exportstudentButton = ttk.Button(leftFrame, text="Export Data", width=25, state=DISABLED,command=export_data)
    exportstudentButton.grid(row=6, column=0, pady=20)

    exitstudentButton = ttk.Button(leftFrame, text="Exit", width=25, state=DISABLED, command=exit_student)
    exitstudentButton.grid(row=7, column=0, pady=20)

    rightFrame = Frame(sms_window)
    rightFrame.place(x=350, y=80, width=820, height=600)

    scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
    scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)

    studentTable = ttk.Treeview(rightFrame, columns=('Id', 'Name', 'Mobile No', 'Email', 'Address', 'Gender', 'D.O.B', 'Added Date', 'Added Time'),
                                xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

    scrollBarX.config(command=studentTable.xview)
    scrollBarY.config(command=studentTable.yview)

    scrollBarX.pack(side=BOTTOM, fill=X)
    scrollBarY.pack(side=RIGHT, fill=Y)

    studentTable.pack(fill=BOTH, expand=1)

    studentTable.heading('Id', text='Id')
    studentTable.heading('Name', text='Name')
    studentTable.heading('Mobile No', text='Mobile No')
    studentTable.heading('Email', text='Email')
    studentTable.heading('Address', text='Address')
    studentTable.heading('Gender', text='Gender')
    studentTable.heading('D.O.B', text='D.O.B')
    studentTable.heading('Added Date', text='Added Date')
    studentTable.heading('Added Time', text='Added Time')

    studentTable.column('Id', width=100, anchor=CENTER)
    studentTable.column('Name', width=200, anchor=CENTER)
    studentTable.column('Mobile No', width=200, anchor=CENTER)
    studentTable.column('Email', width=300, anchor=CENTER)
    studentTable.column('Address', width=200, anchor=CENTER)
    studentTable.column('Gender', width=100, anchor=CENTER)
    studentTable.column('D.O.B', width=150, anchor=CENTER)
    studentTable.column('Added Date', width=150, anchor=CENTER)
    studentTable.column('Added Time', width=150, anchor=CENTER)

    style = ttk.Style()
    style.configure('Treeview', rowheight=40, font=('arial', 12, 'bold'), foreground='black', background='white')
    style.configure('Treeview.Heading', font=('arial', 14, 'bold'), foreground='black')

    studentTable.config(show='headings')
    sms_window.mainloop()

open_sms_window()
