import logging
import requests
import os

from datetime import datetime
from worker import app



@app.task(bind=True, name='fetch_data')
def fetch_data(self, url):
    response = requests.get(url)
    path = './data'
    if response.ok:
        if not os.path.exists(path):
            os.makedirs(path)
        slug = datetime.utcnow().strftime('%Y%m%dT%H%M%S%f')
        with open(os.path.join(path, slug), 'w') as f:
            f.write(response.text)
    else:
        raise ValueError(f'Unexpected status code: {response.status_code}')