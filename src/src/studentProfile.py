import sqlite3
import re
conn = sqlite3.connect('OpenOnlineCourse.db')
curr = conn.cursor()

"""def create_students_table():
    curr.execute("CREATE TABLE IF NOT EXISTS students(s_id INTEGER PRIMARY KEY, s_name TEXT, s_uname TEXT, s_email TEXT)")"""



def view_profile(sid):
    try:
        
        curr.execute("SELECT * from students where s_id=:s_id", {"s_id": sid})
        conn.commit()
        studentDetail = curr.fetchone()
        print('Welcome', str(studentDetail[1]))
        print('Student ID: ', str(studentDetail[0], ))
        print('UserName: ', str(studentDetail[2]))
        print('Email: ', str(studentDetail[3]))
    except sqlite3.IntegrityError as e:
        print ('Database error. Action cannot be completed. ')
        return
        
        