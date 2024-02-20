from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate, login
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


def signup(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.get(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email address already exists'})

        hashed_password= make_password(password)

        user = User.objects.create( 
            firstName=firstName,
            lastName=lastName,
            phone=phone,
            email=email,
            password=hashed_password)
        
        print("created usr",user)

        return redirect('/login')

    return render(request, 'signup.html')    


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user= User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is not None:

            if check_password(password,user.password):
                print("loged user",user)
                return redirect('about')

            else: return render(request,'404.html')
            
        
    return render(request,'login.html')



