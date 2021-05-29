from django.db import models
from datetime import datetime

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length =50)
    zip_code = models.IntegerField()

    def _str_(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=50)

    def _str_(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=50)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True)

    def _str_(self):
        return self.name

class Certificate(models.Model):
    name = models.CharField(max_length=50)

    def _str_(self):
        return self.name

class Grade(models.Model):
    name = models.CharField(max_length=50)
    
    def _str_(self):
        return self.type

    
class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    age = models.IntegerField()
    date_of_resumption = models.DateField(default =datetime.today)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True)
    certificate = models.ForeignKey(Certificate,on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)


    def _str_(self):
        return self.first_name
