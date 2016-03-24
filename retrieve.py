#!/usr/bin/env python3

# name: retrive.py
# description: TODO
# license: MIT
# date: 2016-03-24

from datetime import datetime, timedelta
from random import uniform
from time import sleep
from urllib import request


def month_to_number(month):
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

utcnow = datetime.utcnow()
year = utcnow.strftime('%Y')
dtstamp = utcnow.strftime('%Y%m%dT%H%M%SZ')

collection_header = ''
event_header = open('templates/event-header.txt', 'r')
for line in event_header.readlines():
    collection_header += line.replace('DTSTAMP:', 'DTSTAMP:{}'.format(dtstamp))

collection_footer = ''
event_footer = open('templates/event-footer.txt', 'r')
for line in event_footer.readlines():
    collection_footer += line

for address in open('addresses.tsv', 'r'):
    address = address[:-1].replace('\t', '/')
    if address != '':
        sleep(uniform(1, 3))
        print(address)
        url = 'http://www.mijnafvalwijzer.nl/nl/{}/'.format(address)

        try:
            data = request.urlopen(url).read().decode('utf-8')
        except:
            print('ERROR')

        data = data.split('\n')
        calendar = open('calendars/{}.ics'.format(address.replace('/', '-')), 'w')

        calendar_header = open('templates/calendar-header.txt', 'r')
        for line in calendar_header.readlines():
            calendar.write(line)

        for line in data:
            if '<a href="#waste-' in line:
                name = line.split('title="')[1]
                second = name.split('"><p class="')
                name = second[0].replace(',', '\,')
                second = second[1].replace('<br />', '')
                second = second.split('">')[1]
                (day_name, day, month) = second.split(' ')
                month = month_to_number(month)

                calendar.write('{}{}\n'.format(
                    collection_header.strip(), name))
                date = datetime.strptime(
                    '{}{}{}'.format(year, month, day), '%Y%m%d')
                calendar.write('DTSTART;VALUE=DATE:{}\n'.format(
                    date.strftime('%Y%m%d')))
                date += timedelta(days=1)
                calendar.write('DTEND;VALUE=DATE:{}\n'.format(
                    date.strftime('%Y%m%d')))
                calendar.write(collection_footer)

        calendar_footer = open('templates/calendar-footer.txt', 'r')
        for line in calendar_footer.readlines():
            calendar.write(line)
