# yourapp/tasks.py
from celery import shared_task

@shared_task
def update_user_predictions():
    # Your task logic here
    print("Hi Arshad I am great")
