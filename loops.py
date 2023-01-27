#loops have iteration variables that change each time in the loop
n = 5
while n > 0:
    print(n)
    n = n - 1 
print('Blastoff!')
print(n)

#infinite loop
# n = 5
# while n > 0:
#     print('Lather')
#     print('Rinse')
# print('Dry off')
#uncomment the code to see the behaviour of an infinite loop

#instance of infinite loop exit 
while True: #infinite loop declaration
    line = input('Tell me> ')
    if line == 'done':
        break #prompts exit in an infinite loop
    print(line)
print('Done')