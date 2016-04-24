from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm

def index(request):
    return render(request, 'blog/home.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def contact(request):
    return render(request, 'blog/basic.html',{'content':['If you would like to contact me, please email me.','rmaravanyika@gmail.com']})

def gallery(request):
    return render(request, 'blog/photos.html')

def post_new(request):
	form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})