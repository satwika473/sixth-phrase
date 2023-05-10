lst = [1,2,3,4,5,6,7,8,9,10]

squared_even_lst = list(map(lambda x: x**2, filter(lambda x: x%2 == 0, lst)))

print(squared_even_lst)
