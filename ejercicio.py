#!/usr/bin/python
# -*- coding: utf-8 -*-

fichero = open("/etc/passwd", "r");
lineas = fichero.readlines();
fichero.close();
diccionario = {};

for linea in lineas:
	elemento = linea.split(":");
	usuario = elemento[0];
	shell = elemento[-1][:-1];
	diccionario[usuario] = shell
	print(usuario + ": " + shell);

print("El numero de usuarios es " + str(len(diccionario)));

#print("La shell de root es: " + diccionario["root"]);
#try:
#	print(diccionario["imaginario"]);
#except:
#	print "El nombre de usuario 'imaginario' no existe"