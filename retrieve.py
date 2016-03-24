#!/usr/bin/env python3

# name: retrive.py
# description: TODO
# license: MIT
# date: 2016-03-24

from datetime import datetime
from sys import argv
from time import sleep
from urllib import request


def monthToNumber(month):
    if month == 'januari':
        return '01'
    elif month == 'februari':
        return '02'
    elif month == 'maart':
        return '03'
    elif month == 'april':
        return '04'
    elif month == 'mei':
        return '05'
    elif month == 'juni':
        return '06'
    elif month == 'juli':
        return '07'
    elif month == 'augustus':
        return '08'
    elif month == 'september':
        return '09'
    elif month == 'oktober':
        return '10'
    elif month == 'november':
        return '11'
    elif month == 'december':
        return '12'
    else:
        return ''

now = datetime.now()
stamp = now.strftime('%Y%m%d%H%M')
year_number = now.strftime('%Y')
print('{}'.format(stamp))
for address in open('addresses.tsv', 'r'):
    address = address[:-1].replace('\t', '/')
    if address != '':
        sleep(1)
        print(address)
        url = 'http://www.mijnafvalwijzer.nl/nl/{}/'.format(address)

        try:
            data = request.urlopen(url).read().decode('utf-8')
        except:
            print('ERROR')

        data = data.split('\n')
        calendar = open('{}.ics'.format(address.replace('/', '-')), 'w')
        calendar.write('{}\n'.format(stamp))
		
        for line in data:
            if '<a href="#waste-' in line:
                collection = line.split('title="')[1]
                second = collection.split('"><p class="')
                collection = second[0]
                second = second[1].replace('<br />', '')
                second = second.replace('gft">', '')
                second = second.replace('kerstbomen">', '')
                second = second.replace('papier">', '')
                second = second.replace('pmd">', '')
                (day, day_number, month) = second.split(' ')
                month_number = monthToNumber(month)
                calendar.write('{}\n'.format(collection))
                calendar.write('{}{}{}\n'.format(year_number, month_number, day_number))
