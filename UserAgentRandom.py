import random

def LoadHeader():
	f = open('UserAgent.txt', 'r')
	r = f.read()
	return(random.choice(r.split('\n')))
	
print('Using user agent:', LoadHeader())
