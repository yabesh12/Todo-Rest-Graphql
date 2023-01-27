from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    designation = models.CharField(max_length=200, blank=True, null=True)
    mobile_number = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self) -> str:
        return f"{self.id} - {self.name}"