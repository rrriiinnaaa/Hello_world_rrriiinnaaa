n = int(input("Введите N: "))

summa = 0
i = 1

while i <= n:
    summa = summa + i * i
    i = i + 1

print(f"Сумма квадратов от 1² до {n}²: {summa}")