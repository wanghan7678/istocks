import stockdaily.prepare as pr
from talib import MACD


def get_macd(dates, closes):
    closes_asc = closes.reverse()
    dates_asc = dates.reverse()
    dif, dea, macdhist = MACD(closes_asc, fastperiod=12, slowperiod=26, signalperiod=9)
    print(macdhist)


