import datetime
from stockdaily.models import StockHkList, StockUsList, HkDailyPrices, HkQfqFactor, UsQfqFactor, UsDailyPrices
import stockdaily.calculator as ca
import stockdaily.service as s
import stockdaily.prepare as p

default_period_days = 360


def cal_save_macd_hk():
    now_date = datetime.datetime.now().date()
    start_date = now_date - datetime.timedelta(default_period_days)
    cal_update_macd_hk(start_date=start_date)


def cal_update_macd_hk(start_date):
    now_date = datetime.datetime.now().date()
    s.update_status_to(s.stock_hk, s.status_to_update_signal)
    stocks = StockHkList.objects.filter(status=s.status_to_update_signal).all()
    for stock in stocks:
        dates, prices = p.get_hk_daily_closes_qfq(code=stock.code, start_date=start_date, end_date=now_date)
        items = ca.get_macd(code=stock.code, dates=dates, closes=prices)
        print("  calculate " + stock.code + " MACD Golden: totally " + len(items) + " saved.")
        s.update_items(model_name=s.model_hk_signal, items=items, stock=stock)


def cal_signal_labels(signal):
    pass