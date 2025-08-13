# celery -A celery_addTask worker --loglevel=info
# python celery_addTaskMain.py
from celery import Celery 
# setup message broker
app = Celery("tasks", broker="amqp://guest@localhost//")
@app.task 
def add(x, y):
  return x+y 
