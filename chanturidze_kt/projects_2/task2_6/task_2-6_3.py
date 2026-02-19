donor = input("Введите группу крови донора (I, II, III, IV): ")
recipient = input("Введите группу крови пациента (I, II, III, IV): ")

valid_groups = ["I", "II", "III", "IV"]

if donor not in valid_groups or recipient not in valid_groups:
    print("Ошибка! Группы крови должны быть I, II, III или IV.")
else:
    if donor == recipient:
        print(f" Можно переливать: группа {donor} совпадает с группой пациента {recipient}")
    elif donor == "I":
        print(f" Можно переливать: донор с I (0) группой — универсальный донор для пациента с {recipient} группой")
    else:
        print(f" Нельзя переливать: группа донора {donor} не совместима с группой пациента {recipient}")