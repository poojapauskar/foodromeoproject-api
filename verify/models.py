from django.db import models


from django.core.validators import RegexValidator


class Verify(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=100, blank=False,default='')
    password = models.CharField(max_length=100, blank=False,default='')
    confirmed = models.CharField(max_length=100, blank=False,default='')
    
    class Meta:
        ordering = ('created',)

from django.db import models

# Create your models here.
