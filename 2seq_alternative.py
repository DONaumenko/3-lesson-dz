numbers = input('Введите несколько цифр: ')
unique_numbers = []
for number in numbers:
    if number != ',' and number != ';' and number != '/':
        if number not in unique_numbers:
            unique_numbers.append(number)

for final_numbers in unique_numbers:
    print(final_numbers, end=' ')
