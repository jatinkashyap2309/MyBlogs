from django.contrib import admin
from .models import Post
class Postadmin(admin.ModelAdmin):
    list_disp=("title","author","desc");
admin.site.register(Post,Postadmin);