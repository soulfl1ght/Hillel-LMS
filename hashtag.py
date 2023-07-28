import string

def format_hash(sentence1):
    sentence = ''.join(char for char in sentence1 if char not in string.punctuation)
    words = sentence.split()
    hashtag = "#"
    for word in words:
        hashtag += word.capitalize()
    hashtag = hashtag[:140]

    return hashtag

sentence1 = input("Введіть рядок: ")
hashtag = format_hash(sentence1)
print(hashtag)
