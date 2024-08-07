from stockdaily.service import read_history_hk, read_one_history_hk


def run():
    read_one_history_hk("00700", "qfq")
