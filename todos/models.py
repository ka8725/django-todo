from django.db import models

class Todo(models.Model):
  NEW = 0
  DONE = 1
  STATUSES = (
    (NEW, 'New'),
    (DONE, 'Done')
  )

  name = models.TextField()
  date = models.DateField()
  status = models.PositiveSmallIntegerField(choices=STATUSES)
