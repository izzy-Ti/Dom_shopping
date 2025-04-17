from django.db import models

# Create your models here.

class products(models.Model):
    title = models.CharField(max_length=50) 
    product = models.ImageField()
    name = models.TextField()
    price = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    
