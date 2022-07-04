from os import lseek
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date 

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null = True,blank=True,upload_to = 'images/')
    title_tag = models.CharField(max_length=255,)
    author =models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    def __str__ (self):
        return str(self.title) + "|" + str(self.author) 
    def get_absolute_url(self):
        #return reverse('article-detail',args=(str(self.id)))
        return reverse('home')