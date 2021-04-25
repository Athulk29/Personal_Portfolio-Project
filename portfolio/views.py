from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from blog.models import blog

# Create your views here.
def Home(request):
    projects=Project.objects.all()
    Blog=blog.objects.all()
    return render(request,'portfolio/home.html',{'projects':projects})
