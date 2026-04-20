n = int(input("Введите N: "))

summa = 0
i = 1

while i <= n:
    summa = summa + i
    i = i + 1

print(f"Сумма чисел от 1 до {n}: {summa}")