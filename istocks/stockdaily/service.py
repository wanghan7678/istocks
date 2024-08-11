import time
from django.db import IntegrityError
from stockdaily.models import StockHkList, StockUsList, HkDailyPrices, HkQfqFactor, UsQfqFactor, UsDailyPrices, HkSignal, UsSignal
from stockdaily.util import to_ak_hk_code, to_int, to_float, to_date, ak_date_format
from stockdaily.akreader import read_hk_qfq, read_us_qfq, read_hk_hist, read_us_hist, read_us_spot
import datetime

status_to_update_qfq = "to qfq"
status_to_update_his = "to his"
status_to_update_daily = "to daily"
status_to_update_signal = "to signal"
status_finished = "finished"
status_update_error = "update error"

stock_hk = "hk"
stock_us = "us"

model_hk_list = 'hk_list'
model_hk_daily = 'hk_daily'
model_hk_qfq = 'hk_qfq'
model_hk_sig = 'hk_sig'
model_us_list = 'us_list'
model_us_daily = 'us_daily'
model_us_qfq = 'us_qfq'
model_us_sig = 'us_sig'


def insert_items(model_name, items, stock):
    try:
        print("      " + str(len(items)) + "  saved.")
        if model_name == model_hk_list:
            StockHkList.objects.bulk_create(items)
        elif model_name == model_hk_qfq:
            HkQfqFactor.objects.bulk_create(items)
        elif model_name == model_hk_daily:
            HkDailyPrices.objects.bulk_create(items)
        elif model_name == model_hk_sig:
            print("  insert " + model_name + ",  type=" + str(type(items)))
            for i in items:
                print(i.trade_date)
            HkSignal.objects.bult_create(items)
        elif model_name == model_us_list:
            StockUsList.objects.bulk_create(items)
        elif model_name == model_us_qfq:
            UsQfqFactor.objects.bulk_create(items)
        elif model_name == model_us_daily:
            UsDailyPrices.objects.bulk_create(items)
        elif model_name == model_us_sig:
            UsSignal.objects.bulk_create(items)
        if stock:
            stock.status = status_finished
    except IntegrityError as err1:
        print("duplicated key error: ", type(err1).__name__)
        if stock:
            stock.status = status_update_error
    except Exception as err:
        print("An error: ", type(err).__name__)
        print("    " + str(err))
        if stock:
            stock.status = status_update_error
    finally:
        if stock:
            stock.save()


def update_create_items(model_name, items, stock):
    try:
        print("      " + str(len(items)) + "  saved.")
        if model_name == model_hk_list:
            for item in items:
                StockHkList.objects.update_or_create(item)
        elif model_name == model_hk_qfq:
            for item in items:
                HkQfqFactor.objects.update_or_create(item)
        elif model_name == model_hk_daily:
            for item in items:
                HkDailyPrices.objects.update_or_create(item)
        elif model_name == model_hk_sig:
            for item in items:
                HkSignal.objects.update_or_create(item)
        elif model_name == model_us_list:
            for item in items:
                StockUsList.objects.update_or_create(item)
        elif model_name == model_us_qfq:
            for item in items:
                UsQfqFactor.objects.update_or_create(item)
        elif model_name == model_us_daily:
            for item in items:
                UsDailyPrices.objects.update_or_create(item)
        elif model_name == model_hk_sig:
            for item in items:
                UsSignal.objects.update_or_create(item)
        if stock:
            stock.status = status_finished
    except IntegrityError as err1:
        print("duplicated key error: ", type(err1).__name__)
        if stock:
            stock.status = status_update_error
    except Exception as err:
        print("An error: ", type(err).__name__)
        if stock:
            stock.status = status_update_error
    finally:
        if stock:
            stock.save()


def read_save_history_hk(start_date, end_date):
    stocks = StockHkList.objects.filter(status=status_to_update_his).all()
    for stock in stocks:
        items = read_hk_hist(code=stock.code, start_date=start_date, end_date=end_date)
        insert_items(model_name=model_hk_daily, items=items, stock=stock)
        time.sleep(5)


def read_save_history_us(start_date, end_date):
    stocks = StockUsList.objects.filter(status=status_to_update_his).all()
    for stock in stocks:
        if stock.ak_code:
            items = read_us_hist(code=stock.ak_code, start_date=start_date, end_date=end_date)
            insert_items(model_name=model_us_daily, items=items, stock=stock)
            time.sleep(5)


def read_save_qfq_hk():
    stocks = StockHkList.objects.filter(status=status_to_update_qfq).all()
    for stock in stocks:
        items = read_hk_qfq(code=stock.code)
        insert_items(model_name=model_hk_qfq, items=items, stock=stock)
        time.sleep(3)


def read_save_qfq_us():
    stocks = StockUsList.objects.filter(status=status_to_update_qfq).all()
    for stock in stocks:
        items = read_us_qfq(code=stock.code)
        insert_items(model_name=model_us_qfq, items=items, stock=stock)
        time.sleep(3)


def read_update_qfq(stock_type):
    if stock_type == stock_hk:
        stocks = StockHkList.objects.filter(status=status_to_update_qfq).all()
        for stock in stocks:
            items = read_hk_qfq(stock.code)
            update_create_items(model_name=model_hk_qfq, items=items, stock=stock)
    elif stock_type == stock_us:
        stocks = StockUsList.objects.filter(status=status_to_update_qfq).all()
        for stock in stocks:
            items = read_us_qfq(stock.code)
            update_create_items(model_name=model_us_qfq, items=items, stock=stock)


def update_hk_akcodes():
    for item in StockHkList.objects.all():
        item.code = to_ak_hk_code(item.code)
        item.save()


def read_save_qfq_hk_one(ak_code):
    items = read_hk_qfq(code=ak_code)
    insert_items(model_name=model_hk_qfq, items=items, stock=None)


def get_ak_codes(codes):
    results = []
    for code in codes:
        results.append(to_ak_hk_code(code))
    return results


def match_us_akcodes():
    stocks = StockUsList.objects.all()
    df = read_us_spot()
    for i in range(0, len(df)):
        sym = df.iat[i, 15]
        sp = sym.split('.')
        for stock in stocks:
            if len(sp) > 1 and stock.code == sp[1]:
                stock.ak_code = sym
                stock.save()
                continue


def get_latest_date(stock_type):
    if stock_type == stock_hk:
        item = HkDailyPrices.objects.filter(code='00316').latest('trade_date')
        return item.trade_date
    if stock_type == stock_us:
        item = UsDailyPrices.objects.filter(code="106.ZTS").latest('trade_date')
        return item.trade_date


def import_latest_data(stock_type):
    now = datetime.datetime.now().date()
    print("import " + stock_type + " stocks...")
    last_date = get_latest_date(stock_type=stock_type)
    date_start = last_date + datetime.timedelta(days=1)
    date_end = now
    print("   update " + str(date_start) + " to " + str(date_end))
    update_status_to(stock_type=stock_type, status=status_to_update_his)
    try:
        if stock_type == stock_hk:
            print("    hk:")
            read_save_history_hk(start_date=date_start, end_date=date_end)
        elif stock_type == stock_us:
            print("    us:")
            read_save_history_us(start_date=date_start, end_date=date_end)
    except IntegrityError as err1:
        print("Integration Error.")


def check_if_all_finished(stock_type):
    if stock_type == stock_us:
        finished = StockUsList.objects.filter(status__contains='to').count()
        return finished == 0
    if stock_type == stock_hk:
        finished = StockHkList.objects.filter(status__contains='to').count()
        return finished == 0


def update_status_to(stock_type, status):
    if stock_type == stock_hk and check_if_all_finished(stock_hk):
        items = StockHkList.objects.all()
        for item in items:
            item.status = status
            item.save()
    if stock_type == stock_us and check_if_all_finished(stock_us):
        items = StockUsList.objects.all()
        for item in items:
            item.status = status
            item.save()

