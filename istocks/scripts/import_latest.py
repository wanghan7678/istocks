import stockdaily.service as s


def run():
    s.update_status_to(stock_type=s.stock_hk, status=s.status_to_update_daily)
    s.import_latest_data()



