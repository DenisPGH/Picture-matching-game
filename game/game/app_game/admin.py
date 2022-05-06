from django.contrib import admin

# Register your models here.
from game.app_game.models import Picture, SecretPic


@admin.register(Picture)
class TaskPicture(admin.ModelAdmin):
    list_display = ('order','name','pic','is_known','is_open')


@admin.register(SecretPic)
class TaskSecret(admin.ModelAdmin):
    list_display = ('order','name','pic','is_known','is_open')

