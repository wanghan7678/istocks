import akshare as ak


def read_hk_daily(code, start_year, end_year, adjust):
    stock_hk_d = ak.stock_zh_ah_daily(symbol=code, start_year=start_year, end_year=end_year, adjust=adjust)
    return stock_hk_d


def read_hk_qfq_factors(code):
    return ak.stock_hk_daily(symbol=code, adjust="qfq-factor")

