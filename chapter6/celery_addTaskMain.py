# celery -A celery_addTask worker --loglevel=info
# python celery_addTaskMain.py
import celery_addTask 
# carry on the task
if __name__ == "__main__":
  result = celery_addTask.add.delay(5, 5)
  print("Task ID: ", result.id)
  print("Result: ", result.get(timeout=10))