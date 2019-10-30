#!/bin/sh
bash start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /part1_1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /part1_1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /part1_1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../Parking_Violations_Issued_-_Fiscal_Year_2020.csv /part1_1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../../mapreduce-test-python/part1_1/mapper3.py -mapper ../part1_1/mapper3.py \
-file ../../mapreduce-test-python/part1_1/reducer3.py -reducer ../part1_1/reducer3.py \
-input /logstat/input/* -output /part1_1/output/
/usr/local/hadoop/bin/hdfs dfs -cat /part1_1/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /part1_1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /part1_1/output/
bash stop.sh
