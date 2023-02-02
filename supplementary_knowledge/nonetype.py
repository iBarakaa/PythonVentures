import re

# search for the upper case character in word beginning and print the word
text = "I am the Last Dragon God Superman Sir"

# the different codeblocs result in errors
# they are meant for examining the errors and undesired blocks should be commented out temporarily to examine desired blocks 
# the initial instance of this code produces an error
for i in text.split():
    x = re.match(r"\bS\w+", i)
    print(x.group())

# attribute is any property associated with objects
# check attribute.py for further understanding

# 'nonetype' object has no attribute 'xyz'
# when trying to access None, it returns an unexpected output
x = None
print(x.insert) # this object has no attribute insert

# another instance of nonetype errors
def take(a):
    if a < 0:
        return a

y = take(5) # y = None in this case
print(y.func) # func attribute does not exist

