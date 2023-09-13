
# Kafka Druid Cluster

Here is the code and config files provided for deploying Kafka and Apache Druid cluster using Docker Swarm.

The producer script pushes random data to a Kafka topic which has four partitions and two replicas.

The Druid cluster is using HDFS as its deep storage.

Also, Apache Airflow is used to automate Druid data ingestion. Airflow has two dags:
- The first dag submits a supervisor to the Druid cluster to ingest data from the Kafka topic and stores them to the datasource.
- The second dag is to perform Multi-Stage Query on Druid real-time datasource and store the result into a new datasource.

Note #1: Due to resource limitations, the second dag is disabled.

Note #2: You can check if everything works fine using Druid Web UI (Username: admin, Password: druidAdminPassword)

Note #3: You can access Druid web UI using this url: http://45.159.149.181:8888
