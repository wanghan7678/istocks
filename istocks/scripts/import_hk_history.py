from stockdaily.service import retrieve_history_hk, read_one_history_hk, \
    check_duplicate_code_date, save_hk_daily


def run():
    retrieve_history_hk(start_year='2023', end_year='2024')
