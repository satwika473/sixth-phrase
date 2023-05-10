s = input("Enter a sentence: ")
letters = 0
digits = 0
for char in s:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
print("LETTERS", letters)
print("DIGITS", digits)
