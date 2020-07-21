import pandas as pd

some_list = [
    {
        'num':'1',
        'name':'xiaoming',
        'age':16
    },
    {
        'num':'2',
        'name':'dawang',
        'age':21
    }
]
df = pd.DataFrame(some_list)
df.to_csv('result.csv',index=0)