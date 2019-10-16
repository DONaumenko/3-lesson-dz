first_list_of_numbers = input('Введите первый список цифр: ')
second_list_of_numbers = input('Введите второй список цифр: ')

final_list_of_numbers = []
for number in first_list_of_numbers:
    if number not in second_list_of_numbers:
        final_list_of_numbers.append(number)

for formatted_numbers in final_list_of_numbers:
    print(formatted_numbers, end=' ')

# Проверил на данных ниже
# 1,2,3,4,5,6
# 2,5
# 1 3 4 6

# 1,3,5,4,1,3,5,2,2
# 2,5
# 1 3 4 1 3

# 3,3,3,4,1,1,2,6,9,3,1
# 2,5,1,6
# 3 3 3 4 9 3
