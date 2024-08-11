from stockdaily.models import HkDailyPrices, UsDailyPrices, HkQfqFactor, UsQfqFactor


# 倒序：latest at 0
def get_qfq_f(trade_dates, factors):
    f = []
    count = 0
    for i in range(0, len(trade_dates)):
        while count < len(factors) and factors[count].trade_date > trade_dates[i]:
            count = count + 1
        if count < len(factors):
            f.append(factors[count].factor)
    return f


def get_hk_daily_closes(code, start_date, end_date):
    items = HkDailyPrices.objects.filter(code=code)\
        .filter(trade_date__gte=start_date)\
        .filter(trade_date__lte=end_date)\
        .order_by('-trade_date')
    dates = items.values_list('trade_date', flat=True)
    closes = items.values_list('close_price', flat=True)
    return list(dates), list(closes)


def get_hk_daily_closes_qfq(code, start_date, end_date):
    dates, closes = get_hk_daily_closes(code=code, start_date=start_date, end_date=end_date)
    factors = HkQfqFactor.objects.filter(code=code).order_by('-trade_date').all()
    f = get_qfq_f(trade_dates=dates, factors=factors)
    prices = []
    for i in range(0, len(f)):
        prices.append(f[i] * closes[i])
    return dates, prices
