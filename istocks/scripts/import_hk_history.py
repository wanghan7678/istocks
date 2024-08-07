import stockdaily.service as s
import datetime


def run():
    s.prepare_to_update_daily_hk()
    date_start = datetime.datetime(2023, 1, 1)
    date_end = datetime.datetime(2023, 12, 31)
    s.retrieve_history_hk(start_date=date_start, end_date=date_end)
