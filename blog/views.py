from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import blog
# Create your views here.
def all_blogs(request):
    #return HttpResponse('<h1>this is my profile</h1>')
    blogs=blog.objects.order_by('-date')
    return render(request,'blog/all_blog.html',{'blogs':blogs})
def detail(request, blog_id):
    blogs=get_object_or_404(blog, pk=blog_id)
    return render(request,'blog/detail.html',{'blogs':blogs})
