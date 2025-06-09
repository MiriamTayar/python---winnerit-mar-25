class Human:
    def __init__(self, name, age):
        self._name = name
        self.age = age

        def print_info(self):
            print(f"Name: {self._name}, Age: {self.age}")

human_1 = Human("Miriam", 25)
human_1.print_info()

human_2 = Human("Rachek", 22)
human_2.print_info()

human_2.age = -5
human_2.print_info()
