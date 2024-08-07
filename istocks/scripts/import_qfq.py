import stockdaily.service as s


def run():
    s.prepare_to_update_qfq_hk()
    s.retrieve_qfq_hk()
    s.prepare_to_update_qfq_us()
    s.retrieve_qfq_us()