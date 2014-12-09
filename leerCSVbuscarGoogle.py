#!/usr/bin/env python
import csv
from pygoogle import pygoogle

reader = csv.reader(open('/Users/davidgalisteo/Desktop/scriptsPython/buscarGoogle/profesor_contrasena.csv', 'rb'))
writer = open('/Users/davidgalisteo/Desktop/scriptsPython/buscarGoogle/resultado.txt', "w")

#recorro todas las filas
for row in reader:
    #obtengo el profesor y el password
    profesor = row[0]
    password = row[1]

    #busco en google
    g = pygoogle(password)
    #seteo número de páginas
    g.pages = 1

    #si obtengo 1 o más resultados, los escribo en otro fichero
    if g.get_result_count() > 0
        print '*Hay %s resultados*'%(g.get_result_count())
        writer.write(profesor)
        writer.write('\n')
        writer.write(g.get_urls())
        writer.write('\n')

#cierro fichero
writer.close()
