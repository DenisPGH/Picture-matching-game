from django.db import models

# Create your models here.

class Picture(models.Model):
    name=models.CharField( max_length=100)
    pic=models.ImageField(
        upload_to='media')
    is_open=models.BooleanField(
        default=False
    )
    is_known=models.BooleanField(
        default=False,
    )
    order=models.IntegerField(
        default=0
    )
