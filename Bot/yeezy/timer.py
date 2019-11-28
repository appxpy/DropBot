import datetime
def checktime():
	f = open('timerfile.txt', 'r')
	s = f.read()
	timelist = []
	strtimelist = s.split('*')
	for date in strtimelist:
		time = datetime.datetime.strptime(date,"%H:%M:%S")
		timelist.append(time)
	delta = timelist[1] - timelist[0]
	result = delta#datetime.timedelta(delta.seconds)
	f.close()
	open('timerfile.txt', 'w').close()
	return int(delta.total_seconds())
