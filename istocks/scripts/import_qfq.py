import stockdaily.service as s


def run():
    # s.retrieve_qfq_hk()
    s.update_status_to(stock_type=s.stock_us, status=s.status_to_update_qfq)
    s.save_read_qfq_us()
    s.update_status_to(stock_type=s.stock_hk, status=s.status_to_update_qfq)
    s.save_read_qfq_hk()
