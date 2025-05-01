grades = [80, 100, 95, 80]
print(f"{grades = }")
print(id(grades))
element_to_remove = 81
print(element_to_remove in grades)
grades.remove(element_to_remove)
print(f"{grades =}")
print(id(grades))

# del grades[0]
# print(f"{grades = }")
# print(id(grades))

