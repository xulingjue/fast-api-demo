from apscheduler.schedulers.blocking import BlockingScheduler

from app.jobs.demo_job import demo_job


def create_scheduler() -> BlockingScheduler:
    scheduler: BlockingScheduler = BlockingScheduler()

    register_job(scheduler)

    return scheduler


def register_job(scheduler):
    """
     注册调度任务
    """
    scheduler.add_job(demo_job, 'interval', seconds=5)
