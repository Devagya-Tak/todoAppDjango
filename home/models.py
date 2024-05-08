from django.db import models

class Todo(models.Model):
  todo_title = models.CharField(max_length=100)
  todo_desc = models.CharField(max_length=300)
  is_done = models.BooleanField(default=False)