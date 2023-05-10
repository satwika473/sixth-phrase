# Get the input sequence of words from the user
input_str = input("Enter a comma-separated sequence of words: ")

# Split the input sequence into a list of words
words = input_str.split(',')

# Sort the list of words alphabetically
sorted_words = sorted(words)

# Print the sorted list of words as a comma-separated sequence
output_str = ','.join(sorted_words)
print(output_str)
