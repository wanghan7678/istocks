import stockdaily.service as s
import time


def run(*args):
    if len(args) > 0:
        s.import_latest_data(args[0])
    else:
        print("input --script-args <stock_type: hk or us> ")


