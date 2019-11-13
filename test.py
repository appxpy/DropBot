filepath = 'user-agentschh.txt'
outpath = 'user-agents.txt'
f = open(filepath, 'r')
r = f.read()
useragents = r.split('\n')
print(len(useragents))
it = 1
for x in useragents:
	if 'Chrome' in x and 'Apple' in x and 'KHTML' in x:
		print('OK! Iteration number:',it)
		it += 1
	else:
		print('Not ok. Iteration number:', it)
		it += 1
		useragents.remove(x)
print(len(useragents))
f = open(outpath, 'w')
f.write('\n'.join(useragents))
f.close

