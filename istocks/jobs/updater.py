from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler


def start():
    maintenance_hour = get_maintenance_hour()
    schedular = BackgroundScheduler()
    if maintenance_hour > 0:
        schedular.add_job(read_stock_days, 'cron', hour=maintenance_hour)
    schedular.add_job(update_stock_info, 'interval', weeks=1)


def get_maintenance_hour():
    return 1


def read_stock_days():
    pass


def update_stock_info():
    pass