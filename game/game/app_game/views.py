import random
import time

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django import forms

# Create your views here.
from game.app_game.models import Picture, SecretPic, Field


class InfoLastClickedPic:
    LAST_CLICKED_PIC_ID= 0
    LAST_CLICKED_PIC_NAME= ''



class HelperRandomFuctions:
    RANDOM_LIST_OF_PICS=[]
    ID_LIST=[]
    CURRENT_QUERYSET=[]

    def return_random_list(pairs:int):
        """this function generate random queryset for current game
        it got count of the pairs"""
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
        HelperRandomFuctions.RANDOM_LIST_OF_PICS=pictures_list

        return pictures_list
    @staticmethod
    def return_ids_choosed_pics():
        """ store the new values of ids, and queryset"""
        id_list=[x.id for x in HelperRandomFuctions.RANDOM_LIST_OF_PICS]
        HelperRandomFuctions.ID_LIST=id_list
        HelperRandomFuctions.CURRENT_QUERYSET=Picture.objects.filter(id__in=HelperRandomFuctions.ID_LIST)

        return HelperRandomFuctions.ID_LIST



class IndexView(views.TemplateView):
    """ show the html with the game, and pictures"""
    template_name = 'index.html'
    VALUE_PAIRS_PICTRURES=16
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pictures_list = [] # new queryset with current order
        for each_id in HelperRandomFuctions.ID_LIST:
            pictures_list.append(Picture.objects.get(id=each_id))
        # return the values
        secret=SecretPic.objects.get(order=0)
        context['pictures']=pictures_list
        context['secret']=secret
        return context




def restart(request):
    """ restart all rulls, start new game"""
    HelperRandomFuctions.ID_LIST = []
    HelperRandomFuctions.return_ids_choosed_pics()
    HelperRandomFuctions.return_random_list(IndexView.VALUE_PAIRS_PICTRURES)  # old
    #HelperRandomFuctions.return_random_list(int(Field.objects.last().matrix.split('x')[0])) # new
    InfoLastClickedPic.LAST_CLICKED_PIC_NAME = ''
    for each in Picture.objects.all():
        each.is_known = False
        each.is_open = False
        each.clicked=False
        each.save()

    return redirect('index')


def update_pic(request, pk):
    current_clicked_picture_name=Picture.objects.get(pk=pk).name
    """ update the info of last clicked pic, it could be click again"""
    if InfoLastClickedPic.LAST_CLICKED_PIC_ID != 0:
        update_last_clicked = Picture.objects.get(pk=InfoLastClickedPic.LAST_CLICKED_PIC_ID)
        update_last_clicked.clicked = False
        update_last_clicked.save()
    """ check if last and current clicked are same"""
    if current_clicked_picture_name==InfoLastClickedPic.LAST_CLICKED_PIC_NAME:
        machted_pictures = Picture.objects.filter(name=current_clicked_picture_name)
        InfoLastClickedPic.LAST_CLICKED_PIC_NAME= ''
        for each in machted_pictures:
            each.is_known = True
            each.save()
    """ update the value of last clicked pictures"""
    InfoLastClickedPic.LAST_CLICKED_PIC_ID = pk
    InfoLastClickedPic.LAST_CLICKED_PIC_NAME = current_clicked_picture_name
    """ update the current clicked picture, to be clicked, cant click two times on it"""
    clicked_pic = Picture.objects.get(pk=pk)
    clicked_pic.clicked = True
    clicked_pic.save()

    """ close all pictures"""
    for each in Picture.objects.all():
        each.is_open = False
        each.save()
    """ open only the clicked picture"""
    pic_for_update = Picture.objects.get(pk=pk)
    pic_for_update.is_open = True
    pic_for_update.save()
    return redirect('index')




"""some tests """
class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ('matrix',)


class ChoiseNewFiled(views.CreateView):

    template_name = 'choice.html'
    model = Field
    fields = '__all__'
    # form_class = FieldForm
    # # def get_context_object_name(self, obj):
    # #     print(f'test={self.object.id}')
    # # def get_context_data(self, **kwargs):
    # #     context = super().get_context_data(**kwargs)
    # #     #print(context['view'])
    # #     return context
    success_url = reverse_lazy('index')
    # #
    # def form_valid(self, form):
    #     print(f'test={self.kwargs["matrix"]}')
    #     print(self.content_type)
    #
    #     return super(ChoiseNewFiled,self).form_valid(form)




