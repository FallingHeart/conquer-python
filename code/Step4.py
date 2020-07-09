age = 20
if age >= 18:
    print('adult')
else:
    print('child')

    
some_list = ['a','b']
for i in some_list:
    print(i)

some_list = [
    {'name':'xiaomin','age':12},
    {'name':'dawang','age':20},
]

for i in some_list:
    print(i['name'],i['age'])

for i in some_list:
    if i['age']>18 :
        print('%s is an adult.' % i['name'])
    else:
        print('%s is a child.' % i['name'])