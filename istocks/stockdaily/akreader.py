import akshare as ak

start_year = "2018"
end_year = "2024"

df = ak.stock_zh_ah_daily(symbol="01810", start_year="2018", end_year="2024", adjust="")
print(df)


def read_hk_daily(code, adjust="qfq"):
    stock_hk_d = ak.stock_zh_ah_daily(symbol=code, start_year=start_year, end_year=end_year, adjust=adjust)
    return stock_hk_d
