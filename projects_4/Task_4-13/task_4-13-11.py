array = list(map(float, input("Введите числа массива через пробел: ").split()))

summa = 0
count = 0
i = 0
n = len(array)

while i < n:
    if i % 2 == 0:
        summa = summa + array[i]
        count = count + 1
    i = i + 1

if count > 0:
    average = summa / count
    print("Среднее арифметическое (чётные индексы):", average)
else:
    print("Нет элементов с чётными индексами")