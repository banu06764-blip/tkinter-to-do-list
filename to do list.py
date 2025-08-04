import tkinter
from tkinter import ttk,messagebox,font
import pymysql
mycon = pymysql.connect(
host="localhost",
user="root",
password="abcd",
database="a",
charset="utf8mb4",
collation="utf8mb4_general_ci"
)
mc=mycon.cursor()
root=tkinter.Tk()
f2=font.Font(family='Arial',size=4)
d1={}
select=''
a1=tkinter.StringVar()
def load():
	global select
	for i in tv.get_children():
		tv.delete(i)
	mc.execute("select*from tdl")
	r=mc.fetchall()
	for row in r:
		d1[row[1]]=row[2:]
		tv.insert('',tkinter.END,values=row[0:])
		select=row[1]
def add():
	root1.pack_forget()
	root2.pack()
def view():
	root2.pack_forget()
	root1.pack()
def save():
    global select
    select = a1.get()
    if select == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return
    x = "INSERT INTO tdl VALUES (%s, %s)"
    sql = (select, 'Not')
    mc.execute(x, sql)
    mycon.commit()
    messagebox.showinfo('to do list','updated!')
    a1.set("")
    load()
def d(obj):
	Delete.configure(state=tkinter.NORMAL)
def delete():
	x=tv.selection()[0]
	y=tv.item(x)
	nm=y['values'][0]
	q="delete from tdl where TASK=%s "
	sql=(nm)
	mc.execute(q,sql)
	mycon.commit()
	load()
def edit(obj1):
	x=messagebox.askyesno('to do list','wanna update status')
	X=tv.selection()[0]
	Y=tv.item(X)
	nm=Y['values'][0]
	if x:
		y='update tdl set TASK_STATUS= %s where TASK=%s'
		sql=('Done',nm)
		mc.execute(y,sql)
		mycon.commit()
		load()





root1=tkinter.Frame(root)
ts=ttk.Style()
ts.configure('Treeview.Heading',font=('Arial',4,'bold'))
ts.configure('Treeview',font=('Arial',4,'bold'))
tv=ttk.Treeview(root1,columns=('c1','c2'),show='headings')
tv.heading('c1',text='TASK')
tv.heading('c2',text='TASK STATUS')
tv.pack()
root1.pack()
tkinter.Button(root1,text='Add',command=add).pack()
root2=tkinter.Frame(root)
tkinter.Label(root2,text='Enter Your Task',font=f2).pack()
e=tkinter.Entry(root2,textvariable=a1,font=f2)
e.pack()
tkinter.Button(root2,text='save',font=f2,command=save).pack()
tkinter.Button(root2,text='view',font=f2,command=view).pack()
tv.bind('<<TreeviewSelect>>',d)
Delete=tkinter.Button(root1,text='delete',font=f2,command=delete)
Delete.configure(state=tkinter.DISABLED)
Delete.pack()
tkinter.Button(root1,text='view',command=load).pack()
tv.bind('<Double-1>',edit)

root.mainloop()