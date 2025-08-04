from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='')
    category = models.CharField(max_length=100)
    number = models. IntegerField()
    likes = models. IntegerField(default=0)
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title