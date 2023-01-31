#   learning about the meaning of if__main

#   when we import files, we read the source file and sets __name__ for the file
from module1 import user
#   the value of __name__ is __main__ because it has run directly and not imported from another source file
#   before python interpreter reads files, two things are done
    #   1. setting of special variables like __name__ 
    #   2. executing the file line by line
print(f'Game File: {__name__}') 

def run():
    print('Game Starts')

#   tests if file is run directly or being imported
#   decide whether to run code when imported from py file
if __name__ == '__main__':
    run()   

#   this helps with deciding whether we are dealing with main execution files or modules that aid in dev
