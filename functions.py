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
def greet(greeting):
    if greeting == 'Oe':
        print('Swahili')
    elif greeting == 'Koniichiwa':
        print('Japanese')
    elif greeting == 'Salut':
        print('French')
    elif greeting == 'Hello':
        print('English')
    elif greeting == 'Hola':
        print('Spanish')
    else:
        print('Sumn else')

tgreet = input("Greet me: ")
greet(tgreet)

#return value produces results
#you do not have to call return as it implicitly occurs as the last line of a function
#rewritting above code to greet somebody
def greet(lang):
    if lang == 'Swahili':
        return 'Niaje'
    elif lang == 'Japanese':
        return 'Koniichiwa'
    elif lang == 'Spanish':
        return 'Hola'
    elif lang == 'English':
        return 'Hello'
    elif lang == 'French':
        return 'Salut'
    else:
        quit()
    
tlang = input("Say hello in a language: ")
print(greet(tlang), 'Friend')
