import pandas as pd
some_data_frame = pd.read_csv('sample.csv')
print(some_data_frame)

some_dict = some_data_frame.to_dict()
print(some_dict)
print(some_dict['name'][1])

some_dict = some_data_frame.to_dict('list')
print(some_dict)
print(some_dict['name'][1])


import requests
some_result = requests.get('https://api.bamo.tech/v0/cosmetic/mostUsedCF?top=5')
print(some_result)

some_json = some_result.json()
print(some_json)

some_list = some_json['list']
print(some_list)
print(some_list[0])