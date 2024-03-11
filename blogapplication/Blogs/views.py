from django.shortcuts import render ,HttpResponseRedirect
from . forms import BlogForm
from .models import Post
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout
from .forms import Postform
def home(request):   
    posts=Post.objects.all();
    return render(request,"blog/home.html",{"Post":posts});
def about_page(request):
    return render(request,"blog/about.html");
def contact_page(request):
    return render(request,"blog/contact.html");
def dashboard_page(request):
    if request.user.is_authenticated: 
        posts=Post.objects.all();
        return render(request,"blog/dashboard.html",{"Post":posts});
    else:
        return HttpResponseRedirect("/") 
def welcome(request):
    return render(request,"blog/welcome.html");
def logout_page(request):
    if request.user.is_authenticated: 
        logout(request);
    else:
        return HttpResponseRedirect("/") 
    return HttpResponseRedirect("/");
def signup_page(request):
    if request.method=='POST':
        fm=BlogForm(request.POST);
        if fm.is_valid():
            fm.save();
            return HttpResponseRedirect('/login/');
    else:
        fm=BlogForm();
    return render(request,"blog/signup.html",{"Form":fm});
def login_page(request):
    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST);
        if fm.is_valid():
            a=fm.cleaned_data['username'];
            b=fm.cleaned_data['password'];
            new_user=authenticate(username=a,password=b);
            if not new_user is None:
                login(request,new_user);
                return HttpResponseRedirect("/home/");
            else:
                return HttpResponseRedirect("/signup/");
    else:
        fm=AuthenticationForm();
    return render(request,"blog/login.html",{"Form":fm});





def addpost(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=Postform(request.POST);
            if fm.is_valid():
                fm.save();
                fm=Postform();
        else:
            fm=Postform();
        return render(request,'blog/addpost.html',{'Form':fm});
    else:
        return HttpResponseRedirect("/login/")
def updatepost(request,id):
    if request.user.is_authenticated:
        data=Post.objects.filter(id=id).first();
        if request.method=='POST':
            fm=Postform(request.POST,instance=data);
            if fm.is_valid():
                fm.save();
                return HttpResponseRedirect('/dashboard/')
        else:
            fm=Postform(instance=data);
            return render(request,'blog/update.html',{"Form":fm});
    else:
        return HttpResponseRedirect("/login/")


def delete(request,id):
    if request.method=='POST':
        data=Post.objects.filter(id=id);
        data.delete();
    return  HttpResponseRedirect("/dashboard/");