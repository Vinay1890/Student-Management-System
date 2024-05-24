from time import strftime
from tkinter import *
import ttkthemes
from tkinter import ttk, messagebox
import pymysql

count = 0
text = ''
s = 'Student Management System'




    indexing=studentTable.focus()

    content=studentTable.item(indexing)
    listdata=content['values']
    idEntry.insert(0,listdata[0])
    NameEntry.insert(0,listdata[1])
    Mobile_NoEntry.insert(0,listdata[2])
    EmailEntry.insert(0,listdata[3])
    AddressEntry.insert(0,listdata[4])
    GenderEntry.insert(0,listdata[5])
    DOBEntry.insert(0,listdata[6])

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
                idEntry.get(), NameEntry.get(), Mobile_NoEntry.get(), EmailEntry.get(), AddressEntry.get(),
                GenderEntry.get(), DOBEntry.get(), currentdate, currenttime))
            con.commit()
            result = messagebox.askyesno('Confirm', 'Data added successfully. Do you want to clear the form?',
                                         parent=add_window)
            if result:
                idEntry.delete(0, END)
                NameEntry.delete(0, END)
                Mobile_NoEntry.delete(0, END)
                EmailEntry.delete(0, END)
                AddressEntry.delete(0, END)
                GenderEntry.delete(0, END)
                DOBEntry.delete(0, END)

            query = 'SELECT * FROM student'
            mycursor.execute(query)
            fetched_data = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())

            # Insert new data
            for data in fetched_data:
                datalist = list(data)
                studentTable.insert('', END, values=datalist)

    add_window = Toplevel()
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

    add_student_button = ttk.Button(add_window, text='ADD STUDENT', command=add_data)
    add_student_button.grid(row=7, columnspan=2, pady=15)

def connect_database():
    global mycursor, con

    # Using predefined connection details
    host = "localhost"
    user = "root"
    password = "UP44AX9857"

    try:
        con = pymysql.connect(host=host, user=user, password=password)
        mycursor = con.cursor()
        messagebox.showinfo('Success', 'Database Connection is successful')
        create_database_and_table()
        enable_buttons()
    except pymysql.MySQLError as e:
        messagebox.showerror('Error', f'Error connecting to the database: {e}')
        print(f"MySQLError: {e}")
    except Exception as e:
        messagebox.showerror('Error', f'An unexpected error occurred: {e}')
        print(f"Exception: {e}")

def create_database_and_table():
    try:
        mycursor.execute('CREATE DATABASE IF NOT EXISTS studentmanagementsystem')
        mycursor.execute('USE studentmanagementsystem')
        mycursor.execute('''
            CREATE TABLE IF NOT EXISTS student (
                Id INT NOT NULL PRIMARY KEY, 
                Name VARCHAR(30), 
                Mobile_No VARCHAR(10), 
                Email VARCHAR(30), 
                Address VARCHAR(100), 
                Gender VARCHAR(30), 
                DOB VARCHAR(20), 
                Added_Date VARCHAR(50), 
                Added_Time VARCHAR(20)
            )
        ''')
        messagebox.showinfo('Success', 'Database and table are ready.')
    except pymysql.MySQLError as e:
        messagebox.showerror('Error', f'Error creating the database or table: {e}')
        print(f"MySQLError: {e}")
    except Exception as e:
        messagebox.showerror('Error', f'An unexpected error occurred: {e}')
        print(f"Exception: {e}")

def enable_buttons():
    addstudentButton.config(state=NORMAL)
    searchstudentButton.config(state=NORMAL)
    updatestudentButton.config(state=NORMAL)
    deletestudentButton.config(state=NORMAL)
    showstudentButton.config(state=NORMAL)
    exportstudentButton.config(state=NORMAL)
    exitstudentButton.config(state=NORMAL)

def slider():
    global text, count
    if count >= len(s):
        count = 0
        text = ''
    else:
        text = text + s[count]
        count += 1
    sliderLabel.config(text=text)
    sliderLabel.after(300, slider)

def update_clock():
    date = strftime('%d/%m/%Y')
    currenttime = strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000, update_clock)

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

    updatestudentButton = ttk.Button(leftFrame, text="Update Student", width=25, state=DISABLED)
    updatestudentButton.grid(row=3, column=0, pady=20,command=update_student)

    deletestudentButton = ttk.Button(leftFrame, text="Delete Student", width=25, state=DISABLED, command=delete_student)
    deletestudentButton.grid(row=4, column=0, pady=20)

    showstudentButton = ttk.Button(leftFrame, text="Show Student", width=25, state=DISABLED, command=show_student)
    showstudentButton.grid(row=5, column=0, pady=20)

    exportstudentButton = ttk.Button(leftFrame, text="Export Data", width=25, state=DISABLED)
    exportstudentButton.grid(row=6, column=0, pady=20)

    exitstudentButton = ttk.Button(leftFrame, text="Exit", width=25, state=DISABLED)
    exitstudentButton.grid(row=7, column=0, pady=20)

    rightFrame = Frame(sms_window)
    rightFrame.place(x=350, y=80, width=820, height=600)

    scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
    scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)

    studentTable = ttk.Treeview(rightFrame,
                                columns=('Id', 'Name', 'Mobile_No', 'Email', 'Address', 'Gender', 'DOB', 'Added_Date',
                                         'Added_Time'),
                                xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

    scrollBarX.config(command=studentTable.xview)
    scrollBarY.config(command=studentTable.yview)

    scrollBarX.pack(side=BOTTOM, fill=X)
    scrollBarY.pack(side=RIGHT, fill=Y)

    studentTable.pack(fill=BOTH, expand=1)

    studentTable.heading('Id', text='Id')
    studentTable.heading('Name', text='Name')
    studentTable.heading('Mobile_No', text='Mobile No')
    studentTable.heading('Email', text='Email')
    studentTable.heading('Address', text='Address')
    studentTable.heading('Gender', text='Gender')
    studentTable.heading('DOB', text='DOB')
    studentTable.heading('Added_Date', text='Added Date')
    studentTable.heading('Added_Time', text='Added Time')

    studentTable.column('Id',width=50,anchor=CENTER)
    studentTable.column('Name',width=300,anchor=CENTER)
    studentTable.column('Email',width=300,anchor=CENTER)
    studentTable.column('Mobile_No',width=200,anchor=CENTER)
    studentTable.column('Address',width=300,anchor=CENTER)
    studentTable.column('Gender',width=100,anchor=CENTER)
    studentTable.column('DOB',width=400,anchor=CENTER)
    studentTable.column('Added_Date',width=400,anchor=CENTER)
    studentTable.column('Added_Time',width=400,anchor=CENTER)

    style=ttk.Style()

    style.configure('Treeview',rowheight=40,font=('arial',12,'bold'),background='white',fieldbackround='white')
    style.configure('Treeview.Hedaing',font=('arial',14,'bold'),foreground='red')


    studentTable.config(show='headings')

    sms_window.mainloop()

if __name__ == '__main__':
    open_sms_window()
