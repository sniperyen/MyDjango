# coding:utf-8
from __future__ import absolute_import
from celery import shared_task
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

# The tasks you write will probably live in reusable apps, and reusable apps cannot depend on the project itself, so you also cannot import your app instance directly.
# The @shared_task decorator lets you create tasks without having any concrete app instance:

@shared_task
def add(x=10, y=10):
    logger.info('Adding {0} + {1}'.format(x, y))
    return x + y

@shared_task
def mul(x=3, y=5):
    logger.info('Muling {0} * {1}'.format(x, y))
    return x * y

@shared_task
def start_instances():
    logger.info('start_instances')

@shared_task
def stop_instances():
    logger.info('stop_instances')

