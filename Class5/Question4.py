'''
צור רשימה של 5 מספרים שהמשתמש נותן לכם
עליכם להדפיס את האינדקס (מיקום) של האיבר הגדול ביותר
ניתן להיעזר בפונקציית max

תזכורת:
max = זוהי פונקציה שמקבלת רשימה ומחזירה את מספר הגבוה ביותר בתוכה

'''

numbers = []
for i in range(5):
    num = int(input("Enter a number:"))
    numbers.append(num)

print(f'The index of the max number in the list is {numbers.index(max(numbers))}')