#!/bin/sh
cat workers | while read line
do
    if [ "$line" = "-" ]; then
        echo "Skip $line"
    else
        ssh root@$line -n "rm -rf /big_data_1/ && mkdir /big_data_1/"
        echo "Copy data to $line"
        scp  /big_data_1/setup.py root@$line:/big_data_1/ && scp /big_data_1/manager root@$line:/big_data_1/ && scp /big_data_1/workers root@$line:/big_data_1/
        echo "Setup $line"
        ssh root@$line -n "cd /big_data_1/ && python3 setup.py && ntpdate time.nist.gov"
        echo "Finished config node $line"
    fi
done
