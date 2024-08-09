import stockdaily.service as s
import datetime
import time


def run():
    for i in range(1, 5):
        s.prepare_to_update_history_hk()
        date_start = datetime.date(2020-i, 1, 1)
        date_end = datetime.date(2020-i, 12, 31)
        try:
            s.retrieve_history_hk(start_date=date_start, end_date=date_end)
            print("sleeping....")
            time.sleep(300)
        except Exception as err:
            print("sleeping....")
            time.sleep(300)
            s.retrieve_history_hk(start_date=date_start, end_date=date_end)

