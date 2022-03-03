from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Employees(models.Model):
    firest_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    emp_id = models.IntegerField()