# this datetime module works with date and time
# had initially name the file to "datetime.py" which caused me a circular import error upon calling the module in exe
import datetime

ldgsm_birth = datetime.date(2001, 1, 17)
print(ldgsm_birth)

# timedelta object aids in increasing and decreasing dates
# +ve no. increases
# -ve no. decreases
ldgsm_at_100days_old = datetime.timedelta(100)
print(ldgsm_at_100days_old + ldgsm_birth)

hundredDays_before_ldgsm_birth = datetime.timedelta(-100)
print(hundredDays_before_ldgsm_birth + ldgsm_birth)