
# Kafka Druid Cluster

Here is the code and config files provided for deploying Kafka and Apache Druid cluster using Docker Swarm.

The producer script pushes random data to a Kafka topic which has four partitions and two replicas.

The Druid cluster is using HDFS as its deep storage.

Also, Apache Airflow is used to automate Druid data ingestion. Airflow has two dags:
- The first dag submits a supervisor to the Druid cluster to ingest data from the Kafka topic and stores them to the datasource.
- The second dag is to perform Multi-Stage Query on Druid real-time datasource and store the result into a new datasource.
