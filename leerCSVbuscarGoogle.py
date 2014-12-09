#!/usr/bin/env python
import csv
from pygoogle import pygoogle

reader = csv.reader(open('/Users/davidgalisteo/Desktop/scriptsPython/profesor_contrasena.csv', 'rb'))
writer = open('/Users/davidgalisteo/Desktop/scriptsPython/contrasenas.txt', "w")

hashes = [];

for row in reader:
    try:
        profesor = row[0]
        password = row[1]

    except IndexError:
        print 'index error'

    g = pygoogle(password)
    g.pages = 1

    if(g.get_result_count() > 0)
        print '*Hay %s resultados*'%(g.get_result_count())
        writer.write(profesor)
        writer.write('\n')
        writer.write(g.get_urls())
        hashes.append(password)
        writer.write('\n')

writer.close()
