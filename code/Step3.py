some_tuple = (6,'7')
a,b = some_tuple
print(a)
print(b)

print('digit %d str %s' % some_tuple)



some_str = 'yes,it is.'

some_list = ['y','e','s',',','i','t',' ','i','s','.']

print(len(some_str),len(some_list))
print(some_str[1],some_list[1])

some_list = ['y','e','s',',','i','t',' ','i','s','.']

some_set = set(some_list)
print(some_set)
# {'e', 'y', '.', 's', 't', ' ', 'i', ','}
