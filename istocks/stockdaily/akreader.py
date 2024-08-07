import akshare as ak


def read_hk_daily(code, start_year, end_year, adjust):
    stock_hk_d = ak.stock_zh_ah_daily(symbol=code, start_year=start_year, end_year=end_year, adjust=adjust)
    return stock_hk_d


def read_hk_qfq_factors(code):
    return ak.stock_hk_daily(symbol=code, adjust="qfq-factor")


def read_hk_spot(ak_code):
    # df = ak.stock_hk_hist(symbol=ak_code, period='daily', start_date='20230101', end_date='20230201', adjust='')
    # df = ak.stock_us_hist(symbol='106.TTE', period='daily', start_date='20230101', end_date='20230201', adjust='')
    df = ak.stock_us_spot_em()
    print(df)


def get_us_spot():
    df = ak.stock_us_spot_em()
    return df