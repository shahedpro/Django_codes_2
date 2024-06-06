from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    father = models.TextField(default="rahim")
    def __str__(self):
        return f"{self.first_name} {self.last_name}"