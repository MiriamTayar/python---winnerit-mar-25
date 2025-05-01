age = int(input("Age: "))

if age > 18:
    print("You can enter!")
elif age > 14:
    print("You need your parents")
else:
    print("You not allowed to enter!")

print(" ========================= ")
if age > 18:
    print("You can enter!")
if age > 14:
    print("You need your parents")
else:
    print("You not allowed to enter!")