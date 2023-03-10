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

#function of continue statement
while True:
    line1 = input('Tell me> ')
    if line1[0] == '#':
        continue #stops iteration and reruns the loop from start
    if line1 == 'done':
        break
    print(line1)
print('Done!')

#definite loops
#these iterate through members of a set
for i in [5, 4, 3, 2, 1]: #for each value in the set
    print(i)
print('Blastoff!')

#string instance of loops
friends = ['Davies', 'Hassan', 'Aaron']
for friend in friends:
    print('Happy New Year: ', friend)
print('Done!')