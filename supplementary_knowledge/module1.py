print(f'Module 1 : {__name__}')

user = 'man'
level = 1

if __name__ == '__main__':
    print('I run directly')
else:
    #   this runs in other file as this file is imported there
    print('I did not run directly') 

