import json


class DruidDatasource:

    @staticmethod
    def __load_json(path: str):
        try:
            with open(path, "r") as config_file:
                conf = json.load(config_file)
        except FileNotFoundError:
            raise FileNotFoundError('Config file not found')

        return conf

    @staticmethod
    def load_json_stream_data():
        path = f'/opt/airflow/dags/configs/kafka_ds_config.json'
        return DruidDatasource.__load_json(path)

    @staticmethod
    def load_json_batch_job():
        path = f'/opt/airflow/dags/configs/druid_batch_job.json'
        return DruidDatasource.__load_json(path)
