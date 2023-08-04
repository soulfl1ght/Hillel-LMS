def count_word(text):
    word_freq = {}
    words = text.split()
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq

def sorted_frequency(word_freq):
    freq_word_list = [(freq, word) for word, freq in word_freq.items()]
    sorted_freq_word_list = sorted(freq_word_list, key=lambda x: (-x[0], x[1]))
    for freq, word in sorted_freq_word_list:
        print(f"{word} {freq}")
n = int(input("Type the number of lines: "))

text = ""
for _ in range(n):
    text += input() + " "
word_freq = count_word(text)
sorted_frequency(word_freq)
