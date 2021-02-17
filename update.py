#!/usr/bin/env python3
"""
Generate calendars with garbage collection times in iCal format.

# name: retrive.py
# license: MIT

# List all unique values of SUMMARY with following command
# grep -rh SUMMARY ics|sort|uniq
"""

from datetime import datetime
from os import getpid, listdir, makedirs, path, rename, sep
from random import uniform, shuffle
from socket import getfqdn
from time import sleep, time
from urllib import request
import sys


def month_to_number(month):
    """
    Blah blah.

    Parameters
    ----------
    month : TYPE
        DESCRIPTION.

    Returns
    -------
    number : TYPE
        DESCRIPTION.

    """
    number = ''
    if month.lower() == 'januari':
        number = '01'
    if month.lower() == 'februari':
        number = '02'
    if month.lower() == 'maart':
        number = '03'
    if month.lower() == 'april':
        number = '04'
    if month.lower() == 'mei':
        number = '05'
    if month.lower() == 'juni':
        number = '06'
    if month.lower() == 'juli':
        number = '07'
    if month.lower() == 'augustus':
        number = '08'
    if month.lower() == 'september':
        number = '09'
    if month.lower() == 'oktober':
        number = '10'
    if month.lower() == 'november':
        number = '11'
    if month.lower() == 'december':
        number = '12'
    return number


def address_to_path(address):
    """
    Blah blah.

    Parameters
    ----------
    month : TYPE
        DESCRIPTION.

    Returns
    -------
    number : TYPE
        DESCRIPTION.

    """
    basename = address.replace('/', '-')
    decimals = basename[:4]
    letters = basename[4:6]
    number = basename[7:]
    return f'ics{sep}{decimals}{sep}{letters}{sep}{number}.ics'


def address_to_dir(address):
    """
    Blah blah.

    Parameters
    ----------
    month : TYPE
        DESCRIPTION.

    Returns
    -------
    number : TYPE
        DESCRIPTION.

    """
    basename = address.replace('/', '-')
    decimals = basename[:4]
    letters = basename[4:6]
    return f'ics{sep}{decimals}{sep}{letters}'


def address_to_file(address):
    """
    Blah blah.

    Parameters
    ----------
    month : TYPE
        DESCRIPTION.

    Returns
    -------
    number : TYPE
        DESCRIPTION.

    """
    basename = address.replace('/', '-')
    number = basename[7:]
    return f'{number}.ics'


def reminder_to_alarm(reminder):
    """
    Blah blah.

    Parameters
    ----------
    month : TYPE
        DESCRIPTION.

    Returns
    -------
    number : TYPE
        DESCRIPTION.

    """
    alarm = ''  # no alarm
    if reminder == 'T10H30M':  # maximum, i.e. 21:30 previous day
        alarm = '_2130'
    elif reminder == 'T9H15M':  # nine hours and a quarter before
        alarm = '_2215'
    elif reminder == 'T1H':  # one hour before 08:00
        alarm = '_0700'
    elif reminder == 'T30M':  # half hour before 08:00
        alarm = '_0730'
    return alarm


def improve_name(name):
    """
    Blah blah.

    Parameters
    ----------
    month : TYPE
        DESCRIPTION.

    Returns
    -------
    number : TYPE
        DESCRIPTION.

    """
    if name == 'Groente, fruit- en tuinafval':
        name = 'Groente, Fruit- en Tuinafval (GFT)'
    elif name == 'Papier en karton':
        name = 'Papier en Karton'
    elif name == 'PMD':
        name = 'Plastic, Metalen en Drankkartons (PMD)'
    return name.replace(',', '\\,').replace(' & ', ' en ')


def write_mad(data, event_seq, names):
    """
    Blah blah.

    Parameters
    ----------
    month : TYPE
        DESCRIPTION.

    Returns
    -------
    number : TYPE
        DESCRIPTION.

    """
    for reminder in reminders:
        alarm = reminder_to_alarm(reminder)
        temp = f'ics{sep}{decimals}{sep}{letters}{sep}{number}{alarm}.tmp.ics'
        calendar = open(temp, 'w', newline='\r\n')

        calendar_header = open(f'templates{sep}calendar-header.txt')
        for line in calendar_header:
            calendar.write(line)

        # scraping like it's 1999
        index = 0
        while index < len(data):
            line = data[index]
            index += 1
            if '<a href="#waste-' in line:
                line = data[index]
                index += 1
                name = line.split('title="')[1]
                name = name.split('"')[0]
                name = improve_name(name)
                names.add(name)
                line = data[index]
                index += 1
                line = data[index]
                index += 1
                line = data[index]
                index += 1
                datum = line.split('<span class="span-line-break">')[1]
                datum = datum.split('</span>')[0].split(' ')
                day_name = None
                day = None
                month = None
                year = yearnow
                if len(datum) == 4:
                    (day_name, day, month, year) = datum
                else:
                    (day_name, day, month) = datum
                month = month_to_number(month)

                calendar.write(f'{collection_header.strip()}{name}\n')

                # write UID and autoincrement
                calendar.write(uid_format % (dict(
                    list(uid_replace_values.items()) +
                    list({'lang': 'en', 'seq': event_seq}.items()))))
                event_seq += 1

                date = datetime.strptime(f'{year}{month}{day}', '%Y%m%d')
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
                    calendar.write(f'TRIGGER;VALUE=DURATION:-P{reminder}\n')
                    calendar.write(f'DESCRIPTION:{name} aan de straat'
                                   ' zetten\n')
                    calendar.write('END:VALARM\n')

                calendar.write(collection_footer)

        calendar_footer = open(f'templates{sep}calendar-footer.txt')
        for line in calendar_footer:
            calendar.write(line)
        rename(temp, temp.replace('.tmp.ics', '.ics'))
    return event_seq


def write_rmn(data, event_seq, names):
    """
    Blah blah.

    Parameters
    ----------
    month : TYPE
        DESCRIPTION.

    Returns
    -------
    number : TYPE
        DESCRIPTION.

    """
    for reminder in reminders:
        alarm = reminder_to_alarm(reminder)
        temp = f'ics{sep}{decimals}{sep}{letters}{sep}{number}{alarm}.tmp.ics'
        calendar = open(temp, 'w', newline='\r\n')

        calendar_header = open(f'templates{sep}calendar-header.txt')
        for line in calendar_header:
            calendar.write(line)

        # scraping like it's 1999
        index = 0
        day = None
        month = None
        year = None
        start_month = False
        while index < len(data):
            line = data[index]
            index += 1
            if '<caption class="std-accent"' in line:
                line = data[index]
                index += 1
                month = line.split('<span>')[1].split(' ')[0]
                month = month_to_number(month)
                year = line.split('<span>')[1].split(' ')[1].split('<')[0]
                start_month = False
            if 'class="datum">' in line:
                day = line.split('class="datum">')[1].split('<')[0]
                if 'class="datum">1<' in line:
                    start_month = True
                line = data[index]
                index += 1
                if start_month:
                    while 'class="' not in line:
                        line = data[index]
                        index += 1
                    if 'class="iconafvalstroom"' not in line:
                        continue
                    while 'alt="' not in line:
                        line = data[index]
                        index += 1
                    name = line.split('alt="')[1].split('"')[0]
                    name = improve_name(name)
                    calendar.write(f'{collection_header.strip()}{name}\n')

                    # write UID and autoincrement
                    calendar.write(uid_format % (dict(list(uid_replace_values.items()) + list({'lang': 'en', 'seq': event_seq}.items()))))
                    event_seq += 1

                    date = datetime.strptime(
                        '{}{}{}'.format(year, month, day), '%Y%m%d')
                    calendar.write('DTSTART;VALUE=DATE-TIME:{}T080000\n'.format(
                        date.strftime('%Y%m%d')))
                    calendar.write('DTEND;VALUE=DATE-TIME:{}T080000\n'.format(
                        date.strftime('%Y%m%d')))
# for whole day event, remove the T080000 and add endtime one day later
#                    date += timedelta(days=1)
#                    calendar.write('DTEND;VALUE=DATE:{}\n'.format(
#                        date.strftime('%Y%m%d')))
                    if reminder != '':
                        calendar.write('BEGIN:VALARM\n')
                        calendar.write('ACTION:DISPLAY\n')
                        calendar.write('TRIGGER;VALUE=DURATION:'
                                       f'-P{reminder}\n')
                        calendar.write('DESCRIPTION:'
                                       f'{name} aan de straat zetten\n')
                        calendar.write('END:VALARM\n')

                    calendar.write(collection_footer)

        calendar_footer = open('templates{}calendar-footer.txt'.format(sep))
        for line in calendar_footer:
            calendar.write(line)
        rename(temp, '{}'.format(temp.replace('.tmp.ics', '.ics')))
    return event_seq


def write_rova(data, event_seq, names):
    """
    Blah blah.

    Parameters
    ----------
    month : TYPE
        DESCRIPTION.

    Returns
    -------
    number : TYPE
        DESCRIPTION.

    """
    # scraping like it's 1999
    index = 0
    dates = None
    while index < len(data):
        line = data[index]
        index += 1
        if line == 'Geen adres gevonden':
            print('WARNING: Unsupported address, skipping')
            return event_seq
        if '"kalenderContainer"' in line:
            dates = line.split('afvalkalenderData:\'')[1].split('\'')[0]
            break
    if dates is None:
        return event_seq  #FIXME login via post with postcode required, also do logout! also set 'do not remember'

    for reminder in reminders:
        alarm = reminder_to_alarm(reminder)
        temp = f'ics{sep}{decimals}{sep}{letters}{sep}{number}{alarm}.tmp.ics'
        calendar = open(temp, 'w', newline='\r\n')

        calendar_header = open('templates{}calendar-header.txt'.format(sep))
        for line in calendar_header:
            calendar.write(line)

        print('TODO')
        for d in dates.split(','):
            print(d)
            sys.exit(0)  # TODO, see FIXME above

    return event_seq


# reminders at, before and after
# reminders = ('', 'T10H30M', 'T9H15M', 'T30M', 'T1H')
reminders = ('', 'T10H30M', 'T1H')

# date and time
utcnow = datetime.utcnow()
yearnow = utcnow.strftime('%Y')
dtstamp = utcnow.strftime('%Y%m%dT%H%M%SZ')
now = time()

# event UID
uid_format = 'UID:%(date)s-%(pid)d-%(seq)04d-%(lang)s@%(domain)s\n'
uid_replace_values = {
    'date': dtstamp,
    'pid': getpid(),
    'domain': getfqdn()
}
event_seq = 1

# create ICS header
collection_header = ''
event_header = open(f'templates{sep}event-header.txt')
for line in event_header:
    collection_header += line.replace('DTSTAMP:', 'DTSTAMP:{}'.format(dtstamp))

# create ICS footer
collection_footer = ''
event_footer = open(f'templates{sep}event-footer.txt')
for line in event_footer:
    collection_footer += line

addresses = []
groups = set()
group = set()
for address in open('addresses.tsv'):
    address = address[:-1].replace('\t', '/')
    if address != '' and address[0] != '#':
        adress_path = address_to_path(address)
        if path.isfile(adress_path):
            tstamp = path.getmtime(adress_path)
            if tstamp > now - 4 * 86400:  # not older than four days
                print('INFO: Cache not yet expired for {}'.format(address))
                continue
        addresses.append(address)
        group.add(address)
    elif address == '':
        if group:
            groups.add(tuple(group))
        group = set()

sources = {}
count = 0
names = set()
if addresses:
    print('Updating following {} addresses:'.format(len(addresses)))
    shuffle(addresses)
for address in addresses:
    sleep(uniform(3, 6))
    count += 1
    print('{}/{} {}'.format(count, len(addresses), address))
    basename = address.replace('/', '-')
    decimals = basename[:4]
    letters = basename[4:6]
    number = basename[7:]
    directory = address_to_dir(address)
    if not path.exists(directory):
        makedirs(directory, exist_ok=True)

    postcode = decimals + letters
    huisnummer = number.split('-')[0]
    toevoeging = ''
    if '-' in number:
        toevoeging = number.split('-')[1]

    source = None
    url = f'http://www.mijnafvalwijzer.nl/nl/{address}/'
    try:
        data = request.urlopen(url).read().decode('utf-8').split('\n')
        source = 'maw'
    except:
        url = 'https://inzamelschema.rmn.nl/adres/{}/jaarkalender'.format(
            address.replace('/', ':'))
        try:
            data = request.urlopen(url).read().decode('utf-8').split('\n')
            source = 'rmn'
        except Exception as e:
            url = 'http://afvalkalender.rova.nl/rest/login?' \
                f'postcode={postcode}&huisnummer={huisnummer}&' \
                f'toevoeging={toevoeging}'
            try:
                data = request.urlopen(url).read().decode('utf-8').split('\n')
                source = 'rova'
            except Exception as e:
                url = 'https://www.afvalstoffendienst.nl/login' #TODO
                try:
                    data = request.urlopen(url).read().decode('utf-8').split(
                        '\n')
                    source = 'asd'
                except Exception as e:
                    print(f'WARNING: Could not retrieve url {url} because {e}')
                    continue
    if source == 'maw':
        event_seq = write_mad(data, event_seq, names)
    elif source == 'rmn':
        event_seq = write_rmn(data, event_seq, names)
    elif source == 'rova':
        event_seq = write_rova(data, event_seq, names)
    else:
        print(f'ERROR: Unknown source {source}, skipping')
        continue

if names:
    print('\nFound following types:')
    names_used = open('names-used-dutch.txt', 'w')
    for name in sorted(names):
        print('{}'.format(name.replace('\\', '')))
        names_used.write('{}\n'.format(name.replace('\\', '')))

for decimals in sorted(listdir('ics')):
    for letters in sorted(listdir(f'ics{sep}{decimals}')):
        readme = open(f'ics{sep}{decimals}{sep}{letters}{sep}README.md', 'w')
        readme.write(f'# URL\'s postcode {decimals} {letters}\n\n')
        for number in sorted(listdir(f'ics{sep}{decimals}{sep}{letters}')):
            if number == 'README.md':
                continue
            number = number.replace('.ics', '')
            if '_' in number:
                alarm = number.split('_')[1]
                readme.write('## Huisnummer {} met alarm om {}.{} uur\n\n'.format(number.split('_')[0], alarm[:2], alarm[2:]))
            else:
                readme.write(f'## Huisnummer {number} zonder alarm\n\n')
            readme.write('https://raw.github.com/PanderMusubi/afvalophaaldata/'
                         f'master/ics/{decimals}/{letters}/{number}.ics\n\n')
#            readme.write('![QR-code https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/{}/{}/{}.ics](https://api.qrserver.com/v1/create-qr-code/?data=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F{}%2F{}%2F{}.ics)\n\n'.format(decimals, letters, number, decimals, letters, number))
