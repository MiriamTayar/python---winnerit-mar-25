nums_to_filter = [60, 80, 90, 100, 50, 45, 78, 90, 95, 70, 61, 30]

def work_with_list(list_of_nums: list[int]):
    new_list = []
    for num in list_of_nums:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

print(work_with_list(nums_to_filter))

# list comprehension