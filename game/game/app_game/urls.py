from django.urls import path

from game.app_game.views import IndexView, update_pic, restart, ChoiseNewFiled

urlpatterns=(
        path('',IndexView.as_view(),name='index'),
        path('<int:pk>/',update_pic,name='edit'),
        path('r/',restart,name='restart'),
        path('test/',ChoiseNewFiled.as_view(),name='choice'),
)