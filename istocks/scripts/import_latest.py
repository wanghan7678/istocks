import stockdaily.service as s
import time


def run():
    s.import_latest_data(stock_type=s.stock_hk)
    print("sleep...")
    time.sleep(300)
    s.import_latest_data(stock_type=s.stock_us)



