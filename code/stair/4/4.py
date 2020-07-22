import numpy as np

some_list = [1, '2', 3, '4']
some_array = np.array(some_list)

print(some_array)
# ['1' '2' '3' '4']

some_list = [1, 2, 3, 4]
some_array = np.array(some_list)

print(some_array)
# [1 2 3 4]


import pandas as pd

some_list = [1, 2, 3, 4]
some_series = pd.Series(some_list)

print(some_series)


import pandas as pd

some_list = [
    [1, 2, 3, 4], 
    [5, 6, 7, 8], 
    [9, 10, 11, 12], 
    [13, 14, 15, 16]
]
some_dataframe = pd.DataFrame(some_list)

print(some_dataframe)
print(some_dataframe[1][2])

import numpy as np
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = np.mean(speed)
print(x)
x = np.median(speed)
print(x)
x = stats.mode(speed)
print(x)
print(x.mode,x.count)
x = np.std(speed)
print(x)
x = np.var(speed)
print(x)
x = np.percentile(speed, 75)
print(x)