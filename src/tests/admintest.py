'''
Created on Oct 4, 2018

@author: suchethapanduranga
'''
import unittest
import sys
sys.path.append('/Users/suchethapanduranga/eclipse-workspace/CourseReg/src')
import re

import sqlite3
conn = sqlite3.connect('testOnlineCourse.db')
curr = conn.cursor()


def create_students_table():
    curr.execute("CREATE TABLE IF NOT EXISTS students(s_id INTEGER PRIMARY KEY, s_name TEXT, s_uname TEXT, s_email TEXT)")


def create_student_login_table():
    curr.execute("CREATE TABLE IF NOT EXISTS student_login(s_uname TEXT, s_pwd TEXT)")


def create_courses_table():
    curr.execute(
        "CREATE TABLE IF NOT EXISTS courses(c_id INTEGER PRIMARY KEY, c_name TEXT, c_duration INTEGER, c_subject TEXT)")

    
def create_course_student_table():
    curr.execute("CREATE TABLE IF NOT EXISTS course_student(c_id INTEGER, s_id INTEGER")

    
def create_course_fav_table():
    curr.execute("CREATE TABLE IF NOT EXISTS course_fav(fc_id INTEGER, s_id INTEGER")
 

class adminTest(unittest.TestCase):
    
    def getCount(self):
        curr.execute("SELECT count(*) from courses")
        conn.commit()
        data = curr.fetchone()
        count = data[0]
        return count

    def testadd_course(self):
        print ('====Testing the number of rows in the database before and after adding a course==== ')
        beforecount = self.getCount()
        self.add_course()
        aftercount = self.getCount()
        
        self.assertEqual(beforecount, aftercount)
        
    def testdel_course(self):
        cid = '88888'
        print ('====Testing the number of rows in the database before and after deleting a course (CourseID: ) ', cid)
        
        beforecount = self.getCount()
        self.del_course(cid)
        aftercount = self.getCount()
        
        self.assertEqual(beforecount, aftercount)
        
    def add_course(self):
    
        c_id = raw_input("Enter Course ID: ")
        while len(c_id) < 5 or not re.match('^[0-9]*$', c_id):
            c_id = raw_input('Please enter valid course ID: ')
            
        c_name = raw_input("Enter Course name: ")
        
        # c_name = c_name.split()
        while not re.match('^[a-zA-Z_ ]*$', c_name) or len(c_name) < 1:
            c_name = raw_input('Please enter valid course Name: ')

        c_duration = raw_input("Enter Course duration (in hours): ")
        while not re.match('^[0-9]*$', c_duration) or len(c_duration) < 1:
            c_duration = raw_input('Please enter valid course duration in hours: ')
   
        c_subject = raw_input("Enter the subject name: ")
        while not re.match('^[a-zA-Z_ ]*$', c_subject) or len(c_subject) < 1:
            c_subject = raw_input('Please enter valid course subject: ')
        
        try:
            curr.execute("INSERT INTO courses VALUES(?,?,?,?)",
            (c_id, c_name, c_duration, c_subject))
            conn.commit()
        except sqlite3.IntegrityError as e:
            print('Datbase Error. ')
        
    def del_course(self, cid):
        try:
            
            curr.execute("DELETE FROM courses WHERE c_id=:c_id", {"c_id": cid})
            conn.commit()
            
            print('Course deleted succesfully')
            
        except sqlite3.IntegrityError:
            print('Database error. Cannot complete action. ')
            return


if __name__ == "__main__":
    
    unittest.main()
