import pandas as pd

from config import settings as mys_setting


def write_file_xlsx(data, sheet_name):
    data = pd.DataFrame(data, index=[1])
    writer = pd.ExcelWriter(mys_setting.URL_OUTPUT + 'info_person.xlsx', engine='xlsxwriter')
    data.to_excel(writer, sheet_name=sheet_name)
    writer.save()


def write_file_feed_xlsx(data, sheet_name):
    data = pd.DataFrame.from_records(data)
    writer = pd.ExcelWriter(mys_setting.URL_OUTPUT + 'info_feed.xlsx', engine='xlsxwriter',
                            options={'strings_to_urls': False})
    data.to_excel(writer, sheet_name=sheet_name)
    writer.save()
