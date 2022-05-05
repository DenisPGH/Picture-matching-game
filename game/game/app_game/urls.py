from django.urls import path

from game.app_game.views import IndexView

urlpatterns=(
        path('',IndexView.as_view(),name='index'),
)