from celery import task

@task()
def add(x, y):
    return x + y

@task()
def mux(x, y):
    return x * y    