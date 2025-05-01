
#תרגיל משקופית 15
first_word = (input("Enter a first word: "))
second_word = (input("Enter a second word: "))

print("True" if first_word == second_word else "False")

#תרגיל משקופית 16
salary = int(input("Enter your salary: "))
if salary >= 20000:
    print(f"{salary * 0.87}")
else:
    print(salary)

#תרגיל משקופית 23



#תרגיל משקופית 31




#@@@@@@@@@@@@@@@@@@@@@@@@
day = input("Enter a day of the week: ")

match day.lower():
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("Weekday")
    case "saturday" | "sunday":
        print("Weekend")
    case _:
        print("Invalid day")
