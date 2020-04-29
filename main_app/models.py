from django.db import models
from django.urls import reverse

# Create your models here.

class Page(models.Model): 
    title = models.CharField(max_length=100)
    post = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'page_id': self.id})