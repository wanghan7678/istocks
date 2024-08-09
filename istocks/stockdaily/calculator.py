import stockdaily.prepare as pr
from talib import MACD
import numpy as np
from stockdaily.models import HkSignal

trust_pre_period = 3
space_period = 40

signal_name_macd_golden = 'macd_golden'

signal_status_new = 'new'


def get_macd_golden(code, dates, closes):
    results = []
    closes.reverse()
    dates.reverse()
    dif, dea, macdhist = MACD(np.array(closes), fastperiod=12, slowperiod=26, signalperiod=9)
    for i in range(space_period + trust_pre_period, len(dif)):
        if check_all_less(list_a=dif, list_b=dea, end_index=i, period=trust_pre_period) and dif[i] >= dea[i]:
            sig = HkSignal()
            sig.code = code
            sig.trade_date = dates[i]
            sig.signal_name = signal_name_macd_golden
            sig.status = signal_status_new
            results.append(sig)
    return results


def check_all_less(list_a, list_b, end_index, period):
    for i in range(1, period):
        if list_a[end_index - i] >= list_b[end_index - i]:
            return False
    return True


