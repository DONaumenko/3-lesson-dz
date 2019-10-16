quantity_of_numbers = int(input('Введите количество элементов списка'))
numbers = []

for i in range(0, quantity_of_numbers):
    number = int(input(f'Введите {i + 1} элемент'))
    numbers.append(number)

numbers.sort()
print(numbers)
