class Human:
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    def print_info(self):
        print(f"Name: {self._name}, Age: {self.__age}")

    def get_age(self):
        return self.__age



human_1 = Human("John", 30)
human_1.print_info()

human_2 = Human("Jane", 25)
human_2.print_info()

# human_2._name = "Alex"
# human_2.age = -5
print(human_2._name)
# print(human_2.__age)
print(human_2.get_age())
# human_2.age = -5
# print(human_2.get_age())
# print(human_2.age)