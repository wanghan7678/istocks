# Generated by Django 4.1.3 on 2024-08-07 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockdaily', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HKQfqDaily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('open_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('high_price', models.FloatField()),
                ('low_price', models.FloatField()),
                ('trade_date', models.DateField()),
                ('volume', models.IntegerField()),
                ('fq_type', models.CharField(default='qfq', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='USQfqDaily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('open_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('high_price', models.FloatField()),
                ('low_price', models.FloatField()),
                ('trade_date', models.DateField()),
                ('volume', models.IntegerField()),
                ('fq_type', models.CharField(default='qfq', max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='StockDailyPrices',
        ),
    ]