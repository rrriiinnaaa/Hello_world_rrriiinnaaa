array = list(map(float, input("Введите числа массива через пробел: ").split()))

count = 0
i = 0
n = len(array)

while i < n:
    if array[i] > 0:
        count = count + 1
    i = i + 1

print("Количество положительных чисел:", count)