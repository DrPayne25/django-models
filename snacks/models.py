from django.db import models
from django.contrib.auth import get_user_model

class Snack(models.Model):
  name = models.CharField(max_length=64, default='Please enter a snack name')
  purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, )
  description = models.TextField(default='Please enter a description of your snack')

  def __str__(self):
    return self.name
