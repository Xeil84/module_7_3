def is_prime(func):
    def surrogate(*args, **kwargs):
        result = func(*args, **kwargs)
        for i in range(2, int(result**0.5)+1):
            if result % i == 0:
                return f'Составное\n{result}'
            else:
                return f'Простое\n{result}'
    return surrogate


@is_prime
def sum_three(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


result = sum_three(2, 3, 6)
print(result)