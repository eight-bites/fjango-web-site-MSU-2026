from django.urls import path

from . import views

urlpatterns = [
    path('', views.glavnaya, name='glavnaya'),
    path('catalog/', views.katalog, name='katalog'),
    path('catalog/add/', views.dobavit, name='dobavit'),
    path('catalog/<int:id>/', views.kartochka, name='kartochka'),
    path('catalog/<int:id>/delete/', views.udalit, name='udalit'),
]
