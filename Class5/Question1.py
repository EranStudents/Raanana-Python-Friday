'''
כתוב תוכנית אשר קולטת 7 מספרים מהמשתמש לתוך רשימה
עלייך לאחסן ברשימה רק את המספרים שגדולים מ-5 וקטנים מ-100
לאחר מכן התוכנית צריכה להדפיס רק את המספרים שגדולים מהממוצע של כל המספרים
'''

numbers = []
for i in range(7):
    num = int(input("Enter a number:"))
    if 5 < num < 100:
        numbers.append(num)

avg = sum(numbers) / len(numbers)

for i in numbers:
    if i > avg:
        print(i)
