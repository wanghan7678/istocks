import stockdaily.prepare as p


def run():
    d = p.get_hk_qfq_data(code="00005", start_date='2023-08-01', end_date='2023-08-20')
    print(d)
