from django.db import models


class Note(models.Model):
    """Создание модели Note соответствующую таблице Заметки в базе данных"""
    title = models.CharField('Название', max_length=100)
    text = models.TextField('Текст заметки', max_length=1200)
    img = models.ImageField('Изображение', upload_to='img/', null=True, blank=True)
    created = models.DateTimeField('Дата создания заметки', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/'

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
