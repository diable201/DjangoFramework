from django.db import models
from users.models import User


class TodoList(models.Model):
    title = models.CharField(
        verbose_name='Title',
        max_length=100
    )

    class Meta:
        verbose_name = 'Группа задач'
        verbose_name_plural = 'Группы задач'

    def __str__(self):
        return f'{self.title}'


class Task(models.Model):
    IN_PROGRESS = 'IN_PROGRESS'
    DONE = 'DONE'
    STATUSES = (
        (IN_PROGRESS, 'В прогрессе'),
        (DONE, 'Выполнено')
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Владелец',
        max_length=200
    )
    group = models.ForeignKey(
        TodoList,
        on_delete=models.CASCADE,
        verbose_name='Группа'
    )
    title = models.CharField(
        verbose_name='Название',
        max_length=100,
        blank=True
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        blank=True
    )
    due_date = models.DateTimeField(
        verbose_name='Дедлайн',
        blank=True,
    )
    status = models.CharField(
        verbose_name='Статус Задачи',
        max_length=100,
        choices=STATUSES,
        default=IN_PROGRESS
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-due_date']

    def __str__(self):
        return f'{self.title} - {self.owner}'
