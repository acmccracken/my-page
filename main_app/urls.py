from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pages/', views.pages_index, name='index'),
    path('pages/<int:page_id>/', views.pages_detail, name='detail'),
]