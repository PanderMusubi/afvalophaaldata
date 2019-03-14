#!/usr/bin/env python3

# name: retrive.py
# description: Generate calendars with garbage collection times in iCal format.
# license: MIT
# date: 2016-03-24

from datetime import datetime, timedelta
from os import getpid, listdir, makedirs, path, rename, remove, sep
#from os import chdir, symlink
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

def address_to_path(address):
    basename = address.replace('/', '-')
    decimals = basename[:4]
    letters = basename[4:6]
    number = basename[7:]
    return 'ics{}{}{}{}{}{}.ics'.format(sep, decimals, sep, letters, sep, number)

def address_to_path(address):
    basename = address.replace('/', '-')
    decimals = basename[:4]
    letters = basename[4:6]
    number = basename[7:]
    return 'ics{}{}{}{}{}{}.ics'.format(sep, decimals, sep, letters, sep, number)

def address_to_dir(address):
    basename = address.replace('/', '-')
    decimals = basename[:4]
    letters = basename[4:6]
    return 'ics{}{}{}{}'.format(sep, decimals, sep, letters)

def address_to_file(address):
    basename = address.replace('/', '-')
    number = basename[7:]
    return '{}.ics'.format(number)

def reminder_to_alarm(reminder):
    if reminder == 'T10H30M':  # maximum, i.e. 21:30 previous day
        return '_2130'
    elif reminder == 'T9H15M':  # nine hours and a quarter before
        return '_2215'
    elif reminder == 'T1H':  # one hour before 08:00
        return '_0700'
    elif reminder == 'T30M':  # half hour before 08:00
        return '_0730'
    return ''  # no alarm


# reminders at, before and after
#reminders = ('', 'T10H30M', 'T9H15M', 'T30M', 'T1H')
reminders =  ('', 'T10H30M', 'T1H')

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
event_header = open('templates{}event-header.txt'.format(sep))
for line in event_header:
    collection_header += line.replace('DTSTAMP:', 'DTSTAMP:{}'.format(dtstamp))

# create ICS footer
collection_footer = ''
event_footer = open('templates{}event-footer.txt'.format(sep))
for line in event_footer:
    collection_footer += line

addresses = {}
main = None
for address in open('addresses.tsv'):
    address = address[:-1].replace('\t', '/')
    if address != '' and address[0] != '#':
        main_path = address_to_path(address)
        if main == None:
            main = address
            if path.isfile(main_path):
                tstamp = path.getmtime(main_path)
                if tstamp > now - 4 * 86400:  # not older than four days
                    print('INFO: Cache not yet expired for {}'.format(address))
                    main = None #FIXME see below regarding GitHub
                    continue
            addresses[main] = []
            main = None #FIXME
        else:
            if main in addresses:
                addresses[main].append(address)
    elif address == '':
        main = None

shuffled = list(set(addresses))
shuffle(shuffled)
count = 0
names = set()
if shuffled:
    print('Updating following addresses:')
for address in shuffled:
    sleep(uniform(3, 6))
    count += 1
    print('  {}/{} {}'.format(count, len(shuffled), address))
    basename = address.replace('/', '-')
    decimals = basename[:4]
    letters = basename[4:6]
    number = basename[7:]
    dir = address_to_dir(address)
    if not path.exists(dir):
        makedirs(dir, exist_ok=True)

    url = 'http://www.mijnafvalwijzer.nl/nl/{}/'.format(address)
    try:
        data = request.urlopen(url).read().decode('utf-8')
    except:
        print('WARNING: Could not retrieve url {}'.format(url))
        continue

    data = data.split('\n')
    for reminder in reminders:
        alarm = reminder_to_alarm(reminder)
        temp = 'ics{}{}{}{}{}{}{}.tmp.ics'.format(sep, decimals, sep, letters, sep, number, alarm)
        calendar = open(temp, 'w', newline='\r\n')

        calendar_header = open('templates{}calendar-header.txt'.format(sep))
        for line in calendar_header:
            calendar.write(line)

        index = 0
        while index < len(data):
            line = data[index]
            index += 1
            if '<a href="#waste-' in line:
                name = line.split('title="')[1]
                name = name.split('"')[0].replace(',', '\,')
                names.add(name)
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
# for whole day event, remove the T080000 and add endtime one day later
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

        calendar_footer = open('templates{}calendar-footer.txt'.format(sep))
        for line in calendar_footer:
            calendar.write(line)
        rename(temp, '{}'.format(temp.replace('.tmp.ics', '.ics')))

# doesn't work on GitHub, see https://stackoverflow.com/questions/954560/how-does-git-handle-symbolic-links
# for main, links in sorted(addresses.items()):
#     main_file = address_to_file(main)
#     chdir(address_to_dir(main))
#     for link in links:
#         for reminder in reminders:
#             link_file = address_to_file(link)
#             alarm = reminder_to_alarm(reminder)
#             src = link_file.replace('.ics', '{}.ics'.format(alarm))
#             dst = main_file.replace('.ics', '{}.ics'.format(alarm))
#             if path.exists(src):
#                 remove(src)
#             symlink(dst, src)
#     chdir('..{}..{}..'.format(sep, sep))

if names:
    print('Found following summaries:')
    names_used = open('names-used-dutch.txt', 'w')
    for name in sorted(names):
        print('  {}'.format(name.replace('\\', '')))
        names_used.write('{}\n'.format(name.replace('\\', '')))

for decimals in sorted(listdir('ics')):
    for letters in sorted(listdir('ics{}{}'.format(sep, decimals))):
        readme = open('ics{}{}{}{}{}README.md'.format(sep, decimals, sep, letters, sep), 'w')
        readme.write('# QR-codes postcode {} {}\n\n'.format(decimals, letters))
        for number in sorted(listdir('ics{}{}{}{}'.format(sep, decimals, sep, letters))):
            if number == 'README.md':
                continue
            number = number.replace('.ics', '')
            if '_' in number:
                alarm = number.split('_')[1]
                readme.write('## Huisnummer {} met alarm om {}.{} uur\n\n'.format(number, alarm[:2], alarm[2:]))
            else:
                readme.write('## Huisnummer {} zonder alarm\n\n'.format(number))
            readme.write('https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/{}/{}/{}.ics\n\n'.format(decimals, letters, number))
            readme.write('![QR-code https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/{}/{}/{}.ics](https://api.qrserver.com/v1/create-qr-code/?data=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F{}%2F{}%2F{}.ics)\n\n'.format(decimals, letters, number, decimals, letters, number))
