import asyncio
import os

import django
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

from users.util import print_stats

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "insta_map.settings")
django.setup()


if __name__ == '__main__':
    scheduler = AsyncIOScheduler()

    scheduler.add_job(print_stats, trigger=IntervalTrigger(weeks=1))

    scheduler.start()
    # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass