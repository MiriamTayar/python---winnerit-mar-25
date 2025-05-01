age = int(input("Age: "))

if 18 < age <= 67:
    print("You can enter!")
elif 14 < age <= 18:
    print("You need your parents")
elif age > 67:
    pass
else:
    print("You not allowed to enter!")

print("After if-elif-else")