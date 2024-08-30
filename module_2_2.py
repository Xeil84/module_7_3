first = int(input('Напишите первое число:'))
second = int(input('Напишите второе число:'))
third = int(input('Напишите третье число:'))
if first == second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else: print(0)