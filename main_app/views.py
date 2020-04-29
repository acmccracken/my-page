from django.shortcuts import render
from .models import Page


def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pages_index(request):
    pages = Page.objects.all()
    return render(request, 'pages/index.html', { 'pages': pages })

def pages_detail(request, page_id):
  page = Page.objects.get(id=page_id)
  return render(request, 'pages/detail.html', { 'page': page })
  


