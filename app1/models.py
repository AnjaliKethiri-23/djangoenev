from django.db import models

class emp_table(models.Model):
    pin = models.IntegerField(unique=True)
    name = models.CharField(max_length=20)
    salary = models.FloatField()
    email = models.EmailField(unique=True)

    dept = [
        ('IT', 'IT'),
        ('SALES', 'SALES'),
        ('ADMIN', 'ADMIN')
    ]

    department = models.CharField(max_length=10, choices=dept)