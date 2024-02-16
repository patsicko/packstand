from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import User,Blog

# Create your views here.

def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())

def about(request):
    users = User.objects.all().values()
    blogs = Blog.objects.all().values()
    template=loader.get_template('about.html')

    context = {
        'users':users,
        'blogs':blogs
    }
    return HttpResponse(template.render(context,request))

def details(request,id):
    user = User.objects.get(id=id)
    template = loader.get_template('details.html')
    context ={
        'user':user
    }

    return HttpResponse(template.render(context,request))

def blogs(request):
    blogs = Blog.objects.all().values()
    template = loader.get_template("blogs.html")
    context ={
        "blogs":blogs
    }

    return HttpResponse(template.render(context,request))
