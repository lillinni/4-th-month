from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Clothes(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField(default=150)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title