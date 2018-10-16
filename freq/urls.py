from django.urls import path

from . import views

urlpatterns = [
    path('display', views.display, name='display'),
    path('cal', views.cal, name='cal'),
    path('log', views.log, name='log'),
    path('', views.index, name='index'),
]
