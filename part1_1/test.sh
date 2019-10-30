#!/bin/sh
bash /mapreduce-test/start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /prj_1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /prj_1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /prj_1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal /project_1/big_data_1/test.log  /prj_1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file /project_1/big_data_1/part1_1/mapper.py -mapper /project_1/big_data_1/part1_1/mapper.py \
-file /project_1/big_data_1/part1_1/reducer.py -reducer /project_1/big_data_1/part1_1/reducer.py \
-input /prj_1/input/* -output /prj_1/output/
/usr/local/hadoop/bin/hdfs dfs -cat /prj_1/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /prj_1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /prj_1/output/
bash /mapreduce-test/stop.sh
