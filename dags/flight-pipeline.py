import sys
from pathlib import Path
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

AIRFLOW_HOME = Path("/opt/airflow")

if str(AIRFLOW_HOME) not in sys.path:
    sys.path.insert(0, str(AIRFLOW_HOME))

from scripts.bronze_ingest import run_bronze_ingestion


default_args = {
    "owner": "airflow",
    "retries": 0,
    "retry_delay" : timedelta(minutes=5),
}

with DAG(
    dag_id="flights_ops_medallion_pipe",
    default_args=default_args,
    start_date=datetime(2026, 2, 28),
    schedule_interval="*/30 * * * *",
    catchup=False,
) as dag:

    bronze = PythonOperator(
        task_id="bronze_ingest",
        python_callable=run_bronze_ingestion,
    )

