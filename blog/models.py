from django.db import models
from django.urls import reverse

'''
category
----------
title,slug

Tag
------
title,slug

Post
--------
title,slug,content,created_at,photo,views,category,tags,posted_by
'''

class Category(models.Model):
    title=models.CharField(max_length=250,verbose_name='Категория')
    slug=models.SlugField(max_length=255,verbose_name='url',unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category',kwargs={'slug':self.slug})

    class Meta():
        verbose_name='Категория'
        verbose_name_plural='Категории'
        ordering=['title']

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']

class Post(models.Model):
    title=models.CharField(max_length=255,verbose_name='Название')
    slug=models.SlugField(max_length=255,verbose_name='Url',unique=True)
    content=models.TextField(blank=True,verbose_name='Контент')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='Время создания')
    photo=models.ImageField(upload_to='photos/%Y/%m/d', blank=True,verbose_name='Изображение')
    views=models.IntegerField(default=0,verbose_name='Просмотры')
    category=models.ForeignKey(Category,on_delete=models.PROTECT,related_name='posts',verbose_name='Категория')
    tags=models.ManyToManyField(Tag,blank=True,related_name='posts')
    posted_by=models.CharField(max_length=255,verbose_name='Автор',default='Unknown')

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    class Meta():
        verbose_name='Пост'
        verbose_name_plural='Посты'
        ordering=['-created_at']

    def __str__(self):
        return self.title