i = '1'
while True:
	i += '1'
	print(len(list(i)))
	if len(list(i)) == 10000:
		print(i)
		break