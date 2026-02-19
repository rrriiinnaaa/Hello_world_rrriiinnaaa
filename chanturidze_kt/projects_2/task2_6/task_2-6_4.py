print("Выбери путь:")
print("1 - налево")
print("2 - направо")
print("3 - прямо")
print("4 - назад")

choice = float(input("Твой выбор: "))

if choice == 1:
    print("Потерял коня")
elif choice == 2:
    print("Женился")
elif choice == 3:
    print("Погиб в бою")
elif choice == 4:
    print("Вернулся домой")
else:
    print("Нет такого пути")