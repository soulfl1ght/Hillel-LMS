with open('month.txt', 'r') as file:
    content = file.read()
    words = content.split()
    word_count = len(words)

with open('month_reversed.txt', 'w') as file:
    reversed_words = reversed(words)
    reversed_content = ' '.join(reversed_words)
    file.write(reversed_content)

print(f"Words amount: {word_count}")
print("A file month_reversed.txt was created.")
