from django.shortcuts import render
from blog.models import Post

# Create your views here.


def blogHome(request):
    allPosts = Post.objects.all()
    return render(request, "blogHome.html", {'allPosts':allPosts})

# def blogPost(request):
#     return render(request, "blogPost.html")

def blogPost(request, slug):
    blogpost = Post.objects.filter(slug=slug).first()
    return render(request, "blogPost.html", {'blogpost':blogpost})