import stockdaily.service as s


def run():
    s.retrieve_qfq_hk()
    s.prepare_to_update_qfq_us()
    s.retrieve_qfq_us()
