#Найди индексы первого вхождения максимального элемента.
# Выведи два числа: номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве.
# Если таких элементов несколько, то выводится тот, у которого меньше номер строки, а если номера строк равны то тот, у которого меньше номер столбца.


n = int(input())
m = int(input())
a = []
d = []
max = -123
for w in range(m):
    x = input().split()
for s in range(n):
    d. append(a)
for h in range(len(d)):
    for r in range(len(d[h])):
        d[h][r] = int(d[h][r])
        if d[h][r]>max:
            max = d[h][r]
            print(max)
print(d.index(max))