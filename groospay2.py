#simple conditional statement to give employee 1.5 times the hourly rate for hours worked above 40 hours
hrs = input("Enter hours: ")
rte = input('Enter rate per hour: ')

try:
    ihrs = float(hrs)
    irte = float(rte)
except:
    ihrs 

if ihrs <= 40:
    gp = ihrs * irte
    print("The gross pay is: ",gp)
elif ihrs > 40:
    gp = (40 * irte) + ((ihrs - 40)*(irte * 1.5))
    print("The gross pay is: ",gp)