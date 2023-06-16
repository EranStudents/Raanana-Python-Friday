''''
כתוב תוכנית אשר קולטת 6 מספרים לתוך רשימה מהמשתמש
לאחר מכן מאחסנת אותם ברשימה חדשה בסדר הפוך ומדפיסה את 2 הרשימות אחת אחרי השנייה
'''

numbers2 = []
numbers = []
for i in range(6):
    num = int(input("Enter a number:"))
    numbers.append(num)

# numbers.reverse() הפעולה לא מחזירה שום דבר, בסך הכל מבצעת reverse

# אופציה 1 - של יונתן
for i in range(len(numbers) - 1, -1, -1):
    numbers2.append(numbers[i])

print(f'numbers = {numbers}')
print(f'numbers2 = {numbers2}')
