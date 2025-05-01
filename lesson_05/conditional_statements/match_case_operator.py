# color = input("Enter a color: ")
#
# if color == "red":
#     print("Stop")
# elif color == "yellow":
#     print("Caution")
# elif color == "green":
#     print("Go")
# else:
#     print("Unknown color")
#
# match color:
#     case "red":
#         print("Stop")
#     case "green":
#         print("Go")
#     case "yellow":
#         print("Caution")
#     case _:
#         print("Unknown color")

fruit = input("Enter a fruit: ")

match fruit:
    case "apple" | "banana" | "orange":
        print("This is a common fruit.")
    case "mango" | "ananas":  # if fruit == "mango" or fruit == "ananas"
        print("This is a tropical fruit.")
    case _:
        print("Unknown fruit.")