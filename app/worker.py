import os
from celery import Celery


CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']


app = Celery(__name__)
app.conf.update({
    'broker_url': CELERY_BROKER_URL,
    'imports': (
        'tasks',
    ),
    'task_serializer': 'json',
    'result_serializer': 'json',
    'accept_content': ['json']})