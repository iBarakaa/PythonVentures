#simple program to assign grades to scores between 0.0 - 1.0 range and error handling
score = input("Enter Score: ")

try:
    fScore = float(score)
except:
    print("Enter numeric values")
    quit()

if fScore >= 0.0:
    if fScore <= 1.0:
        if fScore >= 0.9:
            print('A')
        elif fScore >= 0.8:
            print('B')
        elif fScore >= 0.7:
            print('C')
        elif fScore >= 0.6:
            print('D')
        else:
            print('F')
    else:
        print("Out of range, number greater than 1.0")
else:
    print('Out of range, number less than 0.0')

