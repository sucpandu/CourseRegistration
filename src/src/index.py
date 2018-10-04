import sys
sys.path.append('/Users/suchethapanduranga/eclipse-workspace/CourseReg/src')

import sqlite3
from src import studentMaster
from src import administratorMaster
conn = sqlite3.connect('OpenOnlineCourse.db')
curr = conn.cursor()

def create_students_table():
    curr.execute("CREATE TABLE IF NOT EXISTS students(s_id INTEGER PRIMARY KEY, s_name TEXT, s_uname TEXT, s_email TEXT)")

def create_student_login_table():
    curr.execute("CREATE TABLE IF NOT EXISTS student_login(s_uname TEXT, s_pwd TEXT)")

while True:
    
    create_students_table()
    create_student_login_table()
    while True:
        
        print ('1: Administrator Login')
        print ('2: Student Login')
        print('0: Exit')
        
        loginChoice = raw_input('Please select an option:')
        

        if loginChoice == '1':
            while True:
                
                admkey = raw_input('Enter administrator key: ')
                
                if admkey == '8464':
                    print('=====Admin Panel=====')
                    administratorMaster.main()
                    break
                else:
                    print('Administrator Key is wrong. Please Try Again. ')
                    break

        elif loginChoice == '2':
            
            print('=======STUDENT SECTION========')
            while True:
                
                try:
                    print ('1: Login')
                    print ('2: Register')
                    print ('0: Exit')
                    slchoice = raw_input('Please select an option: ')
                except:
                    print('Wrong Choice. Please Try Again.')
                if slchoice == '1':
                    print('=======STUDENT LOGIN======')
                    studentMaster.student_login()

                elif slchoice == '2':
                    print('======STUDENT REGISTRATION======')
                    studentMaster.student_registration()
                elif slchoice == '0':
                    sys.exit()
                    
                else:
                    print('Invalid Choice. Please Try Again.')

        elif loginChoice == '0':
            sys.exit()
                    
        else:
            print('Invalid Choice. Please Try Again.')

    
