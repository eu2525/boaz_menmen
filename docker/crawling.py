import os
import requests
import json
import pandas as pd 
from dotenv import load_dotenv

from utils.preprocess import json_to_df
from utils.request import send_email

load_dotenv()

def request_url(keyword_text):
    # Set the URL for the POST request
    url = "https://im.diningcode.com/API/isearch/"

    # Define the headers from the Request Headers section
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Length": "169",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "im.diningcode.com",
        "Origin": "https://www.diningcode.com",
        "Referer": "https://www.diningcode.com/",
        "Sec-Ch-Ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }

    data = {
        "query": f"{keyword_text}",
        "addr": "",
        "keyword": "",
        "order": "r_score",
        "distance": "",
        "rn_search_flag": "on",
        "search_type": "poi_search",
        "lat": "",
        "lng": "",
        "rect": "",
        "s_type": "poi",
        "dc_flag": "1",
        "page": "1",
        "size": "50"
    }

    # Make the POST request
    response = requests.post(url, headers=headers, data=data).json()

    return response

if __name__ == "__main__":
    keyword = os.getenv("USER_KEYWORD")
    recv_eamil = os.getenv("USER_EMAIL")

    raw_data = request_url(keyword)
    df = json_to_df(raw_data)
    send_email(recv_eamil, df)
