from typing import List, Any

from pythonlangutil import overload

from Lecture import Lecture, LectureEnum


class Student(object):
    student_number = 0

    def __init__(self, name, school_no, *lectures) -> None:  # default argument

        self.__name = name
        self.__school_no = school_no
        self.__lecture = list(lectures)

        Student.student_number = Student.student_number + 1
        print("An object is instantiated")
        print("Object number is " + str(self.student_number))

    @property
    def name(self):
        return self.__name

    @property
    def school_no(self):
        return self.__school_no

    @property  # getter
    def lecture(self) -> list[Any]:
        return self.__lecture

    @lecture.setter  # setter //Not sure if it works ?
    def lecture(self, lecture):
        self.__lecture = lecture

    def add_lecture(self, lecture_no, mark):
        self.__lecture.append(Lecture(lecture_no, mark))

    def add_lecture_obj(self, lecture):
        if type(lecture) is list:
            self.__lecture.extend(lecture)
        elif isinstance(lecture, Lecture):
            self.__lecture.append(lecture)
        else:
            raise Exception("The entered type is not compatible")

    def __add__(self, lecture):
        self.add_lecture_obj(lecture)

    def __str__(self) -> str:
        lecture = ""
        for s in self.__lecture:
            lecture += str(s) + " "
        return f"name: {self.__name}, school No: {self.__school_no}, grade: {lecture}"

    def __del__(self):
        print("PYTHON HAS A DESTRUCTOR! WHY? HOW TO INVOKE IT ?")
        Student.student_number = Student.student_number - 1
        print("Object number is " + str(self.student_number))
