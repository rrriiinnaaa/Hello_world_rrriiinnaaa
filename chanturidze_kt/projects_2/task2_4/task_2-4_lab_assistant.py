volume = float(input("Введите нужный объем физиологического раствора (мл): "))

salt_mass = volume * 0.009

salt_mass_rounded = round(salt_mass, 2)

water_volume = volume

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-" * 23 + "\n")
    file.write(f"Общий объем: {volume:.2f} мл\n")
    file.write(f"Масса соли: {salt_mass_rounded:.2f} г\n")
    file.write(f"Объем воды: {water_volume:.2f} мл\n")

print(f"\n Рецепт сохранен в файл recipe.txt")
print(f"Масса соли: {salt_mass_rounded:.2f} г (округлено)")
