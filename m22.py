from collections import Counter

text = input("Enter some text: ")
words = text.split()
word_counts = Counter(words)
for word, count in sorted(word_counts.items()):
    print(word + ":" + str(count))
