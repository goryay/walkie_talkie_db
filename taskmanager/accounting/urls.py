from django.urls import path
from . import views

urlpatterns = [
    path('', views.accounting_list, name='accounting_list'),
    path('create', views.accounting_create, name='accounting_create'),
    path('update/<int:id>', views.accounting_update, name='accounting_update'),
    path('delete/<int:id>', views.accounting_delete, name='accounting_delete'),
]