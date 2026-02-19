seq_list = ["ATATACGCGTA", "CTTCGGNGGA"]

for sequence in seq_list:
    print("\nПоследовательность:", sequence)
    print("Построчный вывод:")
    for letter in sequence:
        print(letter)

print("\nЦикл выполнен")