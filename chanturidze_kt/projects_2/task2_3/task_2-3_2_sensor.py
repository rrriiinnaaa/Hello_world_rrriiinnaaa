operator_name = input("Введите имя оператора: ")
pressure_value = input("Введите текущее значение давления (Па): ")

with open("sensor_log.txt", "a", encoding="utf-8") as file:
    file.write(f"{operator_name}\t{pressure_value} Па\n")

print("\nДанные успешно сохранены в sensor_log.txt")
