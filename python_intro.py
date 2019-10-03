def hola():
	people=['Kike', 'Elvira', 'Lola']
	for name in people:
		hi(name)
		print('Next')

def hi(name):
	print('Hola ' + name + '!')

hola()