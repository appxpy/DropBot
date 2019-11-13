import random

def LoadHeader():
	f = open('UserAgents.txt', 'r')
	r = f.read()
	return(random.choice(r.split('\n')))
	
print('Using user agent:', LoadHeader())
