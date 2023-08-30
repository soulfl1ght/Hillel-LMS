from functools import reduce

def calc_average_value(numbers):
    odd_numbers = filter(lambda x: x % 2 != 0, numbers)
    squared_odd_numbers = map(lambda x: x ** 2, odd_numbers)
    squared_odd_numbers_list = list(squared_odd_numbers)
    sum_of_squares = reduce(lambda x, y: x + y, squared_odd_numbers_list)
    count = len(squared_odd_numbers_list)
    average = sum_of_squares / count
    return average

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
value = calc_average_value(numbers)
print(f"Середнє значення: {value}")

