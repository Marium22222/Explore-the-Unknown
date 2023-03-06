import mysql.connector
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import time



m=Tk()

# clockcode1
def tick():
    time_string=time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200,tick)

var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()

def new_window():
    m2=Tk()


    def inventory():
        for i in table2.get_children():
            table2.delete(i)
        mydb = mysql.connector.Connect(host="127.0.0.1",
                                       port="3306",
                                       user="root",
                                       auth_plugin="Native MYSQL Authentication",
                                       database="bookstore")
        cursor_1 = mydb.cursor()
        cursor_1.execute("select * from inventory")
        rows = cursor_1.fetchall()
        if rows:
            for i in rows:
                table2.insert('', END, values=i)
        mydb.close()




    #Heading label:
    label=Label(m2,bg="Dark Khaki",text="Welcome To Inventory",font=("Times New Roman",30))
    label.pack(side=TOP,fill=X)

    frame1= Frame(m2, bg="Pale Goldenrod")   #making a frame below heading
    frame1.place(x=150, y=120, width=900, height=520)
    button=Button(frame1,bg="Olive Drab",fg="White",font=("Times New Roman",14),width=5,height=22,bd=5,
                  text="S\nH\nO\nW\n\nI\nN\nV\nE\nN\nT\nO\nR\nY\n\nD\nE\nT\nA\nI\nL\nS",command=inventory)
    button.grid(row=1,column=0,padx=50,pady=15)
    frame2=Frame(m2)
    frame2.place(x=320,y=170,width=600,height=400)
    table2 = ttk.Treeview(frame2, height=1000, columns=('a', 'b', 'c', 'd', 'e'))
    table2.heading('a', text='BOOK ID')  # naming the columns
    table2.heading('b', text='BOOK NAME')
    table2.heading('c', text='QUANTITY')
    table2.heading('d', text='PURCHASED')
    table2.heading('e', text='BORROWED')
    table2.column('#0', minwidth=0, width=2, stretch=NO)
    table2.column('a', minwidth=0, width=100, stretch=NO)
    table2.column('b', minwidth=0, width=200, stretch=NO)
    table2.column('c', minwidth=0, width=100, stretch=NO)
    table2.column('d', minwidth=0, width=100, stretch=NO)
    table2.column('e', minwidth=0, width=100, stretch=NO)
    table2.pack()


def display():

    mydb = mysql.connector.Connect(host="127.0.0.1",
                                   port="3306",
                                   user="root",
                                   auth_plugin="Native MYSQL Authentication",
                                   database="bookstore")
    cursor_1 = mydb.cursor()
    cursor_1.execute("select * from books")
    rows = cursor_1.fetchall()
    if rows:
        for i in rows:
            large_table.insert('',END,values= i)
    mydb.close()

def details():
    for i in large_table.get_children():
        large_table.delete(i)
    mydb = mysql.connector.Connect(host="127.0.0.1",
                                   port="3306",
                                   user="root",
                                   auth_plugin="Native MYSQL Authentication",
                                   database="bookstore")
    cursor_1 = mydb.cursor()
    cursor_1.execute("select * from books")
    rows = cursor_1.fetchall()
    if rows:
        for i in rows:
            large_table.insert('',END,values= i)
    mydb.close()
def add():
    for i in large_table.get_children():
        large_table.delete(i)
    mydb= mysql.connector.Connect(host="127.0.0.1",
                                   port="3306",
                                   user="root",
                                   auth_plugin="Native MYSQL Authentication",
                                   database="bookstore")
    cursor1 = mydb.cursor()
    cursor1.execute(f"INSERT INTO books(book_id,book_name,author,price,genre,genre_id) values('{var1.get()}','{var2.get()}','{var3.get()}','{var4.get()}','{var5.get()}','{var6.get()}')")
    mydb.commit()
    display()
    messagebox.showinfo("One Book has been added to your Library!")
    mydb.close()
def delete():
    for i in large_table.get_children():
        large_table.delete(i)
    mydb = mysql.connector.Connect(host="127.0.0.1",
                                   port="3306",
                                   user="root",
                                   auth_plugin="Native MYSQL Authentication",
                                   database="bookstore")
    cursor1 = mydb.cursor()
    cursor1.execute((f"DELETE FROM books where book_id={var1.get()}"))
    mydb.commit()
    display()
    messagebox.showinfo("One Book has been deleted")
    mydb.close()
def update():
    for i in large_table.get_children():
        large_table.delete(i)
    mydb = mysql.connector.Connect(host="127.0.0.1",
                                   port="3306",
                                   user="root",
                                   auth_plugin="Native MYSQL Authentication",
                                   database="bookstore")
    cursor1 = mydb.cursor()
    cursor1.execute(f"UPDATE books set price={var4.get()} WHERE book_id={var1.get()}")
    mydb.commit()
    display()
    messagebox.showinfo("Library Has Been Updated!")
    mydb.close()

def category():
    for i in cat_table.get_children():
        cat_table.delete(i)
    mydb = mysql.connector.Connect(host="127.0.0.1",
                                   port="3306",
                                   user="root",
                                   auth_plugin="Native MYSQL Authentication",
                                   database="bookstore")
    cursor_1 = mydb.cursor()
    cursor_1.execute("select * from category")
    rows = cursor_1.fetchall()
    if rows:
        for i in rows:
            cat_table.insert('',END,values= i)
    mydb.close()

#putting background image in main window:
bg = PhotoImage(file="C:\\Users\\Amir\\Downloads\\my2.png")
# b_g=bg.subsample(3,3)
bg_label = Label(m,image=bg)
bg_label.place(x=0,y=0,width=1500,height=1200)
# clockcode
clock=Label(m,bg="yellow",font=("Algerian",25),bd=20)
clock.place(x=30,y=75,width=200,height=50)
tick()

#main heading
head_label=Label(m,text="EXPLORE THE UNKNOWN (Read More, Learn More)",fg="White",bg="gray19",font=('Times New Roman',30))
head_label.pack(side=TOP,fill=X)

#record-heading frames making
headingFrame1 = Frame(bg="Gray19", bd=5)
headingFrame1.place(relx=0.75, rely=0.1, relwidth=0.17, relheight=0.09)
headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)
headingLabel = Label(headingFrame2, text="Records", fg='black',font=('Times New Roman',20))
headingLabel.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.5)

record_frame=Frame(m,bg="Coral")                     #right side pink tab/frame below record-heading frame
record_frame.place(x=900,y=145,width=450,height=440)

#labels in record frame/ right side frame:
l1=Label(record_frame,text="Book ID",fg="White",bg="Gray28",width=15,bd=5).grid(row=1,column=0,padx=50,pady=20)
l2=Label(record_frame,text="Book Name",fg="White",bg="Gray28",width=15,bd=5).grid(row=1,column=1,padx=50,pady=10)
l3=Label(record_frame,text="Author",fg="White",bg="Gray28",width=15,bd=5).grid(row=3,column=0,padx=50,pady=10)
l4=Label(record_frame,text="Price",fg="White",bg="Gray28",width=15,bd=5).grid(row=3,column=1,padx=50,pady=10)
l5=Label(record_frame,text="Genre",fg="White",bg="Gray28",width=15,bd=5).grid(row=5,column=0,padx=50,pady=10)
l6=Label(record_frame,text="Genre ID",fg="White",bg="Gray28",width=15,bd=5).grid(row=5,column=1,padx=50,pady=10)

#entries below each label:
e1=Entry(record_frame,textvariable=var1,width=20,bg="White",fg="black",bd=5).grid(row=2,column=0,padx=50,pady=10)
e2=Entry(record_frame,textvariable=var2,width=20,bg="White",fg="black",bd=5).grid(row=2,column=1,padx=50,pady=10)
e3=Entry(record_frame,textvariable=var3,width=20,bg="White",fg="black",bd=5).grid(row=4,column=0,padx=50,pady=10)
e4=Entry(record_frame,textvariable=var4,width=20,bg="White",fg="black" ,bd=5).grid(row=4,column=1,padx=50,pady=10)
e5=Entry(record_frame,textvariable=var5,width=20,bg="White",fg="black" ,bd=5).grid(row=6,column=0,padx=50,pady=10)
e6=Entry(record_frame,textvariable=var6,width=20,bg="White",fg="black" ,bd=5).grid(row=6,column=1,padx=50,pady=10)

#buttons below labels and entries (inside record frame):
b1=Button(record_frame,text="Add Books",bg="Medium Purple1",fg="black",width=15,bd=5,command=add).grid(row=7,column=0,padx=50,pady=10)
b3=Button(record_frame,text="Update Library",bg="Medium Purple1",fg="black",width=15,bd=5,command=update).grid(row=7,column=1,padx=50,pady=10)
b4=Button(record_frame,text="Delete",bg="Medium Purple1",fg="black",width=15,bd=5,command=delete).grid(row=8,column=0,padx=50,pady=10)

#to the left-side at top we are making a frame in order to place button(VIEW BOOK DETAILS)
view_frame=Frame(m,bg="Dark Orange3")
view_frame.place(x=230,y=78,width=500,height=46)
v_btn=Button(view_frame,text="VIEW  ALL  BOOKS",font=('Times New Roman',15),bg="Dark Orange3",fg="White",width=44,height=1,bd=5,
             command=details).grid(row=6,column=0,padx=1,pady=1)

inv_btnframe=Frame(m)       #left-side frame in order to place button(INVENTORY)
inv_btnframe.place(x=4,y=150,width=107,height=59)
i_btn=Button(inv_btnframe,text="Inventory",font=('Times New Roman',12),bg="Dark Orange3",fg="White",width=10,height=2,bd=5,
             command=new_window).grid(row=10,column=0,padx=1,pady=1)

category_btnframe=Frame(m)   #left-side frame below inventory button in order to place button(CATEGORY)
category_btnframe.place(x=4,y=220,width=107,height=59)
c_btn=Button(category_btnframe,text="Categories",font=('Times New Roman',12),bg="Dark Orange3",fg="White",width=10,height=2,bd=5,
             command=category).grid(row=7,column=0,padx=1,pady=1)
# Making a Frame to display the details of categories:
cat_frame=Frame(m,bg="White")
cat_frame.place(x=7,y=290,width=107,height=150)
#making treeview for above category frame:
cat_table=ttk.Treeview(cat_frame,height=500,columns=('a','b'))
cat_table.heading('a',text='')      #naming the columns
cat_table.heading('b',text='GENRE')
#adjusting the widths of the columns
cat_table.column('#0', minwidth=0, width=0, stretch=NO)
cat_table.column('a', minwidth=0, width=0, stretch=NO)
cat_table.column('b', minwidth=0, width=100, stretch=NO)
cat_table.pack()

#making a large frame to the left below VIEW BOOKS DETAILS button to display the details of our books:
large_f=Frame(m,bg="White")
large_f.place(x=130,y=145,width=730,height=465)
#making a treeview for above large frame:
large_table=ttk.Treeview(large_f,height=2000,columns=('a','b','c','d','e','f','g'))
#naming the columns
large_table.heading('a',text='BOOK ID')
large_table.heading('b',text='BOOK NAME')
large_table.heading('c',text='AUTHOR')
large_table.heading('d',text='PRICE')
large_table.heading('e',text='GENRE')
large_table.heading('f',text='GENRE ID')
#adjusting the widths of the columns of treeview:
large_table.column('#0', minwidth=0, width=10, stretch=NO)
large_table.column('a', minwidth=0, width=80, stretch=NO)
large_table.column('b', minwidth=0, width=200, stretch=NO)
large_table.column('c', minwidth=0, width=130, stretch=NO)
large_table.column('d', minwidth=0, width=100, stretch=NO)
large_table.column('e', minwidth=0, width=100, stretch=NO)
large_table.column('f', minwidth=0, width=100, stretch=NO)
large_table.column('g', minwidth=0, width=100, stretch=NO)
large_table.pack()

m.mainloop()

