from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    LEVELS = (
        ("Junior", "Junior"),
        ("Middle", "Middle"),
        ("Senior", "Senior"),
    )

    level = models.CharField(max_length=10, choices=LEVELS, default="Junior")
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=300)  

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.level == "Junior":
            self.salary = 300
        elif self.level == "Middle":
            self.salary = 1000
        elif self.level == "Senior":
            self.salary = 2000
        super(CustomUser, self).save(*args, **kwargs)  

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser'
    )
