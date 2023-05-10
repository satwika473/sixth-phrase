binary_nums = input("Enter comma separated 4-digit binary numbers: ")
binary_list = binary_nums.split(",")

result = []
for num in binary_list:
    decimal = int(num, 2)
    if decimal % 5 == 0:
        result.append(num)

print(",".join(result))
