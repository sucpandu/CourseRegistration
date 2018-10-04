README

==============Introduction=============

The application presents a CLI platform to mimic a course regestration system.
It provides two types of access, Admin and Student access. The admin panel has permissions to add, update or delete a course in the super list. The student profile, after login, has permissions to access the available courses, register for courses and update the favorite list. 

At the end of each operation the application prompts the student/admin for additional operations and loops accordingly. During logout, the applications prompts the student to add courses to a favorite list and calculates the total course hours and displays: 
<user name inputted> has signed up for <number of courses> courses with <total course hours> credits

=============Usage=================

Go to the directory containing the CourseReg project and run the commands below. This triggers a CL Interface for the user. 

user $ cd CourseReg/src
user $ python index.py

Running the test scripts:

user $ cd CourseReg/src/tests/
user $ python adminTest.py
user $ python studentTest.py

==========Code Structure===========

1. The code has been seggregated into appropriate classes based on OOP norms. 
2. The application makes use of a SQLite3 database to store information about the courses, registrations and students. (DB: OpenOnlineCourse.db) 
3. Separate unit test scripts are stored in tests/ module that performs unit tests on all the logical branches of the code. The test scripts uses a test database testOnlineCourse.db
4. Code dealing with Admin panel and Student panel are differentiated and seggregated under different modules. 
5. The favorite panel updates the favorites course list. (To note: This list is different from the registered courses list)
6. Credit hours calculation depends on the registered courses list for that particular Student ID. 


===========Validations==============

Since the code deals with raw input from the terminal, cartain validations on the input values ar enecessary. 
1. Courses
		- Course ID: A 5 digit integer (int)
		- Course Name: Freetext including spaces(string)
		- Course length: integer (int)
		- Course Subject: Freetext including spaces(string)

2. Student Login information
		- Student Name: Freetext including spaces(string)
		- Student Username: Freetext (string)
		- Student Email: String with a valid email format (email)
		- Student login password: character string of length 6 or greater than 6

==============Operations supported=============

1. Admin 
		- Login with password '8464'
		- Add Courses 
		- List Courses
		- Update Courses
		- Delete Courses

2. Student
		- Login
		- Register as new 
		After Login:
			- View Profile
			- View registered courses
      - View favorites list
      - View all available courses
      - Register for a course
      - Search for a course with course ID


==============Highlights================

1. REGEX: 
			- Usage of regex to validate the input arguments. 
2. SQLite3: 
			- Usage of a lightweight serverless databse like sqlite3 to store information. 
			- The advantage of SQLite is that it is easier to install and use and the resulting database is a single file that can be written to a USB memory stick. 
			- Using such on-disk file format for such record keeping programs improves performance, reduces cost and complexity, and improves reliability. 
3. SEPARATE ADMIN AND STUDENT MDOULES:
			- From an application point of view, abstracting the permissions for an admin from that of a student seems logical. 
			- This way only one authentic admin login will be able to make changes to the course list. 
3. UNIT TESTS: 
			- Rigorous tests on logical branches of the code. 
			- Each test unit is scripted to be independent. 
			- Used unittest test module from the python standard library 
			- Usage of test suite (collection of test cases) within unittest modules ensure the aggregation of tests that should be executed together. 



