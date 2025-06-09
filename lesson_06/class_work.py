


# ~~~~~~~ תרגיל 3 ~~~~~~~

class Person:
    def __init__(self, name: str):
        self._name=name

    def get_name(self):
        return self._name


class Student(Person):
    def __init__(self, name: str, student_id: int):
        super().__init__(name)
        self.__student_id = student_id

    def display_student_id(self):
        return self.__student_id

    #property for name
    @property   #החזרת השם של הסטודנט
    def name(self):
        return self._name


    @name.setter    #עידכון שם סטודנט
    def name(self,new_name):
        self._name = new_name


# ======= בדיקות =======


# יצירת מופע של Person
p = Person("Yossi")
print("Person name: ",p.get_name())

# יצירת מופע של Student
s = Student("David", 165897)
print("Student name:", s.name)
print("Student ID: ",s.display_student_id())

# עדכון השם של הסטודנט
s.name = "Shimi"
print("Updated student name:", s.name)