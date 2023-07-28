lst = [45, 67, 23, 45, 111, 67, 12, 55]
def remove(lst):
    lst1 = []
    for num in lst:
        if num not in lst1:
            lst1.append(num)
    return lst1

lst1 = remove(lst)
print(lst)
print(lst1)
