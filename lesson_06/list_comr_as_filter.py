nums_to_filter = [60, 80, 90, 100, 50, 45, 78, 90, 95, 70, 61, 30]

def filter_numbers(x: int):
    return x >= 60

final_result = list(filter(lambda x: x >= 60, nums_to_filter))
print(final_result)

print(filter_numbers(5)) # call to the function

# provide function as parameter
final_result_2 = list(filter(filter_numbers, nums_to_filter))
print(final_result_2)


def work_with_list(list_of_nums: list[int]):
    new_list = []
    for num in list_of_nums:
        if num >= 60:
            new_list.append(num)
    return new_list



print(work_with_list(nums_to_filter))

filtered_numbers = [number for number in nums_to_filter if number >= 60]
print(filtered_numbers)