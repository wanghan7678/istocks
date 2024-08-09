import stockdaily.service as s
import datetime
import time

from django.db import IntegrityError


def run(*args):
    if len(args) > 1:
        s.update_status_to(stock_type=s.stock_hk, status=s.status_to_update_hist)
        date_start = datetime.datetime.strptime(args[0], "%Y-%m-%d").date()
        date_end = datetime.datetime.strptime(args[1], "%Y-%m-%d").date()
        s.read_save_history_us(start_date=date_start, end_date=date_end)
    else:
        print("input --script-args <start_date:yyyy-mm-dd> <end_date:yyyy-mm-dd>")



