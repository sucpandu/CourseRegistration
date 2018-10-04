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
 

class studentTest(unittest.TestCase):

    def getCount(self):
        sid = '1'
        curr.execute("select course_student.c_id,courses.c_name, courses.c_duration, courses.c_subject from  course_student,courses where course_student.c_id = courses.c_id and course_student.s_id=:s_id", {"s_id": sid})
        conn.commit()
        rcourses = curr.fetchall()
        
        return len(rcourses)

    def testreg_course(self):
        print ('====Testing the number of registered courses for signed in student before and after adding a new course==== ')
        sid = '1'
        cid = '11111'
        
        beforecount = self.getCount()
        self.reg_course(cid, sid)
        aftercount = self.getCount()
        
        self.assertEqual(beforecount, aftercount)
        
    def reg_course(self, cid, sid):
        curr.execute("INSERT OR REPLACE INTO course_student (c_id, s_id) VALUES(?,?)", (cid, sid))
        conn.commit()


if __name__ == "__main__":
    unittest.main()
