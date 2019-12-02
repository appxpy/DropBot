f = open('config.txt', 'r', encoding='utf-8')
list = f.readlines()
for x in list:
	x.replace('\n', '')
for x in list:
	print(x, 'has index', list.index(x))
	print('--------------------------------------------------')

