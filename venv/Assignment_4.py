import datetime
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
today=datetime.now()
print(today)
wd = date.weekday(today)
day_name= ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat','Sun']
print ("Today is day number %d" % wd)
print ("which is a " + day_name[wd])
date=str(input('Enter the date(for example:09 02 2019):'))
day = datetime.strptime(date, '%d %m %Y').weekday()
print(day_name[day])