# use of the if else blocks and the use of the try and except blocks

import re

x = None
if x is not None:
    x.something = 'Geronimooo!'
else:
    print('x is a None type object')

# use of the try and except block
def take(a):
    if a < 0:
        return a

x = take(-1)
y = take(5)

try:
    print(x)
    print(y.something())
except AttributeError:
    print('No such Attribute!')

text = "I am the Last Dragon God Superman Sir"

# dealing with no attribute group
# try-except will help us neglect the function group where x returns none
for i in text.split():
    x = re.match(r"\bS\w+", i)

    try:
        print(x.group())
    except AttributeError:
        continue # program flow will move onto the next iteration 
    