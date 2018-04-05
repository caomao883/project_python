name="ouhuihao_test"
mapper=mapper1.py
reduce=reduce1.py
conf_file=../conf/Commonconf.py
prev_day=20180311
day=20180312
today=`date -d "now" +%Y%m%d`
file_input_path=/user/80213526/test/t1
file_output_path=/user/80213526/test/study_streaming/output
function train(){
    hadoop fs -rm -r ${file_output_path}
    /data/tools/hadoop_env/hadoop-2.6.5/bin/hadoop jar /data/huihao/strategy/bin/utils/hadoop-streaming-2.6.0.jar \
    -D mapred.job.name=ad_survey_get_log  \
    -D mapred.map.output.compression.codec=com.hadoop.compression.lzo.LzoCodec  \
    -D mapreduce.map.speculative=true  \
    -D mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec  \
    -D mapred.job.map.capacity=300  \
    -D stream.memory.limit=2000  \
    -D mapred.job.priority=NORMAL  \
    -D mapred.max.split.size=1073741824  \
    -D mapreduce.job.reduce.slowstart.completedmaps=1.0  \
    -D stream.num.map.output.key.fields=1  \
    -D mapreduce.reduce.speculative=true  \
    -D mapreduce.reduce.memory.mb=6192  \
    -D mapred.compress.map.output=false  \
    -D mapreduce.map.memory.mb=3192  \
    -D mapred.job.reduce.capacity=300  \
    -D mapreduce.job.queuename=root.ad.model-offline  \
    -D num.key.fields.for.partition=1  \
    -D mapreduce.map.cpu.vcores=1  \
    -D abaci.split.remote=true  \
    -D mapred.output.compress=true  \
    -D mapred.reduce.tasks=1  \
    -D mapreduce.reduce.cpu.vcores=1  \
    -D mapred.min.split.size=268435456  \
    -cacheArchive hdfs://data-batch-hdfs/hive-dw/ad/tools/python27.tar.gz#python27  \
    -input ${file_input_path} \
    -mapper "python27/python27/bin/python ${mapper}" \
    -reducer "python27/python27/bin/python ${reduce}" \
    -file /data/huihao/study/study-hadoop/study_map_reduce/Commonconf.py \
    -file /data/huihao/study/study-hadoop/study_map_reduce/${mapper} \
    -file /data/huihao/study/study-hadoop/study_map_reduce/${reduce} \
    -output ${file_output_path} \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
}
train
#hadoop fs -cat ${file_output_path}/* | more
