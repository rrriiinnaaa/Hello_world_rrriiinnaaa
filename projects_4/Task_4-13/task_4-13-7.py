array = list(map(float, input("Введите числа массива через пробел: ").split()))

summa = 0
i = 0
n = len(array)

while i < n:
    summa = summa + array[i]
    i = i + 1

average = summa / n

print("Среднее арифметическое:", average)