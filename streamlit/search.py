import streamlit as st
from utils.request import trigger_airflow_dag

st.title("맛집 궁금해? 궁금하면 500원")

keyword_text = st.text_input("검색하고 싶은 지역을 적어주세요")

email_info = st.text_input("이메일 주소를 적어주세요")

if st.button("Trigger DAG"):
    if keyword_text:
        trigger_airflow_dag(keyword_text, email_info)
    else:
        st.error("Please enter a keyword.")