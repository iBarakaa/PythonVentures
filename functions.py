# There are two types of functions, Built-in functions and Programmer-Defined function

 #instance of max() function - prints largest character in string
big = max('Hello world')
print(big) #'w' is printed as it is the largest character in the string

#def allows for rememberance of the code written within it to be invoked for later
#instance of use-case of def keyword
def print_lyrics():
    print('My name is Martian...')
    print("I'm out this world")
    print("'S' on my chest, Superman!!")

print("My name is.. My name is..")
print_lyrics()

#arguments are values passed into the function as input upon invocation
#parameters are variables used in function block to allow access to arguments
#simple language checker program for greetings
def greet(lang):
    if lang == 'Oe':
        print('Swahili')
    elif lang == 'Koniichiwa':
        print('Japanese')
    elif lang == 'Salut':
        print('French')
    elif lang == 'Hello':
        print('English')
    elif lang == 'Hola':
        print('Spanish')
    else:
        print('Sumn else')

tgreet = input("Greet me: ")
greet(tgreet)