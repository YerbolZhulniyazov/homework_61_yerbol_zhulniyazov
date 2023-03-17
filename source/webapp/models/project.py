from django.db import models
from django.utils import timezone


class Project(models.Model):
    started_at = models.DateField(
        null=False,
        blank=False,
        verbose_name='Дата начала'
    )
    finished_at = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата окончания'
    )
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Название'
    )
    description = models.TextField(
        max_length=3000,
        null=False,
        blank=False,
        verbose_name='Описание'
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        null=False,
        default=False)

    deleted_at = models.DateTimeField(
        verbose_name='Время удаления',
        null=True,
        default=None)

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def __str__(self):
        return f'{self.name}'
