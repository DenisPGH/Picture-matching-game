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
    clicked = models.BooleanField(
        default=False,
    )

class SecretPic(models.Model):
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
    clicked = models.BooleanField(
        default=False,
    )


class Field(models.Model):
    two='2x2'
    four='4x4'
    five='6x4'
    six='6x6'

    matrix=models.CharField(
        max_length=100,
        choices=((two,two),
                 (four,four),
                 (five,five),
                 (six,six),
                 )
    )
