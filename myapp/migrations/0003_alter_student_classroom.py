# Generated by Django 5.0.2 on 2024-02-29 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classroom_students', to='myapp.classroom'),
        ),
    ]