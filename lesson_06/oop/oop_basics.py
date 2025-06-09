class Person:  #מקובל לרשום מחלקה באות גדולה


    def __init__(self, name: str, age: float, country: str, job: int):  #פונקצית Dander
        self.name = name
        self.age = age
        self.country = country
        self.job = job

    def __init__ (self): #בנאי ריק
        pass

    def say_hello(self):
        print(f"Hello {self.name}!😃!")

    def get_age(self):
        self.age()

# person = {
#     "name": "Join",
#     "age": 25,
#     "country": "Israel"
# }
#
# person_2 = {
#     "name": "Join",
#     "age": 25,
# }

person_object = Person("Miri", 21.7, "Israel")
person_object.say_hello()
print(person_object.get_age())
print(person_object.job())

person_object_2 = Person("Israeli Israeli", 60, "Panama")
person_object_2.say_hello()
print(person_object_2.get_age())
print(person_object_2.job())

# person_empty = Person(name="Name")
# person_empty.say_hello()

