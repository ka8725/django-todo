from django.db import models

class Todo(models.Model):
  NEW = 0
  FIXED = 1
  STATUSES = (
    (NEW, 'New'),
    (FIXED, 'Fixed')
  )

  name = models.TextField()
  date = models.DateField()
  status = models.PositiveSmallIntegerField(choices=STATUSES, default=NEW)

  def fix(self):
    self.status = self.FIXED
    self.save()

  def __unicode__(self):
    return self.name
