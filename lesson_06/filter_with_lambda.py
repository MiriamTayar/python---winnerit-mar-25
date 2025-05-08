
nums_to_filter = [60, 80, 90, 45, 95, 70, 60]

def filter_numbers(x: int):
    if x < 60:
        return x >= 60

final_result = list(map(lambda x: x >= 60, nums_to_filter))
print(final_result)

print(filter_numbers(5)) # call to the function

#provide function as parameter
final_result_2 = list(map(filter_numbers, nums_to_filter))
print(final_result_2)



def work_with_lust(list_of_nums: list[int]):
    new_list = []
    for num in list_of_nums:
        if num >= 60:
            new_list.append(num)
    return new_list
print(work_with_lust(nums_to_filter))