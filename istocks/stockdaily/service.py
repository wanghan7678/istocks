from datetime import time

from stockdaily.models import StockHkList, StockUsList, HkDailyPrices, HkQfqFactor
from stockdaily.util import to_ak_hk_code, to_int, to_float, to_date, ak_date_format
from stockdaily.akreader import read_hk_daily, read_hk_qfq_factors


def retrieve_history_hk(start_year, end_year):
    stock_codes = StockHkList.objects.filter(indices='HSI').values_list('code', flat=True)
    ak_codes = get_ak_codes(stock_codes)
    for ak_code in ak_codes:
        read_one_history_hk(ak_code=ak_code, start_year=start_year, end_year=end_year, adjust="")
        time.sleep(1)
        read_hk_qfq(code=ak_code)
        time.sleep(4)


def read_hk_qfq(code):
    print("  read qfq factors from ak sina: " + code)
    df = read_hk_qfq_factors(code=code)
    items = []
    for i in range(0, len(df)):
        item = HkQfqFactor()
        item.code = code,
        item.start_date = df.iat[i, 0]
        item.factor = to_float(df.iat[i, 1])
        items.append(item)
    HkQfqFactor.objects.bulk_create(items)
    print("      totally " + str(len(items)) + "  saved.")


def read_one_history_hk(ak_code, start_year, end_year, adjust):
    print("read from ak sina:  " + ak_code)
    df = read_hk_daily(code=ak_code, start_year=start_year, end_year=end_year, adjust=adjust)
    items = []
    for i in range(0, len(df)):
        item = HkDailyPrices()
        item.trade_date = df.iat[i, 0]
        item.code = ak_code
        item.open_price = to_float(df.iat[i, 1])
        item.close_price = to_float(df.iat[i, 2])
        item.high_price = to_float(df.iat[i, 3])
        item.low_price = to_float(df.iat[i, 4])
        item.volume = to_int(df.iat[i, 5])
        items.append(item)
    HkDailyPrices.objects.bulk_create(items)
    print("    totally " + str(len(items)) + "  saved.")


def get_ak_codes(codes):
    results = []
    for code in codes:
        results.append(to_ak_hk_code(code))
    return results


