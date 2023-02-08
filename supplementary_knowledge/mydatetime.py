# this datetime module works with date and time
# had initially name the file to "datetime.py" which caused me a circular import error upon calling the module in exe
import datetime

ldgsm = datetime.date(2001, 1, 17)
print(ldgsm.day)
