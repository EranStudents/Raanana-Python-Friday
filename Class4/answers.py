# שאלה 1

elements = [1, 6, 2, 'hello', '25', [4, 7, 8]]

print('With for loop:')
for element in elements:
    print(element)

print('With range loop:')
# הדפסה עם לולאת for עם range
for i in range(len(elements)):
    print(elements[i])

print('With while loop:')
# הדפסה עם לולאת while
i = 0
while i != len(elements):
    print(elements[i])
    i += 1

# שאלה 2

numbers = [45, 97, 56, 76, 43, 99]
sum_numbers = 0  # הולך להחזיק את סכום כל המספרים
for num in numbers:
    sum_numbers = sum_numbers + num

print(f'The avg is {sum_numbers / len(numbers)}')
