from django.db import models

# Create your models here.

class Page(models.Model): 
    title = models.CharField(max_length=100)
    post = models.CharField(max_length=1000)

    def __str__(self):
        return self.name