if [ -e ics-copy ]
then
    rm -rf ics-copy
fi
cp -r ics ics-copy
cd ics-copy
for i in *
do
    echo $i
    cd $i
    for j in *
    do
        echo '  '$j
        cd $j
        for k in  *.ics
        do
#            echo $k
            sed -i 's/^UID:.*//g' $k
        done
        cd ..
    done
    cd ..
done
pwd
fdupes -r *
cd ..
