# Generated by Django 3.2.3 on 2021-05-29 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_student_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.CharField(default='', editable=False, max_length=50),
        ),
    ]
