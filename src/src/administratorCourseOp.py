import sqlite3
import re
import sys

conn = sqlite3.connect('OpenOnlineCourse.db')
curr = conn.cursor()


def create_courses_table():
    curr.execute(
        "CREATE TABLE IF NOT EXISTS courses(c_id INTEGER PRIMARY KEY, c_name TEXT, c_duration INTEGER, c_subject TEXT)")


def add_course():
    
    c_id = raw_input("Enter Course ID: ")
    while len(c_id) < 5 or not re.match('^[0-9]*$', c_id):
        c_id = raw_input('Please enter valid course ID: ')

    c_name = raw_input("Enter Course name: ")
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
        print('New course added successfully')
        list_courses()
    except sqlite3.IntegrityError:
        print ('Error while adding course to database. Please make sure you have distinct course IDs. ')
        return


def list_courses():
    
    try:
        curr.execute("SELECT c_id ,c_name,c_duration, c_subject FROM courses")
        conn.commit()
        courses = curr.fetchall()
        print("\nThe courses available on list are: ")
        print(" ID  - CourseName - CourseDuration (in Hours) - CourseSubject")
        for course in courses:
            print(str(course[0]), str(course[1]), str(course[2]), str(course[3]))
        avlCourseId = [i[0] for i in courses]
    except sqlite3.IntegrityError as e:
        print ('Error accessing the database. Cannot complete action. ')
        return
    

def search_courses(c_search):
    c_search = raw_input("Enter a search keyword: ")
    
    try:
        curr.execute("CREATE VIRTUAL TABLE searchCourse USING courses(c_id ,c_name,c_duration, c_subject; SELECT * FROM searchCourse WHERE searchCourse MATCH c_search ")
        conn.commit()
        searchCourses = curr.fetchall()
        print (searchCourses)
        for course in searchCourses:
            print(str(course[0]), str(course[1]), str(course[2]), str(course[3]))
        
    except sqlite3.IntegrityError:
        print('Cannot find the search string in the database. Cannot complete action. ')
        return


def validate_cid(cid):
    
    curr.execute('select c_id from courses where c_id=:c_id' , {"c_id": cid})
    data = curr.fetchall()
    if len(data) == 0:
        return False
    return True
        
    
def del_course(cid):
    try:
        if validate_cid:
            curr.execute("DELETE FROM courses WHERE c_id=:c_id", {"c_id": cid})
            conn.commit()
            
            print('Course deleted succesfully')
            list_courses()
        else:
            print ('Course ID not valid or not found in the database. ')
            return
    except sqlite3.IntegrityError:
        print('Database error. Cannot complete action. ')
        return


def edit_course(cid):
    
    try:
        curr.execute("SELECT * FROM courses WHERE c_id=:c_id", {"c_id": cid})
        conn.commit()
        courseDetail = curr.fetchone()
    
        ocid = courseDetail[0]
        ocname = courseDetail[1]
        ocdur = courseDetail[2]
        ocsub = courseDetail[3]
    
        print('Old Course Name: ', ocname)
        
        ncname = raw_input('Enter New Course Name: ')
        if not re.match('^[a-zA-Z_ ]*$', ncname) or len(ncname) < 1:
            print ("Error! Course name is invalid or empty. Please try again with valid characters.")
            return
        
        print('Old Course duration (in hours): ', ocdur)
        
        ncdur = raw_input('Enter New Course duration (in hours): ')
        if not re.match('^[0-9]*$', ncdur) or len(ncdur) < 1:
            print ("Error! Course duration is invalid or empty. Please try again with valid integers. ")
        
        print('Old Course subject: ', ocsub)
        
        nsub = raw_input('Enter New Course subject: ')
        if not re.match('^[a-zA-Z_ ]*$', nsub) or len(nsub) < 1:
            print ("Error! Subject name is invalid or empty. Please try again with valid characters.")
        
        curr.execute(
            "UPDATE courses SET c_name = :c_name, c_duration = :c_duration, c_subject = :c_subject WHERE courses.c_id = :c_id",
            ({"c_name": ncname, "c_duration": ncdur,
              "c_subject": nsub, "c_id": ocid}))
        conn.commit()
    
        print('Course updated successfully')
        view_course_detail(ocid)
        
    except sqlite3.IntegrityError:
        print('Database error. Cannot complete action. ')
        return


def view_course_detail(cid):
    try:
        curr.execute("SELECT courses.c_id, courses.c_name, courses.c_duration, courses.c_subject from courses where courses.c_id=:c_id", {"c_id": cid})
        conn.commit()
        courseDetail = curr.fetchone()
    
        print('Course ID: ', courseDetail[0])
        print('Course Name: ', courseDetail[1])
        print('Course Duration (in Hours): ', courseDetail[2])
        print('Course Subject: ', courseDetail[3])
        
    except sqlite3.IntegrityError:
        print('Database error. Cannot complete action. ')
        return


def main():

    while True:
        
        print ("Please select an option: ")
        print('1: Add course to the super list')
        print('2: List all the courses')
        print ('3: Update a course')
        print ('4: Delete a course')
        print ('0: Exit')
        
        choice = raw_input('Enter: ')
    
        if choice == '1':
            create_courses_table()
            
            add_course()
            
            cont = raw_input('Would you like to continue? Y/ N')
            if cont == 'N' or cont == 'n':
                
                break
            elif cont == 'Y' or cont == 'y':
                continue
            else:
                while cont not in ['y', 'Y', 'n', 'N']:
                    cont = raw_input('Please enter a valid choice: Y/ N')
    
        elif choice == '2':
            list_courses()
            cont = raw_input('Would you like to continue? Y/ N')
            if cont == 'N' or cont == 'n':
                break
            elif cont == 'Y' or cont == 'y':
                continue
            else:
                while cont not in ['y', 'Y', 'n', 'N']:
                    cont = raw_input('Please enter a valid choice: Y/ N')
            
        elif choice == '3':
            
            cid = raw_input('Please enter the course ID you wish to update: ') 
            if validate_cid(cid):
                edit_course(cid)
                cont = raw_input('Would you like to continue? Y/ N')
                if cont == 'N' or cont == 'n':
                    break
                elif cont == 'Y' or cont == 'y':
                    continue
                else:
                    while cont not in ['y', 'Y', 'n', 'N']:
                        cont = raw_input('Please enter a valid choice: Y/ N')
                
            else:
                print ('Not a valid course ID. Please try again.')
            
        elif choice == '4':
            cid = raw_input('Please enter the course ID you wish to delete: ') 
            if validate_cid(cid):
                del_course(cid)
                cont = raw_input('Would you like to continue? Y/ N')
                if cont == 'N' or cont == 'n':
                    break
                elif cont == 'Y' or cont == 'y':
                    continue
                else:
                    while cont not in ['y', 'Y', 'n', 'N']:
                        cont = raw_input('Please enter a valid choice: Y/ N')
            
            else:
                print ('Not a valid course ID. Please try again.')
                  
        elif choice == '0':
            
            return 
        
        else:
            print('Invalid choice. Please try again.  \n')
        
