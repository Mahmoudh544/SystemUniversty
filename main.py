from Student import student
from Doctor import doctor
from Teacher_assistant import teach_assistant
s1=student()
d1=doctor()
t1=teach_assistant()
print("\n \t \t \t \t \t \"welcome to our system\" ")
print("You need to Work with :")
print("1- student")
print("2- Doctor")
print("3- techer_assistant")
print("Enter 0 to exit")
choice = 0
choice = int(input("Enter your choice \n"))
while choice != 0:
    if (choice == 1):
        print("Welcome to student file")
        print("choose what do you need to do")
        print("1- Add New student ")
        print("2- Search for a student ")
        print("3- Display all data ")
        print("Enter your choice \n")
        choice2 = int(input())
        if (choice2 == 1):
            s1.insert_student()
        elif (choice2 == 2):
            s1.search_data()
        elif (choice2 == 3):
            s1.display_data()
        else:
            print("Enter right choice ")
    elif (choice == 2):
        print("1- Add Doctor")
        print("2- Display all data")
        choice3 = int(input("Enter your choice\n"))
        if (choice3 == 1):
            d1.insert_doctor()
        elif (choice3 == 2):
            d1.display_data()
        else:
            print("Enter right choice ")
    elif (choice == 3):
        print("1- add teacher ass")
        print("2- Display all data")
        choice4 = int(input("enter your choice\n"))
        if (choice4 == 1):
            t1.insert_teach_assistant()
        elif (choice4 == 2):
          t1.display_data()
        else:
            print("Enter right choice")
    elif (choice == 0):
        exit()
    else:
        print("Enter right choice")

































