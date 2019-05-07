from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
    posts = Post.objects
    context={
        'posts':posts,

    }
    return render(request,'home.html',context)

