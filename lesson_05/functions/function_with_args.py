#
# names = ["Michal", "Debora", "Ayala"]
#
# def greet(name_to_iterate: list[str]):
#     for namen in name_to_iterate:
#         print(f"Hi {namen}!!!!")
#
# greet(names)



# names = ["Michal", "Debora", "Ayala"]

def greet(*args):
    print(args)
    print(type(args))
    for namen in args:
        print(f"Hi {namen}!!!!")

greet("Michal", "Debora", "Ayala")
