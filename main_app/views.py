from django.shortcuts import render

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pages_index(request):
  return render(request, 'pages/index.html', { 'pages': pages })


class Page:  # Note that parens are optional if not inheriting from another class
  def __init__(self, title, post):
    self.title = title
    self.post = post
    
pages = [
    Page('Title', 'This is a temperary string of words'),
    Page('Also a title', 'Lets have 2')
]