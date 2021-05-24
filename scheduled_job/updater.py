from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from scheduled_job import job

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job.update, 'interval', minutes=1)
    scheduler.start()