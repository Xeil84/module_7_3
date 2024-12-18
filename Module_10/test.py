def calculate_sum(*args):
    total_sum = 0

    for arg in args:
        if isinstance(arg, int):
            total_sum += arg
        elif isinstance(arg, str):
            total_sum += len(arg)
        elif isinstance(arg, (list, tuple, set)):
            total_sum += calculate_sum(*arg)
        elif isinstance(arg, dict):
            total_sum += calculate_sum(*arg.keys(), *arg.values())

    return total_sum

# Пример использования функции
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_sum(data_structure)
print(result)