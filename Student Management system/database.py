import json

def save_students(students):
    students_data = []

    for student in students:
        student_dict = {
            "name": student.name,
            "roll_number": student.roll_number,
            "department": student.department,
            "marks": student.marks
        }

        students_data.append(student_dict)

    with open("students.json", "w") as file:
        json.dump(students_data, file, indent = 4)

def load_students(Student):
    students = []

    try:
        with open("students.json", "r") as file:
            students_data = json.load(file)
            for student in students_data:
                new_student = Student(
                    student["name"],
                    student["roll_number"],
                    student["department"],
                    student["marks"]
                )

                students.append(new_student)

    except FileNotFoundError:
        print("ℹ️  No existing student data found. Starting with an empty list.")

    except json.JSONDecodeError:
        print("❌ Student data file is corrupted. Starting with an empty list.")

    return students