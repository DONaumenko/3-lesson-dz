numbers = input('Введите несколько цифр: ')

# Переводим строковой ввод пользователя поэлементно в список list
list_of_chars = []
for char in numbers:
    list_of_chars.append(char)

# print(list_of_chars)

# Фомируем новый список из уникальных значений, удаляя из исходного списка символы (,;/)
unique_numbers = []
for number in list_of_chars:
    if number != ',' and number != ';' and number != '/':
        if number not in unique_numbers:
            unique_numbers.append(number)

# Расставляем пробелы после каждого итогового элемента списка для удобства восприятия
for final_numbers in unique_numbers:
    print(final_numbers, end=' ')
