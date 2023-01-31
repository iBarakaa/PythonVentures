x = 6
print(x) #simple outputting in python

#in python you cannot use Reserved Words as variable names / identifiers
#the larger the program(sequence of steps to be done in order), the more useful the use of 'scripts'
#there are sequential steps, conditional steps (involvement of paths), and repeated steps (until an exit condition is met)

#the operations may look mathematical but they aren't. Instead, they are computational; where the rhs is processed into the lhs
x = 4 * x * (1-x)
print(x)

#in python '**' stands for raised to the power of
print(5 ** 3)

#in python, we regard operator precendence
# this is the order of operation precedence
# 1. Parentheses 2. Exponentiation (power) 3. * ,/ ,% 4. +, - 5. Left to Right
#integer division in python 3.0 results in floating point numbers
x = 1 + 2 ** 3 / 4 * 5
print(x)

#in strings, '+' is used to concatenate
rizz = "I " + "Trasncend " + "All"
print(rizz)

#traceback usually means 'I quit' in python language, where the program does not want to go any further due to error introduced

#through the type() function we can check the type of variable
type(rizz)
type(x)

#the float() function can be used to convert integers into floating point numbers
f = float(x)
print(f)

# the int() function can convert string digits into integer values to allow math ops
sval = '1738'
ival = int(sval)
print(ival + 1)

#input() function returns a string
nme = input('pssst!?')
print('Hello Mr. ', nme)
