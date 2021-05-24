from django import db
from django.db import models
from django.db.models.expressions import OrderBy
from django.db.models.fields import CharField, reverse_related
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    meta_description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    class Meta:
        Ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('community:post_in_category', args=[self.slug])

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_post')
    title = models.CharField(max_lengt=200)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    title_image = models.ImageField(blank=True)
    comtemt = models.TextField()
    createData = models.DateTimeField(auto_now=True)
    updateDate = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, on_delete=models.SET_NULL,null=True,related_name='posts')
    view_cnt = models.IntegerField(max_langth=50)
    like_users = models.ManyToManyField(User, related_name='like_posts')
    hits = models.PositiveBigIntegerField(default=0)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("community:post_detail", args=[self.id,self.slug])