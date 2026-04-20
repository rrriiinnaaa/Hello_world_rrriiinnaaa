array = list(map(int, input("Введите числа массива через пробел: ").split()))

summa = 0
i = 0
n = len(array)

while i < n:
    if array[i] % 2 != 0:
        summa = summa + array[i]
    i = i + 1

print("Сумма нечётных элементов:", summa)