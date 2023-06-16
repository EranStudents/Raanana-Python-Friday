'''
כתוב תוכנית אשר קולטת 5 מחרוזות לתוך רשימה
התוכנית תדפיס כפלט מחרוזת אחת אשר מורכבת מכל
המחרוזות שהאורך שלהן הוא מעל 4 ויש להן לפחות 'a' אחת במילה
'''

strings = []  # רשימה של מחרוזות
answer = ''
for i in range(5):
    text = input("Enter a text:")
    if len(text) >= 4 and text.count('a') > 0:
        answer = answer + text
    strings.append(text)

print(f'answer = {answer}')
