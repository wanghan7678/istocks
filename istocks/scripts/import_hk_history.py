import stockdaily.service as s
import datetime


def run():
    s.prepare_to_update_history_hk()
    date_start = datetime.date(2024, 1, 1)
    date_end = datetime.date(2024, 8, 8)
    s.retrieve_history_hk(start_date=date_start, end_date=date_end)
