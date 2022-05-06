from django.shortcuts import render, redirect
from django.views import generic as views

# Create your views here.
from game.app_game.models import Picture

class Helper:
    COUNTER_OPENED_IMAGES=0
    NAME_FISRT_PIC=''
    NAME_SECOND_PIC=''
    ID_FIRST_PIC = 0
    ID_SECOND_PIC = 0
    LAST_CLICKED_PIC_ID= 0
    LAST_CLICKED_PIC_NAME= ''
    CLICKED_NAMES=[]


class IndexView(views.TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pictures = Picture.objects.all().order_by('order').filter(order__gt=0)
        secret=Picture.objects.get(order=0)
        context['pictures']=pictures
        context['secret']=secret
        return context

def restart(request):
    Helper.LAST_CLICKED_PIC_NAME = ''
    for each in Picture.objects.all():
        each.is_known = False
        each.is_open = False
        each.clicked=False
        each.save()

    return redirect('index')


def update_pic(request, pk):
    current_clicked_picture_name=Picture.objects.get(pk=pk).name
    if Helper.LAST_CLICKED_PIC_ID != 0:
        update_last_clicked = Picture.objects.get(pk=Helper.LAST_CLICKED_PIC_ID)
        update_last_clicked.clicked = False
        update_last_clicked.save()

    if current_clicked_picture_name==Helper.LAST_CLICKED_PIC_NAME:
        machted_pictures = Picture.objects.all().filter(name=current_clicked_picture_name)
        Helper.LAST_CLICKED_PIC_NAME=''
        for each in machted_pictures:
            each.is_known = True
            each.save()

    Helper.LAST_CLICKED_PIC_ID = pk
    Helper.LAST_CLICKED_PIC_NAME = current_clicked_picture_name

    clicked_pic = Picture.objects.get(pk=pk)
    clicked_pic.clicked = True
    clicked_pic.save()

    for each in Picture.objects.all():
        # each.is_known = False
        each.is_open = False
        # each.clicked=False
        each.save()
  
    pic_for_update = Picture.objects.get(pk=pk)
    pic_for_update.is_open = True
    pic_for_update.save()
    return redirect('index')

