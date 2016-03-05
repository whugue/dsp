# Hint:  use Google to find python function

from datetime import datetime

###a)
date_start = "01-02-2013"
date_stop = "07-28-2015"

print (datetime.strptime(date_stop,"%m-%d-%Y")-datetime.strptime(date_start,"%m-%d-%Y")).days #937 days


###b)
date_start = "12312013"
date_stop = "05282015"

print (datetime.strptime(date_stop,"%m%d%Y")-datetime.strptime(date_start,"%m%d%Y")).days #513 days


###c)
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'

print (datetime.strptime(date_stop,"%d-%b-%Y")-datetime.strptime(date_start,"%d-%b-%Y")).days #7850 days



