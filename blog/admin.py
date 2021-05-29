from django.contrib import admin
from .models import Certificate, Department, Faculty, Grade, School, Student
# Register your models here.
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Grade)
admin.site.register(Department)
admin.site.register(Certificate)
