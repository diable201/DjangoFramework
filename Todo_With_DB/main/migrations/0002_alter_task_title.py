# Generated by Django 4.0.3 on 2022-03-07 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Task'),
        ),
    ]
