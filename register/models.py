from django.db import models


from django.core.validators import RegexValidator


class Register(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=100, blank=True,default='')
    lastname = models.CharField(max_length=100, blank=True,default='')
    email = models.EmailField(max_length=100, blank=True,default='')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{12}$', message="Enter country code. Phone number must be entered in the format: '919999999'.")
    phone = models.CharField(max_length=12,validators=[phone_regex], blank=True) # validators should be a list
    address_line_1 = models.CharField(max_length=100, blank=True,default='')
    address_line_2 = models.CharField(max_length=100, blank=True,default='')
    city = models.CharField(max_length=100, blank=True,default='')
    pin_regex = RegexValidator(regex=r'^\+?1?\d{6}$', message="Enter pin code.")
    pin_code = models.CharField(max_length=6,validators=[pin_regex], blank=True,default='')
    photo = models.TextField(blank=True,default='')
    password = models.CharField(max_length=100, blank=True,default='')
    access_token = models.CharField(max_length=100, blank=True,default='')
    fb_id = models.TextField(blank=True,default='')
    fb_access_token = models.TextField(blank=True,default='')
    google_id = models.TextField(blank=True,default='')
    google_access_token = models.TextField(blank=True,default='')
    
    class Meta:
        ordering = ('created',)