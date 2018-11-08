import requests

from config import settings as mys_setting


def get_info(fb_id, access_token):
    url = mys_setting.URL_GRAPHQL_FB + mys_setting.VERSION + fb_id + mys_setting.ACCESS_TOKEN
    result_data = requests.get(url + format(access_token)).json()

    return result_data


def get_info_fields(field_name, fb_id, access_token):
    url = mys_setting.URL_GRAPHQL_FB + mys_setting.VERSION + fb_id + field_name + mys_setting.ACCESS_TOKEN
    result_data = requests.get(url + format(access_token)).json()
    dt_list = result_data['data']
    return dt_list
