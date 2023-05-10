def print_first_five_squares():
    square_list = []
    for i in range(1, 21):
        square_list.append(i ** 2)
    print(square_list[:5])
