from student import Student
from database import load_students


students = load_students(Student)
Student.all_students = students

while True:
        print(" \n=========Student Management System=========")
        print("1. Add student")
        print("2. Search Student")
        print("3. Update Marks")
        print("4. Delete Student")
        print("5. Show all Student")
        print("6. Show Statistics")
        print("7. Check Grade")
        print("8. Exit")
        print("=============================================")

        choice = input("Enter your option (1-8): ")

        if choice == "1":
            Student.add_student()  

        elif choice =="2":
            Student.search_student()

        elif choice =="3":
            Student.update_student()

        elif choice == "4":
            Student.delete_student()

        elif choice == "5":
            Student.show_all_students()

        elif choice == "6":
            Student.show_statistics()

        elif choice == "7":
            Student.check_grade()

        elif choice == "8":
            print("Exiting student MGMT system. Goodbye! 👋")
            break 
        else:
            print("Invalid choice. Please try again.")

