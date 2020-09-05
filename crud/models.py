from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=15)
    address=models.CharField(max_length=100)
    village=models.CharField(max_length=100)
    class Meta:
        db_table='student1'