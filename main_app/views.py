from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class PageCreate(CreateView):
  model = Page
  fields = '__all__'
  
class PageCreate(CreateView):
  model = Page
  fields = ['title', 'post']

class PageUpdate(UpdateView):
  model = Page
  fields = ['title', 'post']

class PageDelete(DeleteView):
  model = Page
  success_url = '/pages/'
