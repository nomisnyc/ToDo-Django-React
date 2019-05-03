from django.db import models
from django.utils.timezone import now

# Create your models here.

class Todo(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  completed = models.BooleanField(default=False)
  dateEntry = models.DateTimeField(default=now, blank=True)

  def _str_(self):
    return self.title