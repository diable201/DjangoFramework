# Generated by Django 4.0.3 on 2022-03-01 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('due_on', models.DateTimeField(verbose_name='Due on')),
                ('owner', models.CharField(max_length=200, verbose_name='Owner')),
                ('done', models.BooleanField(default=False, verbose_name='Done')),
            ],
        ),
    ]
