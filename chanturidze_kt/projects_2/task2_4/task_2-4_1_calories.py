protein = float(input("Введите массу белков в продукте (г): "))
fat = float(input("Введите массу жиров в продукте (г): "))
carbohydrates = float(input("Введите массу углеводов в продукте (г): "))

calories = (protein * 4) + (fat * 9) + (carbohydrates * 4)

print(f"\nОбщая калорийность продукта: {calories:.2f} ккал")

print(f"\nДетализация калорийности:")
print(f"  - Белки ({protein} г): {protein * 4:.2f} ккал")
print(f"  - Жиры ({fat} г): {fat * 9:.2f} ккал")
print(f"  - Углеводы ({carbohydrates} г): {carbohydrates * 4:.2f} ккал")