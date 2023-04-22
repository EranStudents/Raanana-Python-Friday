age = 29
name = 'Eran'

print(type(age))  # ידפיס את סוג המשתנה

print(f'Hello my name is {name} and my age is {age}')
print('Hello my name is', name, 'and my age is', age)

if name == 'Eran':
    print('This is my name')
if age > 10:
    print('Bigger then 10')

if name == 'Eran':
    print('This is my name')
elif age > 10 or age < 50:
    print('Bigger then 10')

age = 29
name = 'Eran'

if name == 'Eran':
    if age > 50 or age < 30:
        print(f'My name is {name}')
        if age > 50:
            print('hello')
        else:
            print('Im')
    else:
        print(f'My age is {age}')
else:
    print('Hello world')




