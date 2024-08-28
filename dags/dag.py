from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator

default_args = {
    "owner" : "Jin",
    "depends_on_past" : False,
    "email" : ["eu2525@naver.com"],
    "email_on_failure" : False,
    "email_on_retry" : False,
    "retries" : 0,
}

dag = DAG(
    dag_id="boaz_menmen_study_dag",
    default_args = default_args,
    description="Menmen Study Practice",
    schedule_interval=None,
    start_date=datetime(2024,8,25),
    tags=["boaz_menmen"]
)

start = BashOperator(task_id="start_dag", bash_command='echo "start"', dag= dag)

send_email = KubernetesPodOperator(
    task_id="send_email",
    startup_timeout_seconds=300,
    name="send_eamil",
    namespace="airflow",  # Replace with your namespace
    image="hsjindoc/boaz_practice:1.0",  # Replace with your Docker image
    env_vars={
        "USER_EMAIL": '{{ dag_run.conf["user_email"] }}',
        "USER_KEYWORD": '{{ dag_run.conf["user_keyword"] }}'
    },
    image_pull_policy='Always',
    is_delete_operator_pod=True,
    dag=dag
)

complete = BashOperator(task_id="complete_dag", bash_command='echo "complete"', dag= dag)


start >> send_email >> complete