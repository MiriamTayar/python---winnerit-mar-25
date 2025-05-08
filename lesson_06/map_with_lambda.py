
numbers = [1, 2, 3, 4, 5]

def square_numbers(x: int):
    return x ** 3

final_result = list(map(lambda x: x ** 2, numbers))
print(final_result)

print(square_numbers(5)) # call to the function

#provide function as parameter
final_result_2 = list(map(square_numbers, numbers))
print(final_result_2)



def work_with_lust(list_of_nums: list[int]):
    new_list = []
    for num in list_of_nums:
        new_list.append(num ** 2)
    return new_list
print(work_with_lust(numbers))