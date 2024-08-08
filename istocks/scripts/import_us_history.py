import stockdaily.service as s
import datetime


def run():
    s.prepare_to_update_history_us()
    date_start = datetime.date(2021, 1, 1)
    date_end = datetime.date(2021, 12, 31)
    s.retrieve_history_us(start_date=date_start, end_date=date_end)
