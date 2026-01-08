"""Generates calendars with garbage collection times in iCal format."""

# List all unique values of SUMMARY with following command
# grep -rh SUMMARY ics|sort|uniq

from datetime import datetime, timedelta,  UTC
from hashlib import sha256
from os import listdir, makedirs, path, rename, sep
from random import uniform, shuffle
from time import sleep, time
from urllib.request import Request, urlopen
import sys

# pylint:disable=consider-using-with


def month_to_number(month: str) -> str:
    """Convert month to number."""
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


def address_to_path(address: str) -> str:
    """Convert address to path."""
    basename = address.replace('/', '-')
    decimals = basename[:4]
    letters = basename[4:6]
    number = basename[7:]
    return f'ics{sep}{decimals}{sep}{letters}{sep}{number}.ics'


def address_to_dir(address: str) -> str:
    """Convert address to directory."""
    basename = address.replace('/', '-')
    decimals = basename[:4]
    letters = basename[4:6]
    return f'ics{sep}{decimals}{sep}{letters}'


def address_to_file(address: str) -> str:
    """Convert address to file name."""
    basename = address.replace('/', '-')
    number = basename[7:]
    return f'{number}.ics'


def reminder_to_alarm(reminder):
    """Convert reminder to alarm."""
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
    """Improves name."""
    if name.lower() == 'groente-, fruit- en tuinafval' or name.lower() == 'groente, fruit- en tuinafval' or name.lower() == 'gft':
        name = '🥬 Groente, Fruit- en Tuinafval (GFT)'
#    elif name.lower() == 'papier en karton':
#        name = '📦 Papier en Karton'
    elif name.lower() == 'papier' or name.lower() == 'papier en karton':
#        name = '📰 Papier'
        name = '📦 Papier en Karton (PK)'
    elif name.lower() == 'restafval':
        name = '🗑️ Restafval'
#    elif name.lower() == 'restgft':
#        name = '🗑️ Restgft'
    elif name.lower() == 'dhm':
        name = '🔌 Droge Herbruikbare Materialen (DHM)'
    elif name.lower() == 'pmd':
        name = '🧃 Plastic, Metalen en Drankkartons (PMD)'
    elif name.lower() == 'kerstbomen':
        name = '🎄 Kerstbomen (K)'
    return name.replace(',', '\\,').replace(' & ', ' en ')


def write_mad(data, names):  # pylint:disable=too-many-locals
    """Write blah."""
    for reminder in reminders:
        alarm = reminder_to_alarm(reminder)
        temp = f'ics{sep}{decimals}{sep}{letters}{sep}{number}{alarm}.tmp.ics'
        calendar = open(temp, 'w', newline='\r\n')

        with open(f'templates{sep}calendar-header.txt') as f:
            for line in f:
                line = line.replace('AFVALOPHAALDATA//NL',
                                    f'AFVALOPHAALDATA {decimals}{letters.upper()} {number.upper()}{alarm.replace("_", " @")}//NL')
                line = line.replace('X-WR-CALNAME:Afvalophaaldata',
                                    f'X-WR-CALNAME:Afvalophaaldata {decimals}{letters.upper()} {number.upper()}{alarm.replace("_", " @")}')
                calendar.write(line)

        # scraping like it's 1999
        index = 0
        processed = set()
        while index < len(data):
            line = data[index]
            index += 1
            if '<a href="#waste-' in line:
                line = data[index]
                index += 3
                name = line.split('title="')[1]
                name = name.split('"')[0]
                name = improve_name(name)
                names.add(name)
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

                date = datetime.strptime(f'{year}{month}{day}', '%Y%m%d')
                llave = decimals + letters + number + name + date.strftime("%Y%m%d") + reminder
                if llave not in processed:
                    calendar.write('BEGIN:VEVENT\n')
                    tmp = date + timedelta(days=-2)
                    calendar.write(f'DTSTAMP:{tmp.strftime("%Y%m%d")}T040000Z\n')
                    calendar.write(f'SUMMARY:{name}\n')

                    # write UID
                    uid = sha256((year + month + day + name + reminder).encode()).hexdigest()[:16]
                    calendar.write(f'UID:{uid}@afvalophaaldata.pandermusubi\n')

                    calendar.write(f'DTSTART;TZID=Europe/Amsterdam:{date.strftime("%Y%m%d")}T080000\n')
                    calendar.write(f'DTEND;TZID=Europe/Amsterdam:{date.strftime("%Y%m%d")}T080000\n')
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

                    calendar.write('CATEGORIES:Afvalophaal\n')
                    calendar.write('TRANSP:TRANSPARENT\n')
                    calendar.write('END:VEVENT\n')
                    processed.add(llave)

        with open(f'templates{sep}calendar-footer.txt') as f:
            for line in f:
                calendar.write(line)
        rename(temp, temp.replace('.tmp.ics', '.ics'))


def write_rmn(data):
    """Write blah."""
    # FIXME not tested / not working
    for reminder in reminders:
        alarm = reminder_to_alarm(reminder)
        temp = f'ics{sep}{decimals}{sep}{letters}{sep}{number}{alarm}.tmp.ics'
        calendar = open(temp, 'w', newline='\r\n')

        with open(f'templates{sep}calendar-header.txt') as f:
            for line in f:
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
                date = datetime.strptime(f'{year}{month}{day}', '%Y%m%d')
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
                    calendar.write('BEGIN:VEVENT\n')
                    tmp = date + timedelta(days=-2)
                    calendar.write(f'DTSTAMP:{tmp.strftime("%Y%m%d")}T040000Z\n')
                    calendar.write(f'SUMMARY:{name}\n')

                    # write UID
                    uid = sha256((year + month + day + name + reminder).encode()).hexdigest()[:16]
                    calendar.write(f'UID:{uid}@afvalophaaldata.pandermusubi\n')

                    calendar.write(f'DTSTART;VALUE=DATE-TIME:{date.strftime("%Y%m%d")}T080000\n')
                    calendar.write(f'DTEND;VALUE=DATE-TIME:{date.strftime("%Y%m%d")}T080000\n')
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

                    calendar.write('CATEGORIES:Afvalophaal\n')
                    calendar.write('TRANSP:TRANSPARENT\n')
                    calendar.write('END:VEVENT\n')

        with open(f'templates{sep}calendar-footer.txt') as f:
            for line in f:
                calendar.write(line)
        rename(temp, temp.replace('.tmp.ics', '.ics'))


def write_rova(data):
    """Write blah."""
    # scraping like it's 1999
    index = 0
    dates = None
    while index < len(data):
        line = data[index]
        index += 1
        if line == 'Geen adres gevonden':
            print('WARNING: Unsupported address, skipping')
            return
        if '"kalenderContainer"' in line:
            dates = line.split('afvalkalenderData:\'')[1].split('\'')[0]
            break
    if dates is None:
        #FIXME login via post with postcode required
        #FIXME also do logout! also set 'do not remember'
        return

    for reminder in reminders:
        alarm = reminder_to_alarm(reminder)
        temp = f'ics{sep}{decimals}{sep}{letters}{sep}{number}{alarm}.tmp.ics'
        calendar = open(temp, 'w', newline='\r\n')

        with open(f'templates{sep}calendar-header.txt') as f:
            for line in f:
                calendar.write(line)

        for date in dates.split(','):
            print(f'ERROR: {date}')
            sys.exit(1)  # TODO, see FIXME above


# reminders at, before and after
# reminders = ('', 'T10H30M', 'T9H15M', 'T30M', 'T1H')
reminders = ('', 'T10H30M', 'T1H')

# date and time
utcnow = datetime.now(UTC)
yearnow = utcnow.strftime('%Y')
now = time()

addresses = []
groups = set()
group = set()
with open('addresses.tsv') as f:
    for address in f:
        address = address[:-1].replace('\t', '/')
        if address != '' and address[0] != '#':
            adress_path = address_to_path(address)
            if path.isfile(adress_path):
                tstamp = path.getmtime(adress_path)
                if tstamp > now - 4 * 86400:  # not older than four days
    #TODO from dateutil.relativedelta import relativedelta
    # difference_in_years = relativedelta(end_date, start_date).years
                    print(f'INFO: Cache not yet expired for {address}')
                    continue
            addresses.append(address)
            group.add(address)
        elif address == '':
            if group:
                groups.add(tuple(group))
            group = set()

# sources = {}
count = 0
names: set[str] = set()
if addresses:
    print(f'Updating following {len(addresses)} addresses:')
    shuffle(addresses)
for address in addresses:
    sleep(uniform(4, 7))
    count += 1
    print(f'{count}/{len(addresses)} {address}')
    basename = address.replace('/', '-')
    decimals = basename[:4]
    letters = basename[4:6]
    number = basename[7:]
    directory = address_to_dir(address)
    if not path.exists(directory):  # FIXME
        makedirs(directory, exist_ok=True)

    postcode = decimals + letters
    huisnummer = number.split('-')[0]
    toevoeging = ''
    if '-' in number:
        toevoeging = number.split('-')[1]

    source = None
    url = f'https://www.mijnafvalwijzer.nl/nl/{address}/'
    try:
#        print(f'Trying to {url}')
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        data = urlopen(req).read().decode('utf-8').split('\n')
        source = 'maw'
    except Exception as e:  # noqa:F841  # pylint:disable=broad-except
        url = f'https://inzamelschema.rmn.nl/adres/{address.replace("/", ":")}/jaarkalender'
        try:
#            print(f'{e}\nTrying to {url}')
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            data = urlopen(req).read().decode('utf-8').split('\n')
            source = 'rmn'
        except Exception as e:  # noqa:F841  # pylint:disable=broad-except
            url = 'http://afvalkalender.rova.nl/rest/login?' \
                f'postcode={postcode}&huisnummer={huisnummer}&' \
                f'toevoeging={toevoeging}'
            try:
#                print(f'{e}\nTrying to {url}')
                req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                data = urlopen(req).read().decode('utf-8').split('\n')
                source = 'rova'
            except Exception as e:  # noqa:F841  # pylint:disable=broad-except
                url = 'https://www.afvalstoffendienst.nl/login' #TODO analyse
                try:
#                    print(f'{e}\nTrying to {url}')
                    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                    data = urlopen(req).read().decode('utf-8').split('\n')
                    source = 'asd'
                except Exception as e:  # noqa:F841  # pylint:disable=broad-except
                    print(f'WARNING: Could not retrieve url {url} because {e}')
                    continue
    if source == 'maw':
        write_mad(data, names)
    # elif source == 'rmn':
    #     write_rmn(data)
    # elif source == 'rova':
    #     write_rova(data)
    else:
        print(f'ERROR: Unknown source {source}, skipping {url} for postcode {postcode} and huisnummer {huisnummer} {toevoeging}')
        continue

if names:
    print('\nFound following types:')
    with open('names-used-dutch.txt', 'w') as f:
        for name in sorted(names):
            print('{}'.format(name.replace('\\', '')))
            f.write('{}\n'.format(name.replace('\\', '')))

for decimals in sorted(listdir('ics')):
    for letters in sorted(listdir(f'ics{sep}{decimals}')):
        with open(f'ics{sep}{decimals}{sep}{letters}{sep}README.md', 'w') as f:
            f.write(f'# URL\'s postcode {decimals} {letters}\n\n')
            for number in sorted(listdir(f'ics{sep}{decimals}{sep}{letters}')):
                if number == 'README.md':
                    continue
                number = number.replace('.ics', '')
                if '_' in number:
                    alarm = number.split('_')[1]
                    f.write(f"## Huisnummer {number.split('_')[0]} met alarm"
                                 f"/notificatie om {alarm[:2]}.{alarm[2:]} uur\n\n")
                else:
                    f.write(f'## Huisnummer {number} zonder alarm\n\n')
                f.write('klik op [webcal://raw.github.com/PanderMusubi/afvalophaaldata/'
                             f'master/ics/{decimals}/{letters}/{number}.ics](webcal://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/{decimals}/{letters}/{number}.ics)\n\n')
                f.write('of kopieer en plak `https://raw.github.com/PanderMusubi/afvalophaaldata/'
                             f'master/ics/{decimals}/{letters}/{number}.ics`\n\n')
    # FIXME            f.write('![QR-code webcal://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/{}/{}/{}.ics](https://api.qrserver.com/v1/create-qr-code/?data=webcal%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F{}%2F{}%2F{}.ics)\n\n'.format(decimals, letters, number, decimals, letters, number))
