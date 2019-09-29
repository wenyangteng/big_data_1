#!/bin/sh
cat workers | while read line
do
    if [ "$line" = "-" ]; then
        echo "Skip $line"
    else
        ssh root@$line -n "rm -rf /Big_Data/ && mkdir /Big_Data/"
        echo "Copy data to $line"
        scp  /Big_Data/setup.py root@$line:/Big_Data/ && scp /Big_Data/manager root@$line:/Big_Data/ && scp /Big_Data/workers root@$line:/Big_Data/
        echo "Setup $line"
        ssh root@$line -n "cd /Big_Data/ && python3 setup.py && ntpdate time.nist.gov"
        echo "Finished config node $line"
    fi
done
