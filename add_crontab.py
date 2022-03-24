from crontab import CronTab
import os

cron = CronTab(user='username')
job = cron.new(command=f'pipenv run python {os.getcwd()}/users/util.py')
job.day.every(1)

cron.write()
