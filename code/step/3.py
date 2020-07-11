some_tuple = (6,'7')
a,b = some_tuple
print(a)
print(b)
print('digit %d str %s' % some_tuple)

some_str = 'yes,it is.'
some_list = ['y','e','s',',','i','t',' ','i','s','.']
print(len(some_str),len(some_list))

some_tuple = (6,'e')
some_str = 'yes.'
some_list = ['y','e','s','.']
print(some_tuple[1],some_str[1],some_list[1])

some_list = ['y','e','s']
some_list[0] = 'Y'
print(some_list)

some_list = ['y','e','s',',','i','t',' ','i','s','.']
some_set = set(some_list)
print(some_set)

s1 = {1,2,3}
s2 = {2,3,4}
print(s1 & s2)
print(s1 | s2)

some_dict = {
    'num':1,
    'msg':'ok',
    'some_list':[],
    'some_dict':{},
    'freezed':False
}

some_msg = some_dict['msg']
print(some_msg)

some_dict['some_key'] = 'lalala'
print(some_dict)