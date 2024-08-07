from django.db import models

# Create your models here.


class HkDailyPrices(models.Model):
    code = models.CharField(max_length=100)
    open_price = models.FloatField()
    close_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    trade_date = models.DateField()
    volume = models.IntegerField()
    turnover_rate = models.FloatField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['code', 'trade_date'],
                name='hk_day_price_code_date'
            ),
        ]


class HkQfqFactor(models.Model):
    code = models.CharField(max_length=100)
    trade_date = models.DateField()
    factor = models.FloatField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['code', 'trade_date'],
                name='hk_qfq_code_date'
            ),
        ]


class UsDailyPrices(models.Model):
    code = models.CharField(max_length=100)
    trade_date = models.DateField()
    open_price = models.FloatField()
    close_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    volume = models.IntegerField()
    turnover_rate = models.FloatField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['code', 'trade_date'],
                name='us_day_price_code_date'
            ),
        ]


class UsQfqFactor(models.Model):
    code = models.CharField(max_length=100)
    trade_date = models.DateField()
    factor = models.FloatField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['code', 'trade_date'],
                name='us_qfq_code_date'
            ),
        ]


class StockUsList(models.Model):
    code = models.CharField(max_length=50)
    ak_code = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100)
    gics1 = models.CharField(max_length=100)
    gics2 = models.CharField(max_length=100)
    indices = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=100, null=True)


class StockHkList(models.Model):
    code = models.CharField(max_length=50)
    ak_code = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100)
    hkcs1 = models.CharField(max_length=100)
    indices = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=100, null=True)
