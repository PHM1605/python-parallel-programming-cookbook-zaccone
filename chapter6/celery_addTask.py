# celery -A celery_addTask worker --loglevel=info
# python celery_addTaskMain.py
from celery import Celery 
# setup message broker
app = Celery(
  "celery_addTask", 
  broker="amqp://guest:guest@localhost:5672//",
  backend="rpc://")
@app.task 
def add(x, y):
  return x+y 
