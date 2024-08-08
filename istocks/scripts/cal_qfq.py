import stockdaily.prepare as p
import stockdaily.calculator as ca


def run():
    d, c = p.get_hk_daily_closes_qfq(code="00700", start_date='2023-08-01', end_date='2024-08-08')
    ca.get_macd(d, c)


