from datetime import time

from stockdaily.models import StockHkList, StockUsList, StockDailyPrices
from stockdaily.util import to_ak_hk_code, to_int, to_float, to_date, ak_date_format
from stockdaily.akreader import read_hk_daily


def read_history_hk():
    stock_codes = StockHkList.objects.filter(indices='HSI').values_list('code', flat=True)
    ak_codes = get_ak_codes(stock_codes)
    for ak_code in ak_codes:
        print("read from ak sina:  " + ak_code)
        df = read_hk_daily(code=ak_code, adjust="qfq")
        dailys = []
        for i in range(0, len(df)):
            hk_daily = StockDailyPrices()
            hk_daily.trade_date = df.iat[i, 0]
            hk_daily.exchange = 'HK'
            hk_daily.code = ak_code
            hk_daily.open_price = to_float(df.iat[i, 1])
            hk_daily.close_price = to_float(df.iat[i, 2])
            hk_daily.high_price = to_float(df.iat[i, 3])
            hk_daily.low_price = to_float(df.iat[i, 4])
            hk_daily.volume = to_int(df.iat[i, 5])
            hk_daily.fq_type = "qfq"
            dailys.append(hk_daily)
        StockDailyPrices.objects.bulk_create(dailys)
        print("    totally " + str(len(dailys)) + "  saved.")
        time.sleep(5)


def get_ak_codes(codes):
    results = []
    for code in codes:
        results.append(to_ak_hk_code(code))
    return results


