researcher_name = input("Введите ФИО исследователя: ")
experiment_date = input("Введите дату (в формате ДД.ММ.ГГГГ): ")
experiment_name = input("Введите название эксперимента: ")
experiment_conclusion = input("Введите вывод (результат эксперимента): ")

with open("journal.txt", "w", encoding="utf-8") as file:
    file.write("ЭЛЕКТРОННЫЙ ЛАБОРАТОРНЫЙ ЖУРНАЛ\n")
    file.write("=" * 60 + "\n\n")

    file.write("Поле\t\tЗначение\n")
    file.write("-" * 40 + "\n")
    file.write(f"ФИО исследователя\t{researcher_name}\n")
    file.write(f"Дата\t\t{experiment_date}\n")
    file.write(f"Эксперимент\t{experiment_name}\n")
    file.write("-" * 40 + "\n\n")

    file.write("РЕЗУЛЬТАТЫ ЭКСПЕРИМЕНТА:\n")
    file.write("-" * 40 + "\n")
    file.write(f"{experiment_conclusion}\n")
    file.write("-" * 40 + "\n")

print("\n Данные успешно сохранены в journal.txt")