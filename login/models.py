from django.db import models


from django.core.validators import RegexValidator


class Login(models.Model):
    email = models.EmailField(max_length=100, blank=False,default='')
    password = models.CharField(max_length=100, blank=False,default='')
    
    # class Meta:
    #     ordering = ('created',)