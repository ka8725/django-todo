from django.db import models

class Todo(models.Model):
  STATUSES = (
    (0, 'New'),
    (1, 'Completed')
  )
  name = models.TextField()
  date = models.DateField()
  status = models.PositiveSmallIntegerField(choices=STATUSES)
