from stockdaily.service import retrieve_history_hk


def run():
    retrieve_history_hk(start_year='2014', end_year='2024')
