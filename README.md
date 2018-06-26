# Unit Testing Celery Tasks

This projects contains the source code examples accompanying the blog post: https://www.python-celery.com/2018/05/01/unit-testing-celery-tasks.

Docker use is highly recommended.

## With docker

1. Bring up the docker stack:
```docker-compose up -d```

2. Run unit tests:
```docker-compose exec app pyton -m unittest discover -vv```


## Without docker

1. Install and start [RabbitMQ](https://www.rabbitmq.com):
Ensure RabbitMQ runs on port 5672 and the user `user` with password `password` is set up

2. Create virtual environment:
```virtualenv celery-unit-test```

3. Activate virtual environment:
```source activate celery-unit-test```

4. Install pip packages:
```pip install -r requirements.txt```

5. Run unit tests:
```RABBITMQ_DEFAULT_USER=user CELERY_BROKER_URL=amqp://user:password@localhost:5672 python -m unittest discover -vv```
