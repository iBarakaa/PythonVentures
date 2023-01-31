# learning about the meaning of if__main

# the value of __name__ is __main__ because it has run directly and not imported from another source file
# before python interpreter reads files, two things are done
    #1. setting of special variables like __name__ 
    #2. executing the file line by line
print(f'Game File: {__name__}') 

def run():
    print('Game Starts')

# if __name__ == '__main__':
#     pass