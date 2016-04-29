./retrieve.py
find ics -name '*.tmp.ics' -exec rm -f {} \;
flip -m ics/*/*/*.ics
grep -h SUMMARY ics/*/*/*.ics|sed -e 's/SUMMARY://'|sort|uniq>names-used-dutch.txt
cat names-used-dutch.txt
