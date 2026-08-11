from database import save_students

class Student:
    all_students = []

    def __init__(self, name, roll_number, department, marks):
        self.name = name
        self.roll_number = roll_number
        self.department = department
        self.marks = marks

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
    def  find_student_by_roll(cls, roll_number):
        for student in cls.all_students:
            if student.roll_number == roll_number:
                return student 

        return None 

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
    def add_student(cls):
        name = cls.get_name()
        roll = cls.get_roll_number()
        department = cls.get_department()
        marks = cls.get_marks()
        student = cls(name, roll, department, marks)
        cls.all_students.append(student)

        save_students(cls.all_students)

        print(f"✅ Student {name} added successfully! ")

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
            save_students(cls.all_students)
            print("✅ Marks updated successfully!")
        else:
            print("❌ Student not found. ")

    @classmethod
    def delete_student(cls):
        roll = cls.get_existing_roll_number()
        student = cls.find_student_by_roll(roll)

        if student:
            cls.all_students.remove(student)
            save_students(cls.all_students)
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
        print("=============================================")

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

                if 0 <= marks <= 100:
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