from datetime import timedelta
from dateutil.parser import *
def checktime():
	f = open('timerfile.txt', 'r')
	s = f.read()
	timelist = []
	strtimelist = s.split('*')
	for date in strtimelist:
		time = datetime.strptime(date,"%H:%M:%S")
		timelist.append(time)
	min
delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
