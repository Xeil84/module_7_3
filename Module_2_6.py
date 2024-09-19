n = int(input('Здравствуйте! Введите число от 3 до 20:'))
q = []
for i in range(1, n + 1):
    one = []
    one.append(i)
    for j in range(0, n + 1):
        two = []
        two.append(j)
        if (n % (i + j)) == 0:
            if i == j or j == n or i == n or j < i:
                continue
            else:
                q.append(i)
                q.append(j)

print(n,'-', *(q))