# Generated by Django 3.2.3 on 2021-05-29 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_student_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grade',
            old_name='type',
            new_name='name',
        ),
    ]