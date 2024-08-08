import stockdaily.prepare as pr
from talib import MACD
import numpy as np


def get_macd(dates, closes):
    n = len(closes)
    closes.reverse()
    dates.reverse()
    print(closes[n-1])
    dif, dea, macdhist = MACD(np.array(closes), fastperiod=12, slowperiod=26, signalperiod=9)
    print("dif: " + str(dif[n-1]) + ", dea: " + str(dea[n-1]) + ", hist: " + str(macdhist[n-1]))



