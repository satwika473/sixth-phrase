# function to sort a list of tuples by ascending order of name, age and score
def sort_tuples(tuples_list):
    return sorted(tuples_list, key=lambda x: (x[0], int(x[1]), int(x[2])))

# main program to take input and call the sorting function
if __name__ == '__main__':
    input_list = []
    while True:
        user_input = input().strip()
        if not user_input:
            break
        name, age, score = user_input.split(',')
        input_list.append((name, age, score))

    sorted_list = sort_tuples(input_list)
    print(sorted_list)
