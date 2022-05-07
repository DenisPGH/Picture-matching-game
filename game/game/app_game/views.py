import random
import time

from django.shortcuts import render, redirect
from django.views import generic as views

# Create your views here.
from game.app_game.models import Picture, SecretPic


class Helper:
    # COUNTER_OPENED_IMAGES=0
    # NAME_FISRT_PIC=''
    # NAME_SECOND_PIC=''
    # ID_FIRST_PIC = 0
    # ID_SECOND_PIC = 0
    LAST_CLICKED_PIC_ID= 0
    LAST_CLICKED_PIC_NAME= ''


""" den"""
class RandomGeneratedPics:
    RANDOM_LIST_OF_PICS=[]
    ID_LIST=[]
    CURRENT_QUERYSET=[]

    def return_random_list(pairs:int):
        """this function generate random queryset for current game"""
        # take value of wishes pictures pairs
        all_names_pictures = set(x.name for x in Picture.objects.all())
        random_names = random.sample(list(all_names_pictures), min(len(all_names_pictures), pairs))
        pictures = Picture.objects.filter(name__in=random_names)

        # take a random order for the choosed pictures
        valid_ids_list = pictures.values_list('id', flat=True)
        random_ids_list = random.sample(list(valid_ids_list), min(len(valid_ids_list), len(pictures)))
        pictures_list = []
        for each_id in random_ids_list:
            pictures_list.append(Picture.objects.get(id=each_id))
        # pictures = pictures.filter(id__in=random_ids_list)
        RandomGeneratedPics.RANDOM_LIST_OF_PICS=pictures_list

        return pictures_list
    @staticmethod
    def return_ids_choosed_pics():
        """ store the new values of ids, and queryset"""
        id_list=[x.id for x in RandomGeneratedPics.RANDOM_LIST_OF_PICS]
        RandomGeneratedPics.ID_LIST=id_list
        RandomGeneratedPics.CURRENT_QUERYSET=Picture.objects.filter(id__in=RandomGeneratedPics.ID_LIST)

        return RandomGeneratedPics.ID_LIST



class IndexView(views.TemplateView):
    template_name = 'index.html'
    VALUE_PAIRS_PICTRURES=6 # *2
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pictures=Picture.objects.filter(id__in=RandomGeneratedPics.ID_LIST)
        print(pictures)
        # return the values
        secret=SecretPic.objects.get(order=0)
        context['pictures']=pictures
        context['secret']=secret
        return context




def restart(request):
    RandomGeneratedPics.ID_LIST = []
    RandomGeneratedPics.return_ids_choosed_pics()
    RandomGeneratedPics.return_random_list(IndexView.VALUE_PAIRS_PICTRURES)
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
        machted_pictures = Picture.objects.filter(name=current_clicked_picture_name)
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

