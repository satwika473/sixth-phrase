def generateArray(X, Y):
    array = []
    for i in range(X):
        row = []
        for j in range(Y):
            row.append(i * j)
        array.append(row)
    return array

# Prompt the user to enter X and Y
X = int(input("Enter X: "))
Y = int(input("Enter Y: "))

# Generate the 2-dimensional array
array = generateArray(X, Y)

# Print the array
for row in array:
    print(row)
