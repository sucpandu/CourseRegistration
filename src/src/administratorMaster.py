from src import administratorCourseOp


def choice_administrator_home():
    
    print('1: Manage courses')
    print('0: Logout')
    print("Please select an option: ")


def main():
   while True:
        choice_administrator_home()
        choice = raw_input()

        if choice == '1':
            print('======MANAGE  COURSES=====')
            administratorCourseOp.main()
        
        elif choice == '0':
           return
        else:
            print('Invalid Choice. Please try again. ')
