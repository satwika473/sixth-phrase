# Get the sequence of lines from the user
input_lines = []
while True:
    line = input("Enter a line of text (or 'done' to finish): ")
    if line == 'done':
        break
    input_lines.append(line)

# Convert each line to uppercase and print them
for line in input_lines:
    print(line.upper())
