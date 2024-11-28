from django.db import models


class Jutsu(models.Model):
    title = models.CharField(max_length=900)
    image = models.ImageField(null=True)
    tooltip = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title