salary = int(input("Enter your salary: "))
# if salary >= 20000:
#     print(f"{salary * 0.87}")
# else:
#     print(salary)

salary = salary * 0.87 if salary >= 20000 else salary
print(salary)