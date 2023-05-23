from django.urls import path
from . import views

urlpatterns = [
    path('', views.state_list, name='state_list'),
    path('create', views.state_create, name='state_create'),
    path('update/<int:id>', views.state_update, name='state_update'),
    path('delete/<int:id>', views.state_delete, name='state_delete'),
]