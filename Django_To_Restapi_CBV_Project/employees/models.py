
from django.db import models
from django.urls import reverse

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    esal = models.DecimalField(max_digits=10,decimal_places=2)
    eaddr = models.CharField(max_length=100)

    def __str__(self):
        return self.ename

    def get_absolute_url(self):
        return reverse('employee_list')








