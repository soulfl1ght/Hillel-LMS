#1 task
import random
qwer = lambda x: x % 2 == 0
num = int(input("Type your number:"))
print(num)
result = qwer(num)
if result:
    print(f"{num} є парним числом.")
else:
    print(f"{num} є непарним числом.")

#2 task
nums = [4, 32, 235, 423, 1694, 543, 5783, 52435, 52356, 54775, 93258, 203505]
def find_max(nums):
    if len(nums) == 0:
        return float('-inf')
    max_rest = find_max(nums[1:])
    if nums[0] > max_rest:
        return nums[0]
    else:
        return max_rest

print(find_max(nums))

#3 task
def find_popularity(films):
    most_popular = max(films, key=lambda x: x[1])
    less_popular = min(films, key=lambda x: x[1])
    
    return most_popular, less_popular

films = [('Captain Marvel', 7.0), ('Aladdin', 7.4), ('Toy Story 4', 8.2), ('Avengers: Endgame', 8.7)]

most_popular, less_popular = find_popularity(films)

print(f"Most popular: {most_popular[0]} - {most_popular[1]}")
print(f"Less popular: {less_popular[0]} - {less_popular[1]}")
