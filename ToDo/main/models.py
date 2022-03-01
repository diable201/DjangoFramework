from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)
    created = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    due_on = models.DateTimeField(verbose_name='Due on')
    owner = models.CharField(verbose_name='Owner', max_length=200)
    done = models.BooleanField(verbose_name='Done', default=False)

    def __str__(self):
        return f'{self.title}'
