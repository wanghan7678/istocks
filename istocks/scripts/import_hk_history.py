import time
import stockdaily.service as s
import datetime

from django.db import IntegrityError


def run(*args):
    if len(args) > 1:
        s.prepare_to_update_history_hk()
        date_start = datetime.datetime.strptime(args[0], "%Y-%m-%d").date()
        date_end = datetime.datetime.strptime().date()
        try:
            s.retrieve_history_hk(start_date=date_start, end_date=date_end)
        except IntegrityError as err1:
            print("Integration Error.")
        except Exception as err:
            print("sleeping....")
            time.sleep(300)
            print("try again....")
            s.retrieve_history_hk(start_date=date_start, end_date=date_end)
    else:
        print("input --script-args <start_date:yyyy-mm-dd> <end_date:yyyy-mm-dd>")
