"""
URL configuration for blogapplication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Blogs import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",views.home,name='home'),
    path("",views.welcome),
    path("about/",views.about_page , name="about"),
    path("contact/",views.contact_page , name="contact"),
    path("dashboard/",views.dashboard_page , name="dashboard"),
    path("login/",views.login_page , name="login"),
    path("logout/",views.logout_page , name="logout"),
    path("signup/",views.signup_page , name="signup"),
    path('addpost/',views.addpost,name='addpost'),
    path('updatepost/<id>/',views.updatepost,name='updatepost'),
    path('delete/<id>/',views.delete,name='deletedata'),
]
