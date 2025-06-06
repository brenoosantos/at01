from django.db import models

class Produto(models.Model):
    name= models.CharField(max_length=100)
    descriptions = models.TextField()
    image = models.ImageField(upload_to='Produtos/')

    def __str__(self):
        return self.name