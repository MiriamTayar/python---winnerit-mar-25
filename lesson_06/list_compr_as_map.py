numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def square_numbers(x: int):
    return x ** 2

final_result = list(map(lambda x: x ** 2 , numbers))
print(final_result)

# provide function as parameter
final_result_2 = list(map(square_numbers, numbers))
print(final_result_2)


def work_with_list(list_of_nums: list[int]):
    new_list_2 = []
    for num in list_of_nums:
        new_list_2.append(num ** 2)
    return new_list_2

print(work_with_list(numbers))

new_list = [item ** 2 for item in numbers]
print(new_list)