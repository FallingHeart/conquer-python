import pandas as pd
some_data_frame = pd.read_csv('sample.csv')
print(some_data_frame)

some_dict = some_data_frame.to_dict()
print(some_dict)
print(some_dict['name'][1])

some_dict = some_data_frame.to_dict('list')
print(some_dict)
print(some_dict['name'][1])