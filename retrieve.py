#!/usr/bin/env python3

# name: retrive.py
# description: TODO
# license: MIT
# date: 2016-03-24

from datetime import datetime, timedelta
from os import mkdir, path, rename
from random import uniform, shuffle
from time import sleep, time
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
now = time()

collection_header = ''
event_header = open('templates/event-header.txt', 'r')
for line in event_header:
    collection_header += line.replace('DTSTAMP:', 'DTSTAMP:{}'.format(dtstamp))

collection_footer = ''
event_footer = open('templates/event-footer.txt', 'r')
for line in event_footer:
    collection_footer += line

if not path.exists('ics'):
    mkdir('ics')

addresses = []
for address in open('addresses.tsv', 'r'):
    address = address[:-1].replace('\t', '/')
    if address != '' and address[0] != '#':
        basename = address.replace('/', '-')
        print(basename)
        letters = basename[:4]
        decimals = basename[4:6]
        number = basename[7:]
        print(letters)
        print(decimals)
        print(number)
        if not path.exists('ics/{}'.format(letters)):
            mkdir('ics/{}'.format(letters))
        if not path.exists('ics/{}/{}'.format(letters, decimals)):
            mkdir('ics/{}/{}'.format(letters, decimals))
        exit(0)
        if path.isfile('ics/{}.ics'.format(basename)):
            tstamp = path.getmtime('ics/{}.ics'.format(basename))
            if tstamp > now - 4 * 86400:  # not older than four days
#                print('INFO: Cache not yet expired')
                continue
        addresses.append(address)

shuffle(addresses)
count = 0
for address in addresses:
    count += 1
    print('{}/{} {}'.format(count, len(addresses), address))
    basename = address.replace('/', '-')

    url = 'http://www.mijnafvalwijzer.nl/nl/{}/'.format(address)
    try:
        data = request.urlopen(url).read().decode('utf-8')
    except:
        print('WARNING: Could not retrieve url {}'.format(url))
        continue

    data = data.split('\n')
    for reminder in ('', 'T30M', 'T1H', 'T9H15M', 'T10H30M'):
        alarm = ''  # no alarm
        if reminder == 'T30M':  # half hour before 08:00
            alarm = '_0730'
        elif reminder == 'T1H':  # one hour before 08:00
            alarm = '_0700'
        elif reminder == 'T9H15M':  # nine hours and a quarter before
            alarm = '_2215'
        elif reminder == 'T10H30M':  # maximum, i.e. 21:30 previous day
            alarm = '_2130'
        temp = '{}{}.tmp.ics'.format(basename, alarm)
        calendar = open(temp, 'w')

        calendar_header = open('templates/calendar-header.txt', 'r')
        for line in calendar_header:
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
                calendar.write('DTSTART;VALUE=DATE-TIME:{}T080000\n'.format(
                    date.strftime('%Y%m%d')))
                calendar.write('DTEND;VALUE=DATE-TIME:{}T080000\n'.format(
                    date.strftime('%Y%m%d')))
# for whole day event, remove the T080000 and add endtime one dat later
#                date += timedelta(days=1)
#                calendar.write('DTEND;VALUE=DATE:{}\n'.format(
#                    date.strftime('%Y%m%d')))
                if reminder != '':
                    calendar.write('BEGIN:VALARM\n')
                    calendar.write('ACTION:DISPLAY\n')
                    calendar.write('TRIGGER;VALUE=DURATION:-P{}\n'.format(reminder))
                    calendar.write('DESCRIPTION:{} aan de straat zetten\n'.format(name))
                    calendar.write('END:VALARM\n')

                calendar.write(collection_footer)

        calendar_footer = open('templates/calendar-footer.txt', 'r')
        for line in calendar_footer:
            calendar.write(line)
        rename(temp, 'ics/{}'.format(temp.replace('.tmp', '')))

    sleep(uniform(5, 10))
