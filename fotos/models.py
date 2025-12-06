from django.db import models

class Photo(models.Model):
    title = models.CharField('Название', max_length=200, blank=True)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Изображение', upload_to='photos/')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        ordering = ['id'] 
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return self.title or f'Фото #{self.pk}'

