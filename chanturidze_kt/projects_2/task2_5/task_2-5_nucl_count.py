dna = input("Введите последовательность ДНК: ").upper()

print("\n=== Анализ последовательности ДНК ===\n")

print("Последовательность в верхнем регистре:", dna, "\n")

count_A = dna.count("A")
count_T = dna.count("T")
count_G = dna.count("G")
count_C = dna.count("C")

total = len(dna)

print("Подсчёт нуклеотидов:")
print("A:", count_A)
print("T:", count_T)
print("G:", count_G)
print("C:", count_C)

print("\nОбщая длина:", total, "нуклеотидов")

print("\nПроцентное содержание:")
print("A:", count_A / total * 100, "%")
print("T:", count_T / total * 100, "%")
print("G:", count_G / total * 100, "%")
print("C:", count_C / total * 100, "%")