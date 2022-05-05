from django.shortcuts import render, redirect
from django.views import generic as views

# Create your views here.
from game.app_game.models import Picture

class Counter:
    COUNTER_OPENED_IMAGES=0
    NAME_FISRT_PIC=''
    NAME_SECOND_PIC=''
    ID_FIRST_PIC = 0
    ID_SECOND_PIC = 0


class IndexView(views.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        if all([x.is_known for x in Picture.objects.all().filter(order__gt=0)]):
            for each in Picture.objects.all():
                each.is_known = False
                each.is_open=False
                each.save()
        context = super().get_context_data(**kwargs)
        pictures = Picture.objects.all().order_by('order').filter(order__gt=0)
        secret=Picture.objects.get(order=0)
        if Counter.COUNTER_OPENED_IMAGES>2:
            for each in pictures:
                each.is_open=False
                each.save()

            if Counter.NAME_FISRT_PIC==Counter.NAME_SECOND_PIC:
                print("match")
                first_pic=Picture.objects.get(pk=Counter.ID_FIRST_PIC)
                first_pic.is_known=True
                first_pic.save()
                second_pic = Picture.objects.get(pk=Counter.ID_SECOND_PIC)
                second_pic.is_known = True
                second_pic.save()


            Counter.COUNTER_OPENED_IMAGES=0
            Counter.NAME_FISRT_PIC=''
            Counter.NAME_SECOND_PIC=''
            Counter.ID_FIRST_PIC = 0
            Counter.ID_SECOND_PIC = 0



        context['pictures']=pictures
        context['secret']=secret
        return context





def update_pic(request,pk):
    Counter.COUNTER_OPENED_IMAGES+=1
    pic_for_update = Picture.objects.get(pk=pk)
    pic_for_update.is_open = True
    pic_for_update.save()

    if Counter.COUNTER_OPENED_IMAGES %2 !=0:
        Counter.NAME_FISRT_PIC=pic_for_update.name
        Counter.ID_FIRST_PIC=pk
    else:
        Counter.NAME_SECOND_PIC=pic_for_update.name
        Counter.ID_SECOND_PIC = pk

    # print(pk)
    # print(Counter.NAME_FISRT_PIC)
    # print(Counter.NAME_SECOND_PIC)

    return redirect('index')
