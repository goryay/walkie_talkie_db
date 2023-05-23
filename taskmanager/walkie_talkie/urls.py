from django.urls import path
from . import views

urlpatterns = [
    path('', views.walkie_talkie_list, name='walkie_talkie_list'),
    path('create', views.walkie_talkie_create, name='walkie_talkie_create'),
    path('update/<int:id>', views.walkie_talkie_update, name='walkie_talkie_update'),
    path('delete/<int:id>', views.walkie_talkie_delete, name='walkie_talkie_delete'),
]