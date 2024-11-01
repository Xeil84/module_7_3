first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(lenta) for lenta in first_strings if len(lenta) >= 5]

second_result = [ (lenta, lenta2) for lenta in first_strings for lenta2 in second_strings if len(lenta) == len(lenta2)]

third_result = {lenta: len(lenta) for lenta in first_strings + second_strings if not len(lenta) % 2 }


print(first_result)
print(second_result)
print(third_result)