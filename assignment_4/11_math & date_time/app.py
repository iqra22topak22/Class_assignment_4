import time # This is required to include time module.
ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)

# ---------------------------------
import time
localtime = time.localtime(time.time())
print ("Local current time :", localtime)

# --------------------------------------
import time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

# ----------------------------------

import calendar
cal = calendar.month(2025, 1)
print ("Here is the calendar:")
print (cal)


# ----------------------------------------------

from datetime import date

date1 = date(2023, 4, 19)
print("Date:", date1)
date2 = date(2023, 4, 30)
print("Date2:", date2)

# ------------------------------------------------
import datetime

x = datetime.datetime(2025, 1, 1)

print(x.strftime("%f")) #Display Microsecond 000000-999999
print(x.strftime("%A")) #Display the name of the Day
print(x.strftime("%Y")) #Display the Year
print(x.strftime("%B")) #Display the name of the month


# ------------------------------------------------


import math

x = float('nan')
if math.isnan(x):
  print("x is NaN")