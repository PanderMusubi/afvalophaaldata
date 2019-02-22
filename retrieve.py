#!/usr/bin/env python3

# name: retrive.py
# description: TODO
# license: MIT
# date: 2016-03-24

from datetime import datetime, timedelta
from os import getpid, mkdir, path, rename
from random import uniform, shuffle
from socket import getfqdn
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

# date and time
utcnow = datetime.utcnow()
yearnow = utcnow.strftime('%Y')
dtstamp = utcnow.strftime('%Y%m%dT%H%M%SZ')
now = time()

# event UID
uid_format='UID:%(date)s-%(pid)d-%(seq)04d-%(lang)s@%(domain)s\n'
uid_replace_values = {
    'date': dtstamp,
    'pid':  getpid(),
    'domain': getfqdn()
}
event_seq = 1

# create ICS header
collection_header = ''
event_header = open('templates/event-header.txt')
for line in event_header:
    collection_header += line.replace('DTSTAMP:', 'DTSTAMP:{}'.format(dtstamp))

# create ICS footer
collection_footer = ''
event_footer = open('templates/event-footer.txt')
for line in event_footer:
    collection_footer += line

# create ICS directory
if not path.exists('ics'):
    mkdir('ics')

addresses = []
for address in open('addresses.tsv'):
    address = address[:-1].replace('\t', '/')
    if address != '' and address[0] != '#':
        basename = address.replace('/', '-')
        decimals = basename[:4]
        letters = basename[4:6]
        number = basename[7:]
        if path.isfile('ics/{}/{}/{}.ics'.format(decimals, letters, number)):
            tstamp = path.getmtime('ics/{}/{}/{}.ics'.format(decimals, letters, number))
            if tstamp > now - 4 * 86400:  # not older than four days
#                print('INFO: Cache not yet expired')
                continue
        addresses.append(address)

shuffle(addresses)
count = 0
for address in addresses:
    sleep(uniform(3, 6))
    count += 1
    print('{}/{} {}'.format(count, len(addresses), address))
    basename = address.replace('/', '-')
    decimals = basename[:4]
    letters = basename[4:6]
    number = basename[7:]
    if not path.exists('ics/{}'.format(decimals)):
        mkdir('ics/{}'.format(decimals))
    if not path.exists('ics/{}/{}'.format(decimals, letters)):
        mkdir('ics/{}/{}'.format(decimals, letters))

    url = 'http://www.mijnafvalwijzer.nl/nl/{}/'.format(address)
    try:
        data = request.urlopen(url).read().decode('utf-8')
    except:
        print('WARNING: Could not retrieve url {}'.format(url))
        continue

    data = data.split('\n')
#    for reminder in ('T10H30M', 'T9H15M', 'T30M', 'T1H', ''):
    for reminder in ('', 'T10H30M', 'T1H'):
        alarm = ''  # no alarm
        if reminder == 'T10H30M':  # maximum, i.e. 21:30 previous day
            alarm = '_2130'
        elif reminder == 'T9H15M':  # nine hours and a quarter before
            alarm = '_2215'
        elif reminder == 'T1H':  # one hour before 08:00
            alarm = '_0700'
        elif reminder == 'T30M':  # half hour before 08:00
            alarm = '_0730'
        temp = 'ics/{}/{}/{}{}.tmp.ics'.format(decimals, letters, number, alarm)
        calendar = open(temp, 'w', newline='\r\n')

        calendar_header = open('templates/calendar-header.txt')
        for line in calendar_header:
            calendar.write(line)

        index = 0
        while index < len(data):
            line = data[index]
            index += 1
            if '<a href="#waste-' in line:
                name = line.split('title="')[1]
                name = name.split('"')[0].replace(',', '\,')
                index += 1
                line = data[index]
                index += 1
                datum = line.replace('<br />', '').strip()
                datum = datum.split(' ')
                day_name = None
                day = None
                month = None
                year = yearnow
                if len(datum) == 4:
                    (day_name, day, month, year) = datum
                else:
                    (day_name, day, month) = datum
                month = month_to_number(month)
   
                calendar.write('{}{}\n'.format(
                    collection_header.strip(), name))

                # write UID and autoincrement
                calendar.write(uid_format % (dict(list(uid_replace_values.items()) + list({ 'lang': 'en', 'seq': event_seq }.items()))))
                event_seq += 1

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

        calendar_footer = open('templates/calendar-footer.txt')
        for line in calendar_footer:
            calendar.write(line)
        rename(temp, '{}'.format(temp.replace('.tmp.ics', '.ics')))

