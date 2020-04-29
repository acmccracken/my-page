from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pages/', views.pages_index, name='index'),
    path('pages/<int:page_id>/', views.pages_detail, name='detail'),
    path('pages/create/', views.PageCreate.as_view(), name='pages_create'),
    path('pages/<int:pk>/update/', views.PageUpdate.as_view(), name='pages_update'),
    path('pages/<int:pk>/delete/', views.PageDelete.as_view(), name='pages_delete'),
]