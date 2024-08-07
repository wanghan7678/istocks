import akshare as ak
from stockdaily.models import HkQfqFactor, HkDailyPrices, StockUsList, StockHkList, UsDailyPrices
from stockdaily.util import to_float, to_hist_date_str, to_int


def read_hk_daily(code, start_year, end_year, adjust):
    stock_hk_d = ak.stock_zh_ah_daily(symbol=code, start_year=start_year, end_year=end_year, adjust=adjust)
    return stock_hk_d


def read_hk_qfq_factors(code):
    return ak.stock_hk_daily(symbol=code, adjust="qfq-factor")


def read_us_qfq_factors(code):
    return ak.stock_us_daily(symbol=code, adjust="qfq-factor")


def read_hk_spot(ak_code):
    # df = ak.stock_hk_hist(symbol=ak_code, period='daily', start_date='20230101', end_date='20230201', adjust='')
    # df = ak.stock_us_hist(symbol='106.TTE', period='daily', start_date='20230101', end_date='20230201', adjust='')
    df = ak.stock_us_spot_em()
    print(df)


def read_hk_hist(code, start_date, end_date):
    print("read stock: " + code + " from " + str(start_date) + " to " + str(end_date))
    df = ak.stock_hk_hist(symbol=code, period='daily', start_date=to_hist_date_str(start_date),
                          end_date=to_hist_date_str(end_date), adjust='')
    items = []
    for i in range(0, len(df)):
        item = HkDailyPrices()
        item.trade_date = df.iat[i, 0]
        item.code = code
        item.open_price = to_float(df.iat[i, 1])
        item.close_price = to_float(df.iat[i, 2])
        item.high_price = to_float(df.iat[i, 3])
        item.low_price = to_float(df.iat[i, 4])
        item.volume = to_int(df.iat[i, 5])
        item.turnover_rate = to_float(df.iat[i, 10])
        items.append(item)
    return items


def read_us_hist(code, start_date, end_date):
    print("read stock: " + code + " from " + str(start_date) + " to " + str(end_date))
    df = ak.stock_us_hist(symbol=code, period='daily', start_date=to_hist_date_str(start_date),
                          end_date=to_hist_date_str(end_date), adjust='')
    items = []
    for i in range(0, len(df)):
        item = UsDailyPrices()
        item.trade_date = df.iat[i, 0]
        item.code = code
        item.open_price = to_float(df.iat[i, 1])
        item.close_price = to_float(df.iat[i, 2])
        item.high_price = to_float(df.iat[i, 3])
        item.low_price = to_float(df.iat[i, 4])
        item.volume = to_int(df.iat[i, 5])
        item.turnover_rate = to_float(df.iat[i, 10])
        items.append(item)
    return items

def read_hk_qfq(code):
    print("  read qfq factors from ak sina: " + code)
    df = read_hk_qfq_factors(code=code)
    items = []
    for i in range(0, len(df)):
        item = HkQfqFactor()
        item.code = code
        item.trade_date = df.iat[i, 0]
        item.factor = to_float(df.iat[i, 1])
        items.append(item)
    return items


def read_us_qfq(code):
    print("  read qfq factors from ak sina: " + code)
    df = ak.stock_us_daily(symbol=code, adjust="qfq-factor")
    items = []
    for i in range(0, len(df)):
        item = HkQfqFactor()
        item.code = code
        item.trade_date = df.iat[i, 0]
        item.factor = to_float(df.iat[i, 1])
        items.append(item)
    return items


def temp():
    df = ak.stock_hk_hist(symbol="00005", period='daily', start_date="20240801",
                          end_date="20240807", adjust='')
    print(df)
