# this datetime module works with date and time
# had initially name the file to "datetime.py" which caused me a circular import error upon calling the module in exe
# default format is the yyyy-mm-dd format
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

# to create custom formats we create format code
# day-name, month-name day no., year - custom format
# method 1 (strftime method), where %A - day of the week name, %B - month name, %d - day in the month, %Y - yr
print(ldgsm_birth.strftime("%A, %B %d, %Y"))

# method 2
message = "The LDGSM was born on {:%A, %B %d, %Y} "
print(message.format(ldgsm_birth))

# object creation using classes in datetime 
fly_day = datetime.date(2023, 5, 17)
print(fly_day)

# hours minutes and seconds
fly_time = datetime.time(0, 30, 0)
print(fly_time)

# concatenation of date and time classes
# you can access all from this one
fly_datetime = datetime.datetime(2023, 5, 17, 0, 30, 0)
print(fly_datetime)

