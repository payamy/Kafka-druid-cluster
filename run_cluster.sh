# Building Kafka producer Docker image
docker build -t kafka-python-producer:0.0.1 ./producer &&

# Building Apache Druid's custom Docker image
docker build -t druid-hdfs:24.0.1 ./druid &&

# Running cluster
docker-compose -f docker-compose.yml -f docker-compose-airflow.yml -f docker-compose-druid.yml up -d --remove-orphans
