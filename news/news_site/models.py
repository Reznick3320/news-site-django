from pyexpat import model
from django import views
from django.db import models
from django.urls import reverse

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Найменование')
    content = models.TextField(blank=True, verbose_name='Контент')
    create_up = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_up = models.DateTimeField(auto_now=True, verbose_name='Дата измениния')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    is_pablished = models.BooleanField(default=True, verbose_name='Публикация')
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.PROTECT, null=True)
    views = models.IntegerField(default=0, verbose_name='Просмотры')

    def get_absolute_url(self):
        return reverse("view_news", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-create_up']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Найменование категории')

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_id": self.pk})
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']