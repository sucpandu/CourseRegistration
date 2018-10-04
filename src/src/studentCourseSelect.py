import sqlite3

conn = sqlite3.connect('OpenOnlineCourse.db')
curr = conn.cursor()


def create_courses_table():
    curr.execute("CREATE TABLE IF NOT EXISTS courses(c_id INTEGER, c_name TEXT, c_duration INTEGER, c_subject TEXT)")


def create_course_student_table():
    curr.execute("CREATE TABLE IF NOT EXISTS course_student(c_id INTEGER, s_id INTEGER")


def reg_course(cid, sid):
    try:
        
        curr.execute("INSERT OR REPLACE INTO course_student (c_id, s_id) VALUES(?,?)", (cid, sid))
        conn.commit()
        print('Registration successful')
    except sqlite3.IntegrityError as e:
        print ('Database error. Action cannot be completed. ')
        return


def viewAvlCourses(sid):
    try:
        
        curr.execute("SELECT c_id ,c_name,c_duration, c_subject from courses")
        conn.commit()
        courses = curr.fetchall()
        print("Available Courses are:")
        print(" ID  - CourseName - CourseDuration (in Hours) - Subject")
        for course in courses:
            print(str(course[0]), str(course[1]), str(course[2]), str(course[3]))
        avlCourseId = [int(i[0]) for i in courses]
       
        print('Enter Course ID For Details')
        print ('0: Previous Menu')
        
        c_idChoice = raw_input()
        if int(c_idChoice) in avlCourseId:
    
            print("Course Details")
            view_course_detail(c_idChoice, sid)
            return
        elif c_idChoice == 0:
            return
            
        else:
            print('Invalid choice')
            return
    except sqlite3.IntegrityError as e:
        print ('Database error. Action cannot be completed. ')
        return

    
def view_course_detail(cid, sid):
    try:
        curr.execute("SELECT courses.c_id, courses.c_name, courses.c_duration, courses.c_subject  from courses where courses.c_id=:c_id ", {"c_id": cid})
        conn.commit()
        courseDetail = curr.fetchone()
        print('Course ID: ', str(courseDetail[0]))
        print ('Course Name: ', str(courseDetail[1]))
        print('Course Duration (in Hours): ', str(courseDetail[2]))
        print ('Course Subject: ', str(courseDetail[3]))
    
        curr.execute("SELECT count(*) from course_student where c_id=:c_id and s_id=:s_id", {"c_id": cid, "s_id":sid})
        conn.commit()
        data = curr.fetchone()
        count = data[0]
        if (count >= 1):
            cregchk = 1
        else:
            cregchk = 0
        while True:
            if cregchk == 1:
                print('You are already enrolled in this course. Cannot signup again. ')
                break  
    
            else:
                print ('0: Exit without signing up for this course.')
                print('1: Sign up for this course')
                
                c_idChoice = raw_input('Enter: ')
                
                if c_idChoice == '1':
                    reg_course(cid, sid)
                    break
                if c_idChoice == '0':
                    return
                else:
                    print('Invalid Choice.')
                    return
    except sqlite3.IntegrityError as e:
        print ('Database error. Action cannot be completed. ')
        return

