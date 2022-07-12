from enum import Enum


class LectureEnum(Enum):
    MATH = 1
    PHYSIC = 2
    LINEAR_ALGEBRA = 3


class Lecture(object):

    def __init__(self, lecture_no, *grades) -> None:
        self.__lecture_name = LectureEnum(lecture_no)
        self.__grade = self.calculateAverage(grades)
        self.__status = None

    @staticmethod
    def calculateAverage(grades) -> int:
        if grades is list or tuple:
            return sum(grades) / len(grades)
        elif type(grades) is Lecture:
            return grades
        else:
            raise Exception("The entered type is not compatible")

    @property
    def lecture_name(self):
        return self.__lecture_name

    @property
    def grade(self):
        return self.__grade

    @property
    def status(self):
        return self.__status

    def set_status(self,status):
        self.__status = status

    def __str__(self) -> str:
        return f"{self.__lecture_name.name} {self.__grade} {self.__status}"

    #Enums cannot be innerclass / python doesn't support inner class ??
    '''
    class LectureEnum(Enum):
        MATH = 1
        PHYSIC = 2
        LINEAR_ALGEBRA = 3
    '''
