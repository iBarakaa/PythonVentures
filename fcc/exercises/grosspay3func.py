#computepay() to do grosspay computation
def computepay(hours, rph):
    if hours > 40:
        grosspay = (40 * rph) + ((hours-40) * (1.5 * rph))
        return grosspay
    elif hours <= 40:
        grosspay = (hours * rph)
        return grosspay

hours = input("Enter hours: ")
rph = input("Enter hourly rate: ")

try:
    fhours = float(hours)
    frph = float(rph)
except:
    print('Please enter numeric values')
    quit()

print('Pay', computepay(fhours, frph))