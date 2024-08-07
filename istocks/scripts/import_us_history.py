import stockdaily.service as s
import datetime


def run():
    s.prepare_to_update_history_us()
    date_start = datetime.date(2023, 1, 1)
    date_end = datetime.date(2023, 12, 31)
    s.re(start_date=date_start, end_date=date_end)
