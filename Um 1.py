squares = [x**2 for x in range(1, 11)]
print(squares)
# Вывод: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

day_names = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
day_dict = {day: index + 1 for index, day in enumerate(day_names)}
print(day_dict)
# Вывод: {'Понедельник': 1, 'Вторник': 2, 'Среда': 3, 'Четверг': 4, 'Пятница': 5, 'Суббота': 6, 'Воскресенье': 7}

libraries = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
unique_tags = {lib.lower() for lib in libraries}
print(unique_tags)
# Вывод: {'django', 'fastapi', 'numpy', 'python', 'pandas', 'random'}
