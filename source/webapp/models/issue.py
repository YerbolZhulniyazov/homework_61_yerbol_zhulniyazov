from django.db import models
from django.utils import timezone


class Issue(models.Model):
    summary = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        verbose_name='Подробное описание'
    )
    status = models.ForeignKey(
        'webapp.Status',
        related_name='statuses',
        on_delete=models.PROTECT,
        verbose_name='Статус'
    )
    type = models.ManyToManyField(
        to='webapp.Type',
        related_name='types',
        blank=True,
        verbose_name='Тип'
    )
    project = models.ForeignKey(
        'webapp.Project',
        related_name='issues',
        on_delete=models.PROTECT,
        verbose_name='Проект'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления",
        null=True
    )
    is_deleted = models.BooleanField(
        verbose_name="Удалено",
        default=False,
        null=False)

    deleted_at = models.DateTimeField(
        verbose_name='Время удаления',
        null=True,
        default=None)

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def __str__(self):
        return f'{self.summary} - {self.description}'


