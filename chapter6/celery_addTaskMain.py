# celery -A celery_addTask worker --loglevel=info
# python celery_addTaskMain.py
import celery_addTask 
# carry on the task
if __name__ == "__main__":
  result = addTask.add.delay(5, 5)