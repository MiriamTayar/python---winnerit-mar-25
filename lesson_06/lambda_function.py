
def calculate_result(x, y):
    result = x ** y
    return result

calculation = lambda x, y: x ** y
result = calculation(5, 3)
print(result)
print(calculate_result(5, 3))

print_with_lambda = lambda x: print(x)
print_with_lambda("Hello")
#רק במקומות שלמבדה מקצרת, אז טוב להשתמש בה, אבל כאן אין צורך להשתמש כי הדפסה רגילה גם נעשית בשורה אחת.