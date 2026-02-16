name = "Карина"
age = 18
city = "Санкт-Петербург"
occupation = "Студент"
hobby = "Программирование"
f = open("output.txt", "w", encoding="utf-8")
print(f"Меня зовут {name}, мне {age} лет, я живу в городе {city} и я {occupation}. Моё хобби {hobby}", file=f)
