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


def create_macd_goldens(stock_type, start_date):
    if stock_type == s.stock_hk:
        s.update_status_to(stock_type=s.stock_hk, status=s.status_to_update_signal)
        cal_update_macd_hk(start_date=start_date, to_create=True)
    if stock_type == s.stock_us:
        s.update_status_to(stock_type=s.stock_us, status=s.status_to_update_signal)
        cal_update_macd_us(start_date=start_date, to_create=True)


def cal_update_macd_hk(start_date, to_create):
    now_date = datetime.datetime.now().date()
    s.update_status_to(s.stock_hk, s.status_to_update_signal)
    stocks = StockHkList.objects.filter(status=s.status_to_update_signal).all()
    for stock in stocks:
        dates, prices = p.get_hk_daily_closes_qfq(code=stock.code, start_date=start_date, end_date=now_date)
        items = ca.get_macd_hk(code=stock.code, dates=dates, closes=prices)
        print("  calculate " + stock.code + " MACD Golden: totally " + str(len(items)) + " saved.")
        if to_create:
            s.insert_items(model_name=s.model_hk_sig, items=items, stock=stock)
        else:
            s.update_items(model_name=s.model_hk_sig, items=items, stock=stock)


def cal_update_macd_us(start_date, to_create):
    now_date = datetime.datetime.now().date()
    s.update_status_to(s.stock_us, s.status_to_update_signal)
    stocks = StockUsList.objects.filter(status=s.status_to_update_signal).all()
    for stock in stocks:
        dates, prices = p.get_hk_daily_closes_qfq(code=stock.ak_code, start_date=start_date, end_date=now_date)
        items = ca.get_macd_us(code=stock.ak_code, dates=dates, closes=prices)
        print("  calculate " + stock.code + " MACD Golden: totally " + len(items) + " saved.")
        if to_create:
            s.insert_items(model_name=s.model_us_signal, items=items, stock=stock)
        else:
            s.update_items(model_name=s.model_us_signal, items=items, stock=stock)


def cal_signal_labels(signal):
    pass
