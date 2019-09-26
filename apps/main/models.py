from django.db import models

class Option(models.Model):
  name = models.CharField(max_length=191)
  value = models.TextField()