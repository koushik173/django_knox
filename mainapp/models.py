from django.db import models

# Create your models here.

# Create your models here.
class Standard(models.Model):
    name = models.CharField(max_length=266)

    def __str__(self):
        return self.name

class Student(models.Model):
    name  = models.CharField(max_length=266)
    age = models.IntegerField()
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

