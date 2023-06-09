from django.db import models

# Create your models here.

class Authors(models.Model):
    name = models.CharField('Имя',max_length=100)
    surname = models.CharField(max_length=100, verbose_name='Фамилия')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
    
class Style(models.Model):
    genre = models.CharField(max_length=100, verbose_name='Жанр')
   
    def __str__(self):
        return self.genre
    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class News(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=50)
    anons = models.CharField(verbose_name='Анонс', max_length=250)
    text = models.TextField(verbose_name='Статья')
    img = models.CharField(verbose_name='Фото', max_length=250)
    authors = models.ForeignKey(Authors, on_delete = models.CASCADE)
    style = models.ForeignKey(Style, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'