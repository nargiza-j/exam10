import datetime

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

AD_STATUS = (('For moderation', 'На модерацию'), ('Published', 'Опубликовано'), ('Rejected', 'Отклонено'))


class Ad(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads', verbose_name='Автор')
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Заголовок')
    text = models.TextField(max_length=500, null=False, blank=False, verbose_name='Описание')
    category = models.ForeignKey('webapp.Category', on_delete=models.CASCADE, related_name='ads', verbose_name='Категория')
    status = models.CharField(max_length=50, default='For moderation', choices=AD_STATUS, verbose_name='Статус')
    photo = models.ImageField(upload_to="uploads/", null=True, blank=True, verbose_name='Фото')
    price = models.PositiveIntegerField(null=True, blank=True, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    published_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата публикации")
    is_deleted = models.BooleanField(null=True, blank=True, default=False, verbose_name='Удален')

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def set_status_reject(self):
        self.status = "Rejected"
        self.save()

    def set_status_approve(self):
        self.status = "Published"
        self.published_at = datetime.datetime.now()
        self.save()

    class Meta:
        db_table = 'ads'
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return f'{self.id}.{self.author}: {self.title}'


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Название категории')

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'

