from __future__ import annotations

import datetime

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator 
from airflow.operators.empty import EmptyOperator

#DAG에 대한 정의 // 모든 덱에 필요함
with DAG(
    dag_id="dags_bash_operator", # DAG 의 이름 _ 파이썬 파일명과는 상관이 없다. // 덱 파일명과 덱이름은 통일 시켜주는 것이 좋다. 
    schedule="0 0 * * *", #분 시 일 월 요일 _ 언제 돌지를 정함 
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"), # 언제부터 돌지를 정함 UTC = 표준시간 / 아시아 서울 시간으로 변경 
    catchup=False, # 사이의 누락된 구간을 돌릴지 안돌릴지 / True 의 경우 한꺼번에 돌게 되기 때문에 덱을 어떻게 만들었냐에 따라 문제가 발생함 // False로 해두는 것을 권장함 
    #dagrun_timeout=datetime.timedelta(minutes=60), # 60분 이상 돌게 되면 실패하도록 설정 
    #tags=["example", "example2"], ## 사이트의 파란색 값 // 사이트에서 누르면 그것만 필터링하여 볼 수 있음 
    #params={"example_key": "example_value"}, #공통적으로 넘겨줄 파라미터 값 
) as dag:
    
    # [START howto_operator_bash]
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    # [END howto_operator_bash]
    bash_t1 >> bash_t2