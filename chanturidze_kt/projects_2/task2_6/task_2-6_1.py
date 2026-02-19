user_input = input("Введите значение pH (от 0 до 14): ")
pH = float(user_input)

if pH < 7:
    print(f"pH = {pH} — это кислая среда")
elif pH > 7:
    print(f"pH = {pH} — это щелочная среда")
else:
    print(f"pH = {pH} — это нейтральная среда")