from models import HkDailyPrices, UsDailyPrices, HkQfqFactor, UsQfqFactor


# 倒序：
def get_qfq_(prices, factors):
    for i in range(0, len(prices)):
        t_date = prices[i].trade_date
        for j in range(0, len(factors)):
            f_date = factors[j].trade_date




