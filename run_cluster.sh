# Building Kafka producer Docker image
docker build -t kafka-python-producer:0.0.1 ./producer &&
docker tag kafka-python-producer:0.0.1 payamyprojects.com/kafka-python-producer:0.0.1 &&
docker push payamyprojects.com/kafka-python-producer:0.0.1 &&

# Building Apache Druid's custom Docker image
docker build -t druid-hdfs:24.0.1 ./druid &&
docker tag druid-hdfs:24.0.1 payamyprojects.com/druid-hdfs:24.0.1 &&
docker push payamyprojects.com/druid-hdfs:24.0.1 &&

# Running cluster
docker-compose -f docker-compose.yml -f docker-compose-airflow.yml -f docker-compose-druid.yml config > docker-compose.stack.yml &&
export $(cat .env) > /dev/null 2>&1; docker stack deploy -c docker-compose.stack.yml kafka-druid-cluster --with-registry-auth
