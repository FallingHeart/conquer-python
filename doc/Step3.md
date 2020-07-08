# 元组、列表、字典

元组、列表、字典是最简单的数据结构。

## 元组()

元组是可以看做是不可变的列表，在赋值及字符串模板中特别好用。

```python
some_tuple = (6,'7')
a,b = some_tuple
print(a)
print(b)
# 6
# 7
print('digit %d str %s' % some_tuple)
# digit 6 str 7
```

## 列表[]

列表一般用来存放同类型数据，存放不同类型的推荐使用字典。

## 字典{}