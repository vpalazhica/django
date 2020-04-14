
from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField()