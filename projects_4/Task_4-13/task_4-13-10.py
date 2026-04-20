array = list(map(float, input("Введите числа массива через пробел: ").split()))

summa = 0
i = 0
n = len(array)

while i < n:
    if i % 2 != 0:
        summa = summa + array[i]
    i = i + 1

print("Сумма элементов с нечётными индексами:", summa)