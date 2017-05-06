from celery import shared_task


@shared_task
def charge():
    print("charging")
