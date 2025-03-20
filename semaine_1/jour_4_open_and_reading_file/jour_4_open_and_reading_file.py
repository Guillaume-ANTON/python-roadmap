"""
import os
entries = os.listdir('/Users/guillaumeanton/Desktop/6semaines/python-roadmap/semaine_1')

for entry in entries:
    print(entry) """

"""
import os

with os.scandir('/Users/guillaumeanton/Desktop/6semaines/python-roadmap/semaine_1') as entries:
    for entry in entries:
        print(entry.name) """

"""
import os

basepath = '/Users/guillaumeanton/Desktop/6semaines/python-roadmap/semaine_1'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name) """

import os
file = '/Users/guillaumeanton/Desktop/6semaines/python-roadmap/semaine_1/jour_4_open_and_reading_file/'
directory = '/Users/guillaumeanton/Desktop/6semaines/python-roadmap/semaine_1/jour_4_open_and_reading_file/file.csv'

with open(directory,'r') as f:
    data = f.read()
    with os.scandir(file) as entries:
        for entry in entries:
            if entry.is_file() and entry.name.endswith('.csv'):
                print(f"Le fichier est le suivant : {entry.name}")
    print(f"Le fichier est présent ici : {file}")
    print(data)