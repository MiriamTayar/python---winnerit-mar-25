from calendar import month

#מצגת 5
#תרגיל 1
# age= int(input("Enter your age: "))
# if age >= 18:
#     has_ticket = input("Do you have ticket? (yes/ no) ")
#     if has_ticket == "yes":
#         print("You can enter to club!")
#     else: print("Sorry, you can't enter to club!")
# elif age<18:
#     has_permission = input("Do you have special permission? (yes/ no) ")
#     if has_permission =="yes":
#         print("You can enter to club!")
#     else: print("Sorry, you can't enter to club!")


#תרגיל 2
# first_num = int(input("Enter first number: "))
# second_num = int(input("Enter second number: "))

# if first_num > second_num:
#     print(f"The larger number is: {first_num})")
# else: print(f"The larger number is: {second_num}")

#בקצרה יותר....
# print(f"The larger number is: {first_num}" if first_num> second_num else f"The larger number is: {second_num}")


#תרגיל 3
# months = input("Enter a month: ")

# match months:
#     case "December" | "January" | "February":
#         print("Season: Winter")
#     case "March" | "April" | "May":
#         print("Season: Spring")
#     case "June" | "July" | "August":
#         print("Season: Summer")
#     case "September" | "October" | "November":
#         print("Season: Autumn")
#     case _:
#         print("Invalid month.")



#תרגיל 4
# sum_numbers = 0
#
# for i in range(5):
#     num = float(input(f"Enter number {i+1}:"))
#     sum_numbers += num
#
# average = sum_numbers/5
# print(f"The sum of number: {average}")


#תרגיל 5
# def fine_max(*args):
#     if not args:
#         return "No number were given."
#     max_num = args[0]
#     for num in args[1:]:
#         if num > max_num:
#             max_num = num
#
#     return max_num


# print(f"The max number is: {fine_max(3,7,2,8,10,4)}")
# print(fine_max())


# תרגיל 6
def calculate_average (*args):
    if not args:
        return 0
    sum_of_numbers = 0
    for num in args[0:]:
        sum_of_numbers += num
    average = sum_of_numbers/len(args)
    return int(average)


print(f"The average is: {calculate_average (10,20,30,40,50)}")
# print(calculate_average())




