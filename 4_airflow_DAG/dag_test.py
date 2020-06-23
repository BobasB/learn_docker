from datetime import timedelta

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(1),
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('helloWorld', schedule_interval='*/5 * * * *', default_args=default_args)

t1 = BashOperator(
    task_id='task_1',
    bash_command='echo "Hello World from Task 1"',
    dag=dag
)

t2 = KubernetesPodOperator(
    name='print-from-pod',
    task_id='task_2',
    namespace='testing',
    service_account_name='default',
    security_context={"fsGroup": 2000},
    image='bobas/learn_docker:airflow',
    image_pull_policy='Always',
    resources={"request_cpu": "512m", "request_memory": "1Gi"},
    cmds=["python", "-c"],
    arguments=["from time import sleep; print(\"Simple K8S pod run\"); sleep(10)"],
    env_vars={
        'AWS_DEFAULT_REGION': "eu-west-1"
    },
    get_logs=True,
    in_cluster=True,
    is_delete_operator_pod=True,
    labels={'internetEgress': 'allow'},
    dag=dag
)

t3 = BashOperator(
    task_id='task_3',
    bash_command='echo "Hello World from Task 3"',
    dag=dag
)

t4 = BashOperator(
    task_id='task_4',
    bash_command='echo "Hello World from Task 4"',
    dag=dag
)

t2.set_upstream(t1)
t3.set_upstream(t1)
t4.set_upstream(t2)
t4.set_upstream(t3)
