from django.db import models

# Create your models here.


class StockDailyPrices(models.Model):
    code = models.CharField(max_length=100)
    exchange = models.CharField(max_length=40)
    open_price = models.FloatField()
    close_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    trade_date = models.DateField()
    volume = models.IntegerField()
    fq_type = models.CharField(max_length=40, default="qfq")


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
