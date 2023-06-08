from django.db import models


# Create your models here.
class YourModel(models.Model):
    # Define your fields
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
