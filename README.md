📝 Tkinter To-Do List with MySQL

A simple To-Do List desktop application built using Python (Tkinter GUI) and MySQL for data storage.
This app allows users to add, view, edit, and delete tasks with a status (Not/Done).


---

📌 Features

Add Tasks: Add new tasks to the list.

View Tasks: Display all tasks with their status in a table.

Update Status: Double-click a task to mark it as Done.

Delete Tasks: Remove tasks from the list.

Persistent Storage: All tasks are saved in a MySQL database.



---

🛠️ Requirements

Python 3.x

Tkinter (comes pre-installed with Python)

MySQL server

pymysql module


Install pymysql using:

pip install pymysql


---

🗄️ Database Setup

1. Open MySQL and create a database:



CREATE DATABASE a;
USE a;

2. Create the tdl table:



CREATE TABLE tdl (
    TASK VARCHAR(255) PRIMARY KEY,
    TASK_STATUS VARCHAR(50)
);


---

▶️ How to Run

1. Clone or download this repository.


2. Make sure your MySQL server is running.


3. Update your MySQL credentials in the Python script:



mycon = pymysql.connect(
    host="localhost",
    user="root",       # Your MySQL username
    password="abcd",   # Your MySQL password
    database="a"
)

4. Run the script:



python todolist.py


---

🎮 Usage

1. Add Task:

Click Add, type your task, and click Save.



2. View Tasks:

Click View to see all tasks with their current status.



3. Update Task Status:

Double-click on a task → A popup asks for confirmation → Status becomes Done.



4. Delete Task:

Select a task → Click Delete to remove it permanently.





---

📸 GUI Preview

tkinter's gui

![Alt text](https://github.com/banu06764-blip/tkinter-to-do-list/blob/e3ab2bf0ed1173c9521f6c27b1734dcfda59dc0f/20250804_073737.jpg)


mysql's image
![Alt text](https://github.com/banu06764-blip/tkinter-to-do-list/blob/e3ab2bf0ed1173c9521f6c27b1734dcfda59dc0f/20250804_073754.jpg)



---


💡 Notes

If delete or update doesn’t work, check if the selected task exists in the database.

Make sure MySQL service is running before starting the app.



---
