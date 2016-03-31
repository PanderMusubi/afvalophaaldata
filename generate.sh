./retrieve.py
flip -m calendars/*.ics
grep -h SUMMARY calendars/*.ics|sed -e 's/SUMMARY://'|sort|uniq>names-used-dutch.txt
