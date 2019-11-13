import random

def RandomProxy():
	f = open('proxies.txt', 'r')
	r = f.read()
	return(random.choice(r.split('\n')))
	
print('Using proxy:', RandomProxy())
