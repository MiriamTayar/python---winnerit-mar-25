# 1. No parameters and no return
import datetime


# def say_hello():
#     print("Hello Everyone!")
#     print("Hello from here!")
#
# say_hello()

# 2. Parameter and no return
# def say_hello_with_params(name: str, age: float): #זוהי שורת חתימה של הפונקציה
#     print(f"Hello {name.upper()}! Next year you will be {age + 1}")
#
# # say_hello_with_params("Miri", 21)
# say_hello_with_params(age=21, name="Miri")

# נתונים בהגדרה של הפונקציה נקראים- פרמטרים
# נתונים להעברה לפונקציה נקראים- ארגומנטים


# def check_weather(city: str = "jerusalem"): #This is default value- ערך ברירת מחדל
#     print(f"Cheking weather in {city}")
#     print(f"A weather is fine!")
#
# # check_weather()
# check_weather("Dubai")

# 3. Return + Parameters
#
# def calculate_sum(first_num: int, second_num: int) -> int | str :
#     if first_num < 0 or second_num < 0:
#         return "Invalid input"
#     return first_num + second_num
#
# result = calculate_sum(10, 20)
# print(result)
# print(calculate_sum(-5, 100))

# def get_current_time():  #פונקציה למציאת תאריך ושעה מדויקים
#     return datetime.datetime.now()
#
# print(get_current_time())
