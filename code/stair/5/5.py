import numpy
x = numpy.random.uniform(0.0, 5.0, 10)
print(x)
y = numpy.random.normal(5.0, 1.0, 10)
print(y)

import matplotlib.pyplot as plt
plt.hist(x, 5)
plt.show()
plt.scatter(x, y)
plt.show()
plt.plot(x, y)
plt.show()

import matplotlib.pyplot as plt
from scipy import stats
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
slope, intercept, r, p, std_err = stats.linregress(x, y)
def mymodel(x):
  return slope * x + intercept
some_map = map(mymodel, x)
print(some_map)
line_y = list(some_map)
print(line_y)
line_x = x
plt.scatter(x, y)
plt.plot(line_x, line_y)
plt.show()
print(r)
print(r**2)
speed = mymodel(10)
print(speed)

import numpy
import matplotlib.pyplot as plt
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
some_array = numpy.polyfit(x, y, 3)
print(some_array)
mymodel = numpy.poly1d(some_array)
print(mymodel)
line_x = numpy.linspace(1, 22, 100)
line_y = mymodel(line_x)
plt.scatter(x, y)
plt.plot(line_x, line_y)
plt.show()
from sklearn.metrics import r2_score
r = r2_score(y, mymodel(x))
print(r)
speed = mymodel(17)
print(speed)