#!/usr/bin/python

fich= open("/etc/passwd","r")
userShells= {}
lineas= fich.readlines()
for linea in lineas:
	token = linea.split(':')
	userShells[token[0]] = token[-1]
	#print("User: " , token[0] , " Shell que utiliza: ", token [-1][:-1])
fich.close()

try:
	print('root', userShells['root'])
	print('imaginario', userShells['imaginario'])
except KeyError:
	print("Introduce un usuario existente")
