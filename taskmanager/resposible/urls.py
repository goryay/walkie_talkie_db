from django.urls import path
from . import views

urlpatterns = [
    path('', views.resposible_list, name='resposible_list'),
    path('create', views.resposible_create, name='resposible_create'),
    path('update/<int:id>', views.resposible_update, name='resposible_update'),
    path('delete/<int:id>', views.resposible_delete, name='resposible_delete'),
]