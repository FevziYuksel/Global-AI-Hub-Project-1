import With_Classes.Grade
from With_Classes.Grade import grade_students, create_pandas_dataframe
from With_Classes.Lecture import Lecture
from With_Classes.Student import Student

if __name__ == '__main__':
    student_list = [
        Student("Fevzi Yüksel", 723, Lecture(1, 70, 80), Lecture(2, 55, 100), Lecture(3, 54, 63)),
        Student("İrfan Bayrak", 547, Lecture(1, 90, 20), Lecture(2, 57, 87), Lecture(3, 47, 65)),
        Student("Tuğbanur Balcı", 848, Lecture(1, 100, 100), Lecture(2, 90, 60), Lecture(3, 40, 30)),
        Student("Efsane Kaplan", 800, Lecture(1, 70, 60), Lecture(2, 66, 65), Lecture(3, 48, 70)),
    ]
    # Assigning global/static variables from another file
    With_Classes.Grade.file_address = "grades.txt"

    grade_students(students=student_list, mode="w", encoding="utf-8")

    columns = ["Student Name", "Student Surname", "Student Number", "Lecture Name", "Numeric Grade",
               "Letter Grade", "Status"]

    # python support default and random order parameters
    create_pandas_dataframe(header=None, sep=",", columns=columns, excel_address="Grades.xlsx")
