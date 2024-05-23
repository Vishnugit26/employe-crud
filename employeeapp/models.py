from django.db import models

class Employee(models.Model):
    empname = models.CharField(max_length=100)
    empdesignation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='employee_images/', blank=True, null=True)