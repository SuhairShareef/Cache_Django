import random
from django.db import models


class Student(models.Model):
    std_number = models.CharField(max_length=10, primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.std_number:
            self.std_number = str(random.randint(1000000000, 9999999999))
        super().save(*args, **kwargs)
