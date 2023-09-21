from celery import shared_task
import django
django.setup()

from djangoproject.views import update_stats_data
from prediction.models import Stats

@shared_task
def update_user_predictions():
    update_stats_data()
    print("Done")
