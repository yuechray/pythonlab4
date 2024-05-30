def write_and_read_even_lines(text, filename):
    with open(filename, "a+") as file:
        file.write(text + "\n")

    with open(filename, "r") as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            if index % 2 != 0:  # четные строки (нумерация с 0, по факту это нечетный индекс)
                print(line.strip())


write_and_read_even_lines("Пример текста", "example.txt")
# Вывод из четных строк файла будет, если они существуют.
