import stockdaily.signal_service as ss


def run(*args):
    if len(args) > 1:
        s.update_status_to(stock_type=s.stock_us, status=s.status_to_update_his)
        stock_type = args[0]
        start_date = datetime.datetime.strptime(args[1], "%Y-%m-%d").date()
        ss.create_macd_goldens(stock_type=stock_type, start_date=start_date)
    else:
        print("input --script-args <stock_type: hk or us> <start_date: yyyy-mm-dd>")
