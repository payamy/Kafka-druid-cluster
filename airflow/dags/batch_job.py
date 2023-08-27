from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from ds import DruidDatasource

from requests.auth import HTTPBasicAuth
import requests

start_date = datetime.today()

default_args = {
    'owner': 'Payam',
    'start_date': datetime(start_date.year, start_date.month, start_date.day, 2, 30, 0),
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
}


def load_data():
    conf = DruidDatasource.load_json_batch_job()
    auth = HTTPBasicAuth('admin', 'druidAdminPassword')
    requests.post(
        url='http://router:8888/druid/v2/sql/task',
        json=conf,
        auth=auth,
    )


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
