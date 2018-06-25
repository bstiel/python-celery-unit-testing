# Unit Testing Celery Tasks

This projects contains the source code examples accompanying the blog post: https://www.python-celery.com/2018/05/01/testing-celery-tasks.html.


## With docker

1. Runt the docker stack:
```docker-compose up -d```

2. Run unit tests:
```docker-compose exec app pyton -m unittest discover -vv```
