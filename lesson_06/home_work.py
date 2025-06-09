

#    =========  תרגיל 1  ========

class Person:
    def __init__(self, name):
        self.name = name

    def get(self):
        return self.name

class Employee(Person):
    def __init__(self, name, salary, role):
        super().__init__(name)
        self._salary = salary
        self._role = role

    # --- property עבור salary ---
    @property
    def salary(self):  #החזרת השכר של העובד
        return self._salary

    @salary.setter
    def salary(self, value): #מוודא שערך השכר אינו שלילי
        if value < 0:
            raise ValueError("Salary cannot be negative!")
        self._salary = value

        # --- property עבור role ---
    @property
    def role(self):  # החזרת התפקיד של העובד
        return self._role

    @role.setter
    def role(self, value):  # מוודא שערך המוזן אינו ריק
        if not value.strip():
            raise ValueError("The role cannot be empty!!!")
        self._role = value


#    -------- בדיקה ---------

#יצירת עובד
e = Employee("Dana", 5000, "Developer")
#הדפסת פרטי עובד לפני שינוי
print("Before promotion:")
print(f"Name: {e.name}")
print(f"Salary: {e.salary}")
print(f"Role: {e.role}")

#עידכון שכר ותפקיד עם setters

e.salary = 6000
e.role = "Team Lead"

print("\nAfter promotion:")
print(f"New salary: {e.salary}")
print(f"New role: {e.role}")

#ניסיון הכנסת ערך שלילי
try:
    e.salary = -1000
except ValueError as e:
    print(f"\nValidation error: {e}")


#    =========  תרגיל 2  ========

def filter_words(words, min_length):
    return [word for word in words if len(word) >= min_length]

words_list = ["apple", "banana", "cherry", "date", "fig", "grape"]
filtered_words = filter_words(words_list, 5)
print(filtered_words)