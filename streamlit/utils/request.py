import requests
import uuid
from requests.auth import HTTPBasicAuth

def trigger_airflow_dag(keyword, user_email):
    airflow_url = "http://localhost:8080/api/v1/dags/boaz_menmen_study_dag/dagRuns"
    user_name = "admin"
    user_password = "admin"
    dag_run_uuid = str(uuid.uuid4())
    
    request_data = {
        "dag_run_id" : dag_run_uuid,
        "conf" :{
            "user_email" : user_email,
            "user_keyword" : keyword,
        }
    }
    
    response = requests.post(
        airflow_url,
        auth=HTTPBasicAuth(user_name, user_password),
        headers={"Content-Type": "application/json"},
        json=request_data
    )

    return response