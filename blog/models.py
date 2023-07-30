from django.db import models
from autoslug import AutoSlugField
# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.CharField(max_length=20)
    image = models.ImageField(upload_to='blog_images', default='blog_images/blog-1.jpg')
    # slug = models.CharField(max_length=122)
    slug = AutoSlugField(populate_from='title')
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author
