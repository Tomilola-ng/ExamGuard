from ctypes.wintypes import tagMSG
from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager



# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField()
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    date = models.DateTimeField(default = timezone.now )
    viewcount = models.IntegerField(default=0)
    imgurl = models.TextField(null = True)
    tags = TaggableManager()

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id])

    def number_of_views(self):
        return self.viewcount

    def __str__(self):
        return self.title
    


    