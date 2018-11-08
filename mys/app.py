from mys_batch import service_batch as mys_batch
from mys import utils as mys_utils


def written_file_feed(field_name, uid, access_token):
    data_person_info_status = mys_batch.get_info_fields(field_name, uid, access_token)
    try:
        mys_utils.write_file_feed_xlsx(data_person_info_status, 'person_info_status')
        print("file written !")
    except Exception as err:
        print(err.args)


if __name__ == '__main__':
    access_token = "EAAD1JA3fTSYBAOAmCEaWOGFrXsXcQYT87wZAhSFzVpz4A7F5GxrsojkEGZBoPdln8z4rryytc94PF4hN0wbk885vjSkE6hMTTadguiOjs5Eszj5BrVdMLjPQ01Xb54gzwGXv1tLIvEKNHPqaYRrpIdH7ZB1F9celt23KUeUZB9azFDj4MNxunZBSnaZAcvIa9Nmr2w5iyLDAZDZD"
    uid = '772247376441327'
    field_name = '/feed'
    written_file_feed(field_name, uid, access_token)
