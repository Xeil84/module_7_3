# Cписковая сборка (list comprehension)
list_ = [value if value % 2 == 0 else None for value in range(6)]
print(list_)

# Полный аналог списковой сборки
list_ = []
for value in range(6):
    if value % 2 == 0:
        list_.append(value)
    else:
        list_.append(None)
print(list_)

# Операция сборки во множество
set_ = {value if value % 2 == 0 else None for value in range(6)}
print(set_)

# Операция сборки в словарь
dict_ = {value: None if value % 2 == 0 else None for value in range(6)}
print(dict_)

# Фильтрация данных перед помещением в список (Отбрасываем те значения, которые не прошли проверку if)
list_ = [value for value in range(6) if value % 2 == 0]
print(list_)

"""
Протокол итератора:
1) __iter__: при вызове возвращается итератор
2.1) __next__: возвращается следующий элемент итератора, если такого больше нет, то вызов StopIteration
2.2) Исключение StopIteration

Итерируемый объект: тот объект, в котором присутствует магический метод __iter__
Пример: list_ = [1,2,3]
list_ является итерируемым объектом
Итератор: тот объект, в котором присутствует магический метод __next__
Пример: list_ = [1,2,3]
iterator = iter(list_) 
iterator является итератором

2 встроенные функции по работе с протоколом:
1) iter() возвращает итератор от итерируемого объекта
2) next() возвращается следующий элемент от итератора
Они используются, чтобы напрямую не обращаться к соответствующим магическим методам.
"""

# Проверка на наличие методов и атрибутов - функция dir()
print(dir(list_))

# От одного итерируемого объекта возможно создать несколько итераторов
iterator1 = iter(list_)
iterator2 = iter(list_)


# Стандартный вызов for
for value in list_:
    print(value, end=' ')

print()

# Внутренняя реализация цикла for
iterator = iter(list_)
while True:
    try:
        value = next(iterator)
        print(value, end=' ')
    except StopIteration:
        break


class Iterat:
    """
    Реализация Протокола Итератора в собственном классе
    """

    def __init__(self):
        self.value = 0
        self.stop = 3

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value >= self.stop:
            self.value = 0
            raise StopIteration
        current = self.value
        self.value += 1
        return current


it = Iterat()

for value in it:
    print(value, end=' ')
print()
for value in it:
    print(value, end=' ')


"""
Генератор
Работает по Протоколу Итератора
next(), StopIteration

Каждый Генератор является Итератором,
но не каждый Итератор является Генератором

Главное отличие от Итератора заключается в способе выдачи данных.
Основное преимущество Генератора заключается в возможности обрабатывать большое количество данных, занимая малое пространство памяти.
В то время как для стандартного Итератора потребуется предварительно выделить память для хранения всех данных целиком.

1) Вариант создания Генератора
Генераторная сборка
"""
gen_ = (value for value in range(3))
print('\n', gen_)
print(type(gen_), '\n')  # Генератор


def gen_func():
    """
    2) Вариант создания Генератора
    Генераторная функция
    Ключевое отличие от стандартной функции - наличие оператора yield
    """
    for value in range(3):
        yield value


gen_ = gen_func()
print('\n', gen_)
print(type(gen_), '\n')  # Генератор

# Методы по работе с генератором:
# 1)
gen_ = gen_func()
print(list(gen_))
# 2)
gen_ = gen_func()
try:
    next(gen_)
except StopIteration:
    pass
# 3)
gen_ = gen_func()
for value in gen_:
    print(value)
