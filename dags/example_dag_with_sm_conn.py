from airflow.decorators import dag
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator



@dag(
    schedule=None,
    dag_id="example_dag_with_sm_conn"
)
def my_dag():
    results = SQLExecuteQueryOperator(
        task_id="execute_query",
        conn_id="my_mysql_instance",  # Omit the 'airflow/connections' prefix defined in the name of the secret in Secrets Manager
        sql=f"SELECT * FROM actor LIMIT 50;"
    )


my_dag()
