import sqlite3

conn = sqlite3.connect('OpenOnlineCourse.db')
curr = conn.cursor()


def create_course_student_table():
    curr.execute("CREATE TABLE IF NOT EXISTS course_student(c_id INTEGER, s_id INTEGER")

    
def create_course_fav_table():
    curr.execute("CREATE TABLE IF NOT EXISTS course_fav(fc_id INTEGER, s_id INTEGER")

def create_courses_table():
    curr.execute("CREATE TABLE IF NOT EXISTS courses(c_id INTEGER, c_name TEXT, c_duration INTEGER, c_subject TEXT)")


def view_registered_courses(sid):
    try:
        
        curr.execute("select course_student.c_id,courses.c_name, courses.c_duration, courses.c_subject from  course_student,courses where course_student.c_id = courses.c_id and course_student.s_id=:s_id", {"s_id": sid})
        conn.commit()
        rcourses = curr.fetchall()
        if len(rcourses) < 1:
            print ('You have currently no courses registered. ')
            return
        else:
            print("Courses currently registered for: ")
            print(" ID  - CourseName - CourseDuration (in Hours) - Subject")
            for rcourse in rcourses:
                print(str(rcourse[0]), str(rcourse[1]), str(rcourse[2]), str(rcourse[3]))
            avlCourseId = [int(i[0]) for i in rcourses]
    
            while True:
                
                print('Enter Course ID for details')
                print ('0: Previous Menu')
                
                c_idChoice = raw_input('Enter: ')
                if c_idChoice in avlCourseId:
                    view_reg_course_detail(c_idChoice)
                    break
                elif c_idChoice == '0':
                    return
                else:
                    print('Invalid Course ID. ')
                    return
    except sqlite3.IntegrityError as e:
        print ('Database error. Action cannot be completed. ')
        return

            
def cal_total_credits(sid):
    curr.execute("select course_student.c_id,courses.c_name, courses.c_duration, courses.c_subject from  course_student,courses where course_student.c_id = courses.c_id and course_student.s_id=:s_id", {"s_id": sid})
    conn.commit()
    ccourses = curr.fetchall()
    if len(ccourses) < 1:
        totalCourses = 0
        totalCredits = 0
    else:
        totalCourses = len(ccourses)
        totalCredits = 0
        for ccourse in ccourses:
            
            totalCredits += int(ccourse[2])
    return totalCourses, totalCredits


def add_fav(fcid, sid):
    try:
        
        if isinstance(fcid, int):
            curr.execute("SELECT count(*) from course_fav where fc_id=:fc_id and s_id=:s_id", {"fc_id": fcid, "s_id":sid})
            conn.commit()
            data = curr.fetchone()
            
            count = data[0]
            
            if (count < 1):
                curr.execute("INSERT OR REPLACE INTO course_fav (fc_id, s_id) VALUES(?,?)", (fcid, sid))
                conn.commit()
            else:
                return
        
        else:
            for item in fcid:
                
                curr.execute("SELECT count(*) from course_fav where fc_id=:fc_id and s_id=:s_id", {"fc_id": item, "s_id":sid})
                conn.commit()
                data = curr.fetchone()
                
                count = data[0]
                
                if (count < 1):
                    
                    curr.execute("INSERT OR REPLACE INTO course_fav (fc_id, s_id) VALUES(?,?)", (item, sid))
                    conn.commit()
            else:
                return
    except sqlite3.IntegrityError as e:
        print ('Database error. Action cannot be completed. ')
        return
            

def view_favorite_courses(sid):
    try:
        curr.execute("select course_fav.fc_id,courses.c_name, courses.c_duration, courses.c_subject from  course_fav,courses where course_fav.fc_id = courses.c_id and course_fav.s_id=:s_id", {"s_id": sid})
        conn.commit()
        ccourses = curr.fetchall()
        if len(ccourses) < 1:
            print('No favorites registered.')
        else:
            print("Favorite courses: \n ")
            print(" ID  - CourseName - CourseDuration (in HOurs) - Subject")
            for ccourse in ccourses:
                print(str(ccourse[0]), str(ccourse[1]), str(ccourse[2]), str(ccourse[3]))
            return
    except sqlite3.IntegrityError as e:
        print ('Database error. Action cannot be completed. ')
        return
    

def view_reg_course_detail(cid):
    curr.execute("SELECT courses.c_id, courses.c_name, courses.c_duration, courses.c_subject  from courses where courses.c_id=:c_id ", {"c_id": cid})
    conn.commit()
    courseDetail = curr.fetchone()

    print('Course ID: ', str(courseDetail[0]))
    print (' Course Name: ', str(courseDetail[1]))
    print('Course Duration (in Hours): ', str(courseDetail[2]))
    print('Course Subject: ', str(courseDetail[3]))
    
    return
