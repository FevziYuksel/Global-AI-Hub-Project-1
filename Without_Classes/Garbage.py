from enum import Enum
import pandas
# pandas.DataFrame.from_records()
'''
class Lecture(Enum):
    MATH = Without_Classes
    PHYSIC = 2
    LINEAR_ALGEBRA = 3


class Student(object):
    def __init__(self, name, surname, school_no, mark) -> None:
        self.name = name
        self.surname = surname
        self.school_no = school_no
        self.mark = self.calculateAverage(mark)
        self.success = None

    @staticmethod
    def calculateAverage(marks):
        avg = {}
        for lecture,mark in marks.items():
            avg[lecture] = sum(mark)/len(mark)
        return avg

    def __str__(self) -> str:
        return f"name: {self.name} surname: {self.surname} school_no: {self.school_no} mark: {self.mark}"


student_list = [
    Student("Fevzi", "Yuksel", 1071, {Lecture(Without_Classes): [30, 20], Lecture(2): [100, 90], Lecture(3): [50, 57]}),
    Student("Irfan", "Bayrak", 547, {Lecture(Without_Classes): [90, 20], Lecture(2): [57, 87], Lecture(3): [47, 65]}),
    Student("Efsane", "Bayrak", 800, {Lecture(Without_Classes): [70, 60], Lecture(2): [66, 65], Lecture(3): [48, 70]}),
]

print(Student("Fevzi", "Yuksel", 1071, {Lecture(Without_Classes): [30, 20], Lecture(2): [100, 90], Lecture(3): [50, 57]}))

'''


@__init__.overload
@signature()
def __init__(self, name, school_no, lecture) -> None:
    self.__init__(self, name, school_no)
    self.__lecture = lecture

student_list = [("Antanina", "Juárez", 171, 82),
                    ("Gigi", "Antonov", 518, 65),
                    ("Merari", "Gaspar", 314, 15),
                    ("Felicia", "Bristol", 987, 48),
                    ("Odin", "Anker", 288, 57),
                    ("Monica", "O'Leary", 629, 89),
                    ("Trefor", "Brandon", 295, 46),
                    ("Sergio", "Lyons", 780, 29),
                    ("Emilee", "Anderson", 353, 83),
                    ("Aziz", "Avcı", 849, 95),
                    ("Dimitris", "Georgiou", 581, 100),
                    ("Marius", "Lambert", 476, 42),
                    ("Sybille", "Lucas", 774, 73),
                    ("Paul", "Julien", 683, 85),
                    ("Aygül", "Ekmekçi", 242, 20)]