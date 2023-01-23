#flowcharts aid in the understanding of conditional statements
#conditional statements always follow the order the code was written, bear this in mind
# basic if then else conditionals
x = 0
y = 10

if 0 == x:
    if y == 10:
        print('Yes')
    else:
        print('Damn son')
else:
    print('Damn son')

#try / except structure
#surrounds dangerous sections of code 
#if code in try block works, the except section is skipped
#if code in try block fails, except block is executed

#code explanation of try/except structure
x = input("Enter working or not working: ")

if x == 'working':
    print('Working code, skip except block')
elif x == 'not working':
    print('Error in code, Jump to except block')
else:
    print('INVALID')

#actual use of the try except structure
#code execution halts upon the point of traceback, hence we should only put 'dangerous' code in the structure
#the structure prevents tracebacks from outputting where they are expected to
str = input("Enter a number: ")
try:
    ival = int(str)
except:
    ival = -1

if ival > 0:
    print('Wow, what a number... SSIIIIUUU')
else:
    print('NaN')