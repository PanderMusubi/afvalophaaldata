./retrieve.py
find ics -name '*.tmp.ics' -exec rm -f {} \;
flip -m ics/*/*/*.ics
grep -h SUMMARY ics/*/*/*.ics|sed -e 's/SUMMARY://'|sort|uniq>names-used-dutch.txt
cat names-used-dutch.txt

# Generate QR codes
cd ics
for i in ????
do
    cd $i
    for j in ??
    do
        cd $j
        rm -f README.md
        echo -e "# QR-codes postcode $i $j #\n" >> README.md
        for k in *.ics
        do
            if [ `echo $k|grep '_'|wc -l` == '0' ]
            then
                echo -e "## Huisnummer `echo $k|sed -e 's/\.ics//'` zonder alarm ##\n" >> README.md
            else
                echo -e "## Huisnummer `echo $k|sed -e 's/_.*//'|sed -e 's/\.ics//'` met alarm om `echo $k|sed -e 's/.*_//'|sed -e 's/\.ics//'` ##\n" >> README.md
            fi
            echo -e "https://raw.githubusercontent.com/PanderMusubi/afvalophaaldata/master/ics/$i/$j/$k\n" >> README.md
            echo -e "![QR-code https://raw.githubusercontent.com/PanderMusubi/afvalophaaldata/master/ics/$i/$j/$k](https://api.qrserver.com/v1/create-qr-code/?data=https%3A%2F%2Fraw.githubusercontent.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F$i%2F$j%2F$k)\n" >> README.md
        done
        cd ..
    done
    cd ..
done
cd ..
