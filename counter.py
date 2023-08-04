def count_characters(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1

    return char_count
input_string = input("Type string: ")
result = count_characters(input_string)
for char, count in result.items():
    print("Result:")
    print(f"{char}, {count}")
