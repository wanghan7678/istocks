import time
from django.db import IntegrityError
from stockdaily.models import StockHkList, StockUsList, HkDailyPrices, HkQfqFactor, UsQfqFactor, UsDailyPrices
from stockdaily.util import to_ak_hk_code, to_int, to_float, to_date, ak_date_format
from stockdaily.akreader import read_hk_qfq, read_us_qfq, read_hk_hist, read_us_hist, read_us_spot

status_to_update_qfq = "to qfq"
status_to_update_his = "to his"
status_to_update_daily = "to daily"
status_finished = "finished"
status_update_error = "update error"


def retrieve_history_hk(start_date, end_date):
    stocks = StockHkList.objects.filter(status=status_to_update_his).all()
    for stock in stocks:
        items = read_hk_hist(code=stock.code, start_date=start_date, end_date=end_date)
        save_hk_daily(items=items, stock=stock)
        time.sleep(5)


def retrieve_history_us(start_date, end_date):
    stocks = StockUsList.objects.filter(status=status_to_update_his).all()
    for stock in stocks:
        if stock.ak_code:
            items = read_us_hist(code=stock.ak_code, start_date=start_date, end_date=end_date)
            save_us_daily(items=items, stock=stock)
            time.sleep(5)


def retrieve_qfq_hk():
    stocks = StockHkList.objects.filter(status=status_to_update_qfq).all()
    for stock in stocks:
        items = read_hk_qfq(code=stock.code)
        save_hk_qfq(items=items)
        stock.status = status_finished
        stock.save()
        time.sleep(3)


def retrieve_qfq_us():
    stocks = StockUsList.objects.filter(status=status_to_update_qfq).all()
    for stock in stocks:
        items = read_us_qfq(code=stock.code)
        save_us_qfq(items=items)
        stock.status = status_finished
        stock.save()
        time.sleep(3)


def update_hk_akcodes():
    for item in StockHkList.objects.all():
        item.code = to_ak_hk_code(item.code)
        item.save()


def retrieve_qfq_hk_one(ak_code):
    items = read_hk_qfq(code=ak_code)
    save_hk_qfq(items=items)


def get_ak_codes(codes):
    results = []
    for code in codes:
        results.append(to_ak_hk_code(code))
    return results


def save_hk_daily(items, stock):
    try:
        print("       " + str(len(items)) + "  saved.")
        HkDailyPrices.objects.bulk_create(items)
        stock.status = status_finished
    except IntegrityError as err1:
        print("duplicated key error: ", type(err1).__name__)
        stock.status = status_update_error
    except Exception as err:
        print("An error: ", type(err).__name__)
        stock.status = status_update_error
    finally:
        stock.save()


def save_us_daily(items, stock):
    try:
        print("       " + str(len(items)) + "  saved.")
        UsDailyPrices.objects.bulk_create(items)
        stock.status = status_finished
    except IntegrityError as err1:
        print("duplicated key error: ", type(err1).__name__)
        stock.status = status_update_error
    except Exception as err:
        print("An error: ", type(err).__name__)
        stock.status = status_update_error
    finally:
        stock.save()


def save_hk_qfq(items):
    try:
        print("      " + str(len(items)) + "  saved.")
        HkQfqFactor.objects.bulk_create(items)
    except IntegrityError as err1:
        print("duplicated key error: ", type(err1).__name__)
    except Exception as err:
        print("An error: ", type(err).__name__)


def save_us_qfq(items):
    try:
        print("      " + str(len(items)) + "  saved.")
        UsQfqFactor.objects.bulk_create(items)
    except IntegrityError as err1:
        print("duplicated key error: ", type(err1).__name__)
    except Exception as err:
        print("An error: ", type(err).__name__)


def prepare_to_update_history_hk():
    stocks = StockHkList.objects.all()
    for st in stocks:
        st.status = status_to_update_his
        st.save()


def prepare_to_update_history_us():
    stocks = StockUsList.objects.all()
    for st in stocks:
        st.status = status_to_update_his
        st.save()


def prepare_to_update_qfq_hk():
    stocks = StockHkList.objects.all()
    for st in stocks:
        st.status = status_to_update_qfq
        st.save()


def prepare_to_update_qfq_us():
    stocks = StockUsList.objects.all()
    for st in stocks:
        st.status = status_to_update_qfq
        st.save()


def prepare_to_update_daily_hk():
    stocks = StockHkList.objects.all()
    for st in stocks:
        st.status = status_to_update_daily
        st.save()


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
