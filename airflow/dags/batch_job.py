from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from ds import DruidDatasource

from requests.auth import HTTPBasicAuth
import requests

start_date = datetime.today() - timedelta(days=1)

default_args = {
    'owner': 'Payam',
    'start_date': datetime(start_date.year, start_date.month, start_date.day, 2, 30, 0),
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
}


def load_data():
    conf = DruidDatasource.load_json_batch_job()
    auth = HTTPBasicAuth('admin', 'druidAdminPassword')
    res = requests.post(
        url='http://router:8888/druid/v2/sql/task',
        json=conf,
        auth=auth,
    )
    print(res._content)


with DAG(
    dag_id="batch_job",
    description="Apache Druid Multi-Stage Query Batch Job",
    default_args=default_args,
    schedule_interval="@daily",
) as dag:

    task1 = PythonOperator(
        task_id="load_data",
        python_callable=load_data,
    )

    task1
