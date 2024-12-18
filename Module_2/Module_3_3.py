def print_params(a = 1, b = 'привет', c= True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ('ole', 4, False)
values_dict = {'a': 5, 'b': 'mono', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ('max', 88)
print_params(*values_list_2,42)


