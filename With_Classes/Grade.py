from Lecture import Lecture, LectureEnum
from Student import Student
import pandas as pd

# Unused imports
from openpyxl.workbook import Workbook
from pythonlangutil.overload import Overload, signature
import metaclass

global file_address  # python global variable is actually static like in C++


def determine_grade(grade):
    if grade > 100:
        raise Exception("Impossible grade!")
    if grade > 90:
        return "A+", "Pass"
    if grade > 80:
        return "A", "Pass"
    if grade > 70:
        return "B", "Pass"
    if grade > 60:
        return "C", "Pass"
    if grade > 50:
        return "D", "Pass"
    return "F", "Fail"


def grade_student_old(students, mode, encoding):
    global file  # Doesn't cause a problem in python but suppose to enter inner scopes
    try:
        file = open(file_address, mode=mode, encoding=encoding)
        for student in students:
            for lecture in student.lecture:
                grade, result = determine_grade(lecture.grade)
                lecture.setResult(grade)
                name, surname = student.name.split(" ")
                file.write(f"{name},{surname},{student.school_no},{lecture.lecture_name},{grade},{result}\n")
    except IOError:
        print("IO EXCEPTION!")

    finally:
        file.flush()
        file.close()
        return file


def grade_students(students, mode, encoding):
    with open(file_address, mode=mode, encoding=encoding) as file:

        for student in students:
            for lecture in student.lecture:
                letter_grade, status = determine_grade(lecture.grade)
                lecture.set_status(letter_grade)
                name, surname = student.name.split(" ")
                file.write(
                    f"{name},{surname},{student.school_no},{lecture.lecture_name},{lecture.grade},{letter_grade},{status}\n")


def create_pandas_dataframe(sep, header, columns, excel_address):
    data = pd.read_csv(file_address, sep=sep, header=header)

    data.columns = columns

    data.to_excel(excel_address)

'''
def input_students():
    numberofstudent = input("Enter number of students you wish to input: ")
    student_list = []
    for _ in range(numberofstudent):
        name = input("Name and surname: ")
        school_no = input("School no: ")
        numberoflecture = input("Enter number of lectures per student you wish to input: ")
        lectures = []
        for _ in range(numberoflecture):
            lecture_no = input("Lecture name: ") #Switch no to enum
            grades = []
            numberofgrade = input("Enter number of grades per lecture you wish to input: ")
            for _ in range(numberofgrade):
                grades.append(input("Grade: "))
            lectures.append(Lecture(lecture_no=lecture_no), grade=grades)
        student_list.append(Student(name=name, school_no=school_no,lecture= lectures ))
'''