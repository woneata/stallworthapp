# Generated by Django 3.2.3 on 2021-05-29 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210529_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='department',
        ),
    ]
