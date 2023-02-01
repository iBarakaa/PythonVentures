# return file object whence we input the name of the file and the mode (way we will work with the text file)
# r reads data into a file, whereas the write mode in the existing file will be overwritten
# append mode appends data into a file, where data is appended to the end of the file

#   using relative path
# file_object('relative path', 'r')

#   full path used
fullpath_of_file = r"C:\Users\Izaq Baraka\Desktop\Python Ventures\supplementary_knowledge\TextDocument.txt"
file_object = open(fullpath_of_file, 'r')

print(file_object.read()) 

# if we do not close objects properly, any further attempts to use the file will be failed
file_object.close()

# to go past issues that may arise upon not using the close function
# we can use the with statement as follows
# the result proves similar to the above code block
with open('supplementary_knowledge\TextDocument.txt', 'r') as f:
    print(f.read()) #   reads everything

with open('supplementary_knowledge\TextDocument.txt', 'r') as f:
    print(f.readlines()) #   reads line by line

with open('supplementary_knowledge\TextDocument.txt', 'r') as f:
    for line in f:
        print(line) #   lines are read seperately



