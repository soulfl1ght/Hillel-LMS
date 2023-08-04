def common_keys(dict1, dict2):
    keys_set = set(dict1.keys()) & set(dict2.keys())
    keys_list = list(keys_set)
    print(' '.join(keys_list))

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}
common_keys(a, b)
