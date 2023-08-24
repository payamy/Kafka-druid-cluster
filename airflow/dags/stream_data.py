from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'Payam',
    'start_date': datetime(2023, 1, 1),
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
}


def load_data():
    pass


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
