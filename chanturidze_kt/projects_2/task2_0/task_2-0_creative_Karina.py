course = 1
current_year = 2026
border = "┌" + "─" * 40 + "┐"
middle = "│" + " " * 40 + "│"
bottom = "└" + "─" * 40 + "┘"
print(border)
print( " " * 9 + "🌟 Добро пожаловать 🌟" + " " * 12)
print(middle)
info = f"│ Студент {course} курса {current_year} года │"
print(" " * ((40 - len(info) + 4) // 2) + info + " " * ((40 - len(info) + 4) // 2))
print(middle)
print(" " * 8 + "🎓 Удачи в обучении! 🎓" + " " * 8)
print(bottom)