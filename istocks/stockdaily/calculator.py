import stockdaily.prepare as pr
from talib import MACD
import numpy as np
from stockdaily.models import HkSignal

trust_pre_period = 3
space_period = 40

signal_name_macd_golden = 'macd_golden'
signal_name_macd_death = 'macd_death'

signal_status_new = 'new'


def get_macd_golden(code, dates, closes):
    results = []
    goldens = []
    closes.reverse()
    dates.reverse()
    dif, dea, macdhist = MACD(np.array(closes), fastperiod=12, slowperiod=26, signalperiod=9)
    for i in range(space_period + trust_pre_period, len(dif)):
        if check_all_less(list_a=dif, list_b=dea, end_index=i, period=trust_pre_period) and dif[i] >= dea[i]:
            goldens.append(i)
    for i in range(0, len(goldens)):
        cross_index = goldens[i]
        sig = HkSignal()
        sig.code = code
        sig.trade_date = dates[cross_index]
        sig.signal_name = signal_name_macd_golden
        sig.status = signal_status_new
        print("date: " + str(sig.trade_date))
        if closes[cross_index] == 0:
            continue
        if cross_index + 5 < len(closes):
            print("   " + str(closes[cross_index + 5]))
            sig.chg_pct_5d = (closes[cross_index + 5] - closes[cross_index]) / closes[cross_index]
        if cross_index + 10 < len(closes):
            sig.chg_pct_10d = (closes[cross_index + 10] - closes[cross_index]) / closes[cross_index]
        if cross_index + 20 < len(closes):
            sig.chg_pct_10d = (closes[cross_index + 10] - closes[cross_index]) / closes[cross_index]
        results.append(sig)
    return results


def get_macd_death(code, dates, closes):
    results = []
    deaths = []
    closes.reverse()
    dates.reverse()
    dif, dea, macdhist = MACD(np.array(closes), fastperiod=12, slowperiod=26, signalperiod=9)
    for i in range(space_period + trust_pre_period, len(dif)):
        if check_all_greater(list_a=dif, list_b=dea, end_index=i, period=trust_pre_period) and dif[i] <= dea[i]:
            deaths.append(i)
    for i in range(0, len(goldens)):
        sig = HkSignal()
        sig.code = code
        sig.trade_date = dates[goldens[i]]
        sig.signal_name = signal_name_macd_golden
        sig.status = signal_status_new
        results.append(sig)
    return results


def check_all_less(list_a, list_b, end_index, period):
    for i in range(1, period):
        if list_a[end_index - i] >= list_b[end_index - i]:
            return False
    return True


def check_all_greater(list_a, list_b, end_index, period):
    for i in range(1, period):
        if list_a[end_index - i] <= list_b[end_index - i]:
            return False
    return True


