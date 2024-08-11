import stockdaily.prepare as p
import stockdaily.calculator as ca


def run():
    d, c = p.get_hk_daily_closes_qfq(code="00700", start_date='2023-08-01', end_date='2024-08-08')
    items = ca.get_macd_golden("00700", d, c)
    for i in items:
        print(i.trade_date)
        print("  " + str(i.chg_pct_5d))
        print("  " + str(i.chg_pct_10d))
        print("  " + str(i.chg_pct_20d))


