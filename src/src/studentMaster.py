import sqlite3
from src import studentCourseReg
from src import studentCourseSelect
from src import studentProfile
import re

conn = sqlite3.connect('OpenOnlineCourse.db')
curr = conn.cursor()

def create_students_table():
    curr.execute("CREATE TABLE IF NOT EXISTS students(s_id INTEGER PRIMARY KEY, s_name TEXT, s_uname TEXT, s_email TEXT)")

def create_student_login_table():
    curr.execute("CREATE TABLE IF NOT EXISTS student_login(s_uname TEXT, s_pwd TEXT)")
    
 



def student_registration():
    # validation required
    s_name = ''
    s_uname = ''
    s_email = ''
    
    
    s_name = raw_input("Enter Student Name: ")
    while not re.match('^[a-zA-Z_ ]*$', s_name) or len(s_name)<1:
        s_name = raw_input("Please enter valid name: ")
    
    s_uname = raw_input("Select UserName: ")
    while not re.match('^[a-zA-Z_ ]*$', s_name) or len(s_uname)<1:
        s_name = raw_input("Please enter valid User name: ")
    
    s_email = raw_input("Enter e-mail: ")
    while s_email.count('@') != 1 and s_email.count('.') != 1:
        s_email = raw_input("Please enter a valid email. ")
    
        
    
    s_pwd = raw_input("Enter Password: (must have atleast 6 characters)")
    while len(s_pwd) < 6:
        s_pwd = raw_input('Please enter a password with atleast 6 characters: ')
    create_students_table()
    create_student_login_table()
    try:
        
        curr.execute(
            "INSERT INTO students (s_name, s_uname, s_email) VALUES(?,?,?)",
            (s_name, s_uname, s_email))
        conn.commit()
        curr.execute("INSERT INTO student_login  VALUES(?,?)", (s_uname, s_pwd))
        conn.commit()
        print('Registration Successful')
    except sqlite3.IntegrityError as e:
        print ('Database error. Action not completed. ')
        return


def validate_cid(cid):
    if cid is not None:
        curr.execute('select c_id from courses where c_id=:c_id' , {"c_id": cid})
        data = curr.fetchall()
        if len(data) == 0:
            return False
        return True
    else:
        print('Please enter valid Course ID. ')

def student_login():


    while True:
        print ('0: Exit')
        suname = raw_input("Enter your username to login: ")
        if suname == '0':
            return
        spassword = raw_input("Enter Your Password: ")
        curr.execute(
            "SELECT count(*) FROM student_login WHERE student_login.s_uname = ? AND student_login.s_pwd = ?",
            (suname, spassword))
        data = curr.fetchone()
        count = data[0]
        if (count >= 1):
            print("Login Successful")
            curr.execute("SELECT s_id, s_name FROM students WHERE students.s_uname=:s_uname", {"s_uname": suname})
            conn.commit()
            student = curr.fetchone()
            sid = student[0]
            print('WELCOME : ')
            print (student[1])
            while True:
                
                print ('Select an option: ')
                print("1: View Profile")
                print("2: View registered courses")
                print ('3: View favorites list')
                print("4: View all available courses")
                print("5: Register for a course")
                print ('6: Search for a course with course ID')
                
                print("0: Return")

                schoiceh = raw_input('Enter: ')
                if schoiceh == '1':
                    print("======Profile======")
                    studentProfile.view_profile(sid)
                    
                    cont = raw_input('Would you like to continue? Y/ N')
                    if cont == 'N' or cont == 'n':
                        break
                    elif cont == 'Y' or cont == 'y':
                        continue
                    else:
                        while cont not in ['y', 'Y', 'n', 'N']:
                            cont = raw_input('Please enter a valid choice: Y/ N')
                            
                elif schoiceh == '2':
                    print("======Registered Courses=======")
                    studentCourseReg.view_registered_courses(sid)
                    cont = raw_input('Would you like to continue? Y/ N')
                    if cont == 'N' or cont == 'n':
                        break
                    elif cont == 'Y' or cont == 'y':
                        continue
                    else:
                        while cont not in ['y', 'Y', 'n', 'N']:
                            cont = raw_input('Please enter a valid choice: Y/ N')
                    
                elif schoiceh == '3':
                    print("======Favorite Courses=======")
                    studentCourseReg.view_favorite_courses(sid)
                    cont = raw_input('Would you like to continue? Y/ N')
                    if cont == 'N' or cont == 'n':
                        break
                    elif cont == 'Y' or cont == 'y':
                        continue
                    else:
                        while cont not in ['y', 'Y', 'n', 'N']:
                            cont = raw_input('Please enter a valid choice: Y/ N')
                
                
                elif schoiceh == '4':
                    print("======Available Courses======")
                    studentCourseSelect.viewAvlCourses(sid)
                    cont = raw_input('Would you like to continue? Y/ N')
                    if cont == 'N' or cont == 'n':
                        break
                    elif cont == 'Y' or cont == 'y':
                        continue
                    else:
                        while cont not in ['y', 'Y', 'n', 'N']:
                            cont = raw_input('Please enter a valid choice: Y/ N')
                    
                elif schoiceh == '5':
                    print("======Registration Panel======")
                    cid = raw_input('Please enter a course ID to register: ')
                    
                    
                    if validate_cid(cid):
                        studentCourseSelect.view_course_detail(cid, sid)
               
                        cont = raw_input('Would you like to continue? Y/ N')
                        if cont == 'N' or cont == 'n':
                            break
                        elif cont == 'Y' or cont == 'y':
                            continue
                        else:
                            while cont not in ['y', 'Y', 'n', 'N']:
                                cont = raw_input('Please enter a valid choice: Y/ N')
                    
                    else:
                        print ('Please enter a valid Course ID. ')
                        print ("======Available Courses======")
                        studentCourseSelect.viewAvlCourses(sid)
                
                
            
                
            
                    
                        
                        
                    
                elif schoiceh == '6':
                    cid = raw_input('Please enter a course ID to view the details: \n')
                    if validate_cid(cid):
                        studentCourseReg.view_reg_course_detail(cid)
               
                        cont = raw_input('Would you like to continue? Y/ N')
                        if cont == 'N' or cont == 'n':
                            return
                    else:
                        print ('Please enter a valid Course ID. ')
                        print ("======Available Courses======")
                        studentCourseSelect.viewAvlCourses(sid)
                        
                    
                    
                    
                    
                elif schoiceh == '0':
                    print('======Add Favourites==== ')
                    print ('Please enter the course IDs you want to add to the favorites list : ')
                    print ('0: Previous Menu')
                    fcid = raw_input().split(',')
                    
                    if fcid == 0:
                        return
                    else:
                    
                    
                        studentCourseReg.add_fav(fcid, sid)
                        totalCourses, totalCredits = studentCourseReg.cal_total_credits(sid)
                        print ('Favorites has been updated. Note: Favorites list is different from your registered courses list. ')
                        print ('Student ', str(student[1]), ' has signed up for ' , str(totalCourses) , ' courses with '  , str(totalCredits),' total credits.')
                        
                        return

                else:
                    print('Invalid choice. Please try again. ')



        else:
            print('Incorrect User Name or Password. Please try again. ')
