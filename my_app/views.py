from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Subscriber
from .forms import BlogForm

# Create your views here.

def index(request):
  blogs = [
    {'title': 'Learning Django', 'content': 'Django is an awesome open source framework for building APIs using Django REST Framework', 'author': 'John Doe', 'date': '2024-06-04'},

    {'title': 'Learning Django', 'content': 'Django is an awesome open source framework for building APIs using Django REST Framework', 'author': 'John Doe', 'date': '2024-06-04'},

    {'title': 'Learning Django', 'content': 'Django is an awesome open source framework for building APIs using Django REST Framework', 'author': 'John Doe', 'date': '2024-06-04'},

    {'title': 'Learning Django', 'content': 'Django is an awesome open source framework for building APIs using Django REST Framework', 'author': 'John Doe', 'date': '2024-06-04'},
  ]

  context = {'blogs': blogs}
  return render(request, 'index.html', context)

def about(request):

  return render(request, 'about.html')

def contact(request):
  
  return render(request, 'contact.html')

def blog_list(request):
    blogs= Blog.objects.all()
    context = {'blogs' : blogs}
    return render(request, 'blog_list.html', context)

def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, 'You are already subscribed.')
        else:
            subscriber = Subscriber(email=email)
            subscriber.save()
            messages.success(request, 'Thank you for subscribing!')
            return redirect('subscribe')
    return render(request, 'subscribe.html')

def add_blog(request):
   if request.METHOD == 'POST':
      form = BlogForm(request.POST)
      if form.is_valid():
         blog = form.save()
         return redirect('blog_list')
      else:
         form = BlogForm()
      return render(request, 'add_blog.html', {'form': form})