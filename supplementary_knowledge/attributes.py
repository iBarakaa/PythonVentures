a = ['Pentagram', 'Square', 'Pentagon']
a.insert(2, 'Circle') # insert is an attribute of list type 'a' hence this code is functional

print(a)

# however, insert in not an attribute of object type 'tuple'
# this results in an invalid reference
a = ('Pentagram', 'Square', 'Pentagon')
a.insert(2, 'Circle') # this results to an attribute error 
print(a)
