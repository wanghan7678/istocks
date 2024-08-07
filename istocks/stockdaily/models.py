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
    fq_type = models.CharField(max_length=40, default="qfq")

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
    open_price = models.FloatField()
    close_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    trade_date = models.DateField()
    volume = models.IntegerField()

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
    name = models.CharField(max_length=100)
    gics1 = models.CharField(max_length=100)
    gics2 = models.CharField(max_length=100)
    indices = models.CharField(max_length=50)


class StockHkList(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    hkcs1 = models.CharField(max_length=100)
    indices = models.CharField(max_length=50)
