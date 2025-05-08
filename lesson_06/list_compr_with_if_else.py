nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list_3 = [num ** 3 if num % 2 == 0 else num ** 0 for num in nums]

print(new_list_3)