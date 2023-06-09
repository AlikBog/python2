from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=50)
    anons = models.CharField(verbose_name='Анонс', max_length=250)
    text = models.TextField(verbose_name='Статья')
    img = models.CharField(verbose_name='Фото', max_length=250)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'



     
