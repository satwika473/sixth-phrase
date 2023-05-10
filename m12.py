even_nums = []

for num in range(1000, 3001):
    all_even_digits = True
    for digit in str(num):
        if int(digit) % 2 != 0:
            all_even_digits = False
            break
    if all_even_digits:
        even_nums.append(str(num))

print(",".join(even_nums))
