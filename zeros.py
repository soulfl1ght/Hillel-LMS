
lst = [12, 0, 5, 87, 9, 0, 0, 34, 2]

def qwer(lst):
    zeros_count = lst.count(0)
    lst = [num for num in lst if num != 0]
    lst.extend([0] * zeros_count)
    return lst
print(qwer(lst))