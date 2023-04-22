name = 'Eran Levy'
#       012345678

print(f'The length of my name is {len(name)}')

#  אם אני רוצה להגיע לתו מסוים בתוך המחרוזת

print(f'name[5] = {name[5]}')

print(f'name[9] = {name[9]}')

print(f'name[-1] = {name[-1]}')

'''
string_name [start(default=0):end(not included,default=end):step
name = 'Eran Levy'
'''

print(f'print(name[::2] = {name[::2]}')

print(f'print(name[::-1] = {name[::-1]}')

print(f'print(name[-3:] = {name[-3:]}')

'''
פונקציה מספר 1 - קוראים לה upper()
 אנו קוראים לפונקציה דרך מחרוזת
 ומה שהיא עושה זה פשוט הופכת את האותיות לאותיות גדולות
'''

print(name.upper())
# אותו הדבר כמו upper רק הופך לאותיות קטנות
print(name.lower())
print(name[0:5].upper())

'''

פונקציה מספר 3 - זוהי הפונקציה isupper()
מפעילים אותה על מחרוזת והיא מחזירה אמת או שקר לגבי האם היא אות גדולה
או לא מספיק שתו אחד הוא אות קטנה - הפונקציה תחזיר שקר
על מנת שהפונקציה תחזיר אמת - כל המחרוזת צריכה להיות עם אותיות גדולות
פונקציה מספר 4 - זוהי הפונקציה islower()
מפעילים אותה על מחרוזת והיא מחזירה אמת או שקר לגבי האם היא אות קטנה
 או לא מספיק שתו אחד הוא אות גדולה - הפונקציה תחזיר שקר
  על מנת שהפונקציה תחזיר אמת - כל המחרוזת צריכה להיות עם אותיות קטנות
'''

x = 'My name'
# x.upper()
x = x.upper()
print(x.isupper())

'''
את הפונקציה find אנו מפעילים על משתנה מסוג מחרוזת
ומה שהיא עושה זה מחזירה לך את המיקום של האות הראשונה של מה שאתה מחפש
ואם לא מצאת - הפונקציה תחזיר 1-

# Eran levy

'''

print(f'name.find("n") = {name.find("nn")}')

print(f'name.find("an") = {name.find("an")}')

print(f'name.find("er") = {name.find("er")}')

print(f'name.find("rn") = {name.find("rn")}')

'''
הפונקציה count (בעברית לספור) מופעלת על מחרוזת ומה שהיא מקבלת זה תת מחרוזת
ומה שהיא מחזירה זה את כמות המופעים שלה - כלומר כמות הפעמים שהיא מופיעה
'''

print(f'name.count("EE") = {name.count("EE")}')
print(f'name.count("E") = {name.count("E")}')
print(f'name.count(" ") = {name.count(" ")}')

print(f'name[::2].count("e") = {name[::2].count("e")}')
