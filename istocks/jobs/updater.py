from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
import stockdaily.service as s

def start():
    schedular = BackgroundScheduler()
    schedular.add_job(read_stock_days_hk, 'cron', day_of_week='mon-fri', hour=11)


def get_maintenance_hour():
    return 11


def read_stock_days_hk():
    s.prepare_to_update_daily_hk()

    pass


def update_stock_info():
    pass