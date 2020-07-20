import mymodule
mymodule.a_function()
print(mymodule.a_str)

from mymodule import a_function
from mymodule import a_str
a_function()
print(a_str)

import mymodule as md
md.a_function()
print(md.a_str)