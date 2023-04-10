import requests
from pandas import json_normalize



def process_request(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def json_items_to_dataframe(http_response, record_path, meta):
    return json_normalize(
        http_response,
        record_path=record_path,
        meta=meta
    )