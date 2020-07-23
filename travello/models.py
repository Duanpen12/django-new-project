from django.db import models
from django.urls import reverse


# Create your models here.
class Destination(models.Model):
    # id: int
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField
    offer = models.BooleanField(default=False)


class Background(models.Model):
    # id: int
    name = models.CharField(max_length=100)


class Intro(models.Model):
    # id: int
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()


class Post(models.Model):
    ub_date = models.DateField()
    name = models.CharField(max_length=100)
    desc = models.TextField()

    # def get_absolute_url(self):
    #     return reverse('article-detail', kwargs={'pk': self.pk})











