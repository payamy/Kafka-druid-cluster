from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from requests.auth import HTTPBasicAuth
import requests
import json
import time


class DruidDatasource:

    @staticmethod
    def load_json():
        path = f'/opt/airflow/dags/kafka_ds_config.json'
        try:
            with open(path, "r") as config_file:
                conf = json.load(config_file)
        except FileNotFoundError:
            raise FileNotFoundError('Config file not found')

        return conf




default_args = {
    'owner': 'Payam',
    'start_date': datetime(2023, 1, 1),
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
}


def load_data():
    conf = DruidDatasource.load_json()
    auth = HTTPBasicAuth('admin', 'druidAdminPassword')
    res = requests.post(
        url='http://router:8888/druid/indexer/v1/supervisor',
        json=conf,
        auth=auth,
    )
    time.sleep(60)
    supervisor_id = json.loads(res._content)['id']
    res_2 = requests.get(
        url=f'http://router:8888/druid/indexer/v1/supervisor/{supervisor_id}/status',
        auth=auth,
    )
    healthy = str(json.loads(res_2._content)['payload']["state"])
    if healthy == "RUNNING":
        print('Data loaded to Druid datasource')
    else:
        raise AirflowException('Submitting supervisor was unsuccessful')


with DAG(
    dag_id="stream_data",
    description="Stream Data from Kafka Topic to Apache Druid Datasource",
    default_args=default_args,
    schedule_interval="@once",
) as dag:

    task1 = PythonOperator(
        task_id="load_data",
        python_callable=load_data,
    )

    task1
