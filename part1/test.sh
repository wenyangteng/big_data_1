#!/bin/sh
../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /part1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /part1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /part1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../access.log /part1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../part1/Mapper.py -mapper ../part1/Mapper.py \
-file ../part1/Reducer.py -reducer ../part1/Reducer.py \
-input /part1/input/* -output /part1/output/
/usr/local/hadoop/bin/hdfs dfs -cat /part1/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /part1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /part1/output/
../stop.sh
