import json

class Student:
    all_students = []

    def __init__(self, name, roll_number, department, marks):
        self.name = name
        self.roll_number = roll_number
        self.department = department
        self.marks = marks

# VALIDATION METHODS

    @staticmethod
    def get_name():
        while True:
            name = input("Enter your name: ").strip()
            
            if len(name) < 2:
                print("❌ Invalid name. Please enter a name with at least 2 characters.")
            elif not name.replace(" ", "").isalpha():
                print("❌Invalid name. Please enter a name containing only letters and spaces.")
            else:
                return name
    
    @staticmethod
    def get_marks():
        while True:
            try:
                marks =int(input("Enter the marks:"))

                if marks in range(0, 101):
                    return marks
                else:
                    print("Invalid marks. Please enter marks between 0 and 100.")

            except ValueError: 
                print("❌ Invalid input. Please enter a valid integer.")

    @staticmethod
    def get_department():
        while True:
            department = input("Enter your department:  ").strip()

            if len(department) < 2:
                print("❌ Invalid department. Please enter a department with at least 2 characters.")
            elif not department.replace(" ", "").isalpha():
                print("❌Invalid department. Please enter a department containing only letters and spaces.")
            else:
                return department

    @staticmethod
    def get_roll_number():
        while True:
            try:
                roll_number =  int(input("Enter your roll_number:  "))

                if Student.find_student_by_roll(roll_number):
                    print("❌ Roll number already exists. Please enter a unique roll number.")
                else:
                    return roll_number

            except ValueError:
                print("❌ Invalid input. Please enter a valid integer.")

    @staticmethod
    def get_existing_roll_number():
        while True:
            try:
                roll = int(input("Enter the roll number: "))
                return roll
            except ValueError:
                print("❌ Invalid input. Please enter a valid integer.")

# CRUD METHODS

    @classmethod
    def add_student(cls):
        name = cls.get_name()
        roll = cls.get_roll_number()
        department = cls.get_department()
        marks = cls.get_marks()
        student = cls(name, roll, department, marks)
        cls.all_students.append(student)

        print(f"✅ Student {name} added successfully! ")

        cls.save_students()  

    @classmethod
    def search_student(cls):
        roll = cls.get_existing_roll_number()
        student = cls.find_student_by_roll(roll)

        if student:
            student.show_details()
        else:
            print("❌ Student not found.")

    @classmethod
    def update_student(cls):
        roll = cls.get_existing_roll_number()
        student = cls.find_student_by_roll(roll)

        if student:
            new_marks = cls.get_marks()
            student.update_marks(new_marks)
            cls.save_students()
            print("✅ Marks updated successfully!")
        else:
            print("❌ Student not found. ")

    @classmethod
    def delete_student(cls):
        roll = cls.get_existing_roll_number()
        student = cls.find_student_by_roll(roll)

        if student:
            cls.all_students.remove(student)
            cls.save_students()
            print("✅ Student deleted successfully!")
        else:
            print("❌ Student not found.")
    
    @classmethod
    def check_grade(cls):
        roll = cls.get_existing_roll_number()
        student = cls.find_student_by_roll(roll)

        if student:
            grade = student.calculate_grade()
            print(f"\n🎓 Student: {student.name}")
            print(f"📊 Marks    : {student.marks}")
            print(f"🎓 Grade    : {grade}")
        else:
            print("❌ Student not found.")

# DISPLAY METHODS

    def show_details(self):
        print(f"\n========= Student Details: =========")
        print(f"👤 Name       : {self.name}")
        print(f"🆔 Roll Number: {self.roll_number}")
        print(f"🏢 Department : {self.department}")
        print(f"📊 Marks      : {self.marks}")
        print(f"🎓 Grade      : {self.calculate_grade()}")
        print("========================================")

    
    @classmethod
    def show_all_students(cls):
        if not cls.all_students:
            print("No students found. ")
            return
        
        for student in cls.all_students:
            student.show_details()
      
    @classmethod
    def  find_student_by_roll(cls, roll_number):
        for student in cls.all_students:
            if student.roll_number == roll_number:
                return student 

        return None 


# HELPER METHODS

    def update_marks(self, new_marks):
        self.marks = new_marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"

    @classmethod
    def show_statistics(cls):
        
        if not cls.all_students:
            print("❌ No students found.")
            return

        total_students = len(cls.all_students)
        total_marks = sum(student.marks for student in cls.all_students)

        average_marks = total_marks / total_students

        highest_marks = max(student.marks for student in cls.all_students)

        lowest_marks = min(student.marks for student in cls.all_students)

        print(f"\n=========  📊 Student Statistics =========")
        print(f"👨‍🎓 Total Students : {total_students}")
        print(f"📊 Total Marks    : {total_marks}")
        print(f"📈 Average Marks  : {average_marks:.2f}")
        print(f"🥇 Highest Marks  : {highest_marks}")
        print(f"🥈 Lowest Marks   : {lowest_marks}")
        print("==============================================")

# FILE HANDLING METHODS

    @classmethod
    def save_students(cls):
        students_data = []

        for student in cls.all_students:
            student_dict = {
                "name": student.name,
                "roll_number": student.roll_number,
                "department": student.department,
                "marks": student.marks
            }
            students_data.append(student_dict)
        with open("students.json", "w") as file:
            json.dump(students_data, file)

    @classmethod
    def load_students(cls):
        try:
            with open("students.json", "r") as file:
                students_data = json.load(file)

                for student in students_data:
                    new_student = cls(
                        student["name"],
                        student["roll_number"],
                        student["department"],
                        student["marks"]
                    )
                    cls.all_students.append(new_student)
        except FileNotFoundError:
            print("ℹ️  No existing student data found. Starting with an empty list.")

    @staticmethod
    def menu():
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

if __name__ == "__main__":
    Student.load_students()
    Student.menu()
        
        